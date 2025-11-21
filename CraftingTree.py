from Item import Item
from CraftingElement import CraftingElement
from Outcome import PossibleItemOutcome, PossibleCurrencyEffect
from collections import deque
from functools import lru_cache
from typing import Dict, List, Optional, Set, Tuple

@lru_cache(maxsize=None)
def getSlammingOutcomes(item : Item, craftingElem: CraftingElement) -> list[PossibleItemOutcome]:
    if not all(cond.value.isSatisfiedBy(item) for cond in craftingElem.conditions):
        # print(f"When slamming {craftingElem} on \n{item}, some conditions are not satisfied")
        return []
    
    applicableOutcomes: list[PossibleCurrencyEffect] = []

    outcomes : set[PossibleItemOutcome] = set()
    for possibleCurrencyEffect in craftingElem.getPossibleCurrencyEffectsFor(item):
        applicableOutcomes.append(possibleCurrencyEffect)
    
    for possibleCurrencyEffect in applicableOutcomes:
        total_weight = sum([x.weight for x in applicableOutcomes])
        outcome_probability = int((possibleCurrencyEffect.weight / total_weight) * 100)
        outcomes.add(possibleCurrencyEffect.applyEffectOn(item, outcome_probability))
    return list(outcomes)

class CraftTreeNode:
    def __init__(self, outcome: PossibleItemOutcome, nodeProbability: int,parent: Optional["CraftTreeNode"] = None, used_elem: Optional[CraftingElement] = None):
        self.outcome = outcome
        self.parent = parent
        self.used_elem = used_elem
        self.children: Dict[CraftingElement, List["CraftTreeNode"]] = {}
        self.nodeProbability: int = nodeProbability

    def add_child(self, elem: CraftingElement, child_node: "CraftTreeNode"):
        self.children.setdefault(elem, []).append(child_node)

    def path_from_root(self) -> List[Tuple[CraftingElement, Item]]:
        node, path = self, []
        while node.parent is not None:
            path.append((node.used_elem, node.outcome))
            node = node.parent
        return list(reversed(path))

    def __repr__(self):
        return f"Node({self.outcome})"


class TreePath:
    def __init__(self, path : List[List[Tuple[CraftingElement, PossibleItemOutcome]]]):
        self.path = path
        
    def __repr__(self) -> str:
        lines : List[str] = []
        for path in self.path:
            lines.append('=== New Path ===')
            for step in path:
                lines.append(f"Using {step[0].name}, and gives {step[1].probability}% chance to get")
                lines.append(str(step[1].item))
        return "\n".join(lines)

class CraftingTree:
    def __init__(self, root_item: Item):
        self.root = CraftTreeNode(PossibleItemOutcome(root_item), 100)

    def find_paths_to_target(self, target_item: Item, available_elements: List[CraftingElement], max_depth: int = 10) -> tuple[TreePath, int]:
        found_paths = []
        visited: Set[int] = set()

        # BFS queue: (node, current_depth)
        queue = deque([(self.root, 0)])
        visited.add(hash(self.root.outcome))
        visited_skip_count = 0

        while queue:
            node, depth = queue.popleft()
            if depth >= max_depth:
                continue

            for elem in available_elements:
                for outcome in getSlammingOutcomes(node.outcome.item, elem):
                    h = hash(outcome)
                    if h in visited: 
                        visited_skip_count += 1
                        continue
                    visited.add(h)
                    child = CraftTreeNode(outcome, int((node.nodeProbability/100 * outcome.probability/100)*100),parent=node, used_elem=elem)
                    node.add_child(elem, child)

                    if outcome.item == target_item:
                        found_paths.append(child.path_from_root())
                    else:
                        queue.append((child, depth + 1))

        return TreePath(found_paths), visited_skip_count

    def __repr__(self) -> str:
        lines: List[str] = []

        def walk(node: CraftTreeNode, prefix: str = ""):
            #lines.append(f"{prefix}{node.outcome.item.name}")
            for elem, children in node.children.items():
                for i, child in enumerate(children):
                    branch = "└─" if i == len(children) - 1 else "├─"
                    full_prefix = f"{prefix}{branch}[{elem.name}]"
                    lines.append(f"{full_prefix} Path Prob. {child.nodeProbability: >2}% | Child Prob. {child.outcome.probability: >2}% {child.outcome.functionParam} {child.outcome.item.__hash__()}")# → {child.outcome.item.rarity.value} {child.outcome.item.name}")
                    next_prefix = prefix + ("   " if i == len(children) - 1 else "│  ")
                    walk(child, next_prefix)

        walk(self.root)
        return str(self.root.outcome.item.name) + '\n' + "\n".join(lines)