from Item import Item
from CraftingElement import CraftingElement
from Outcome import PossibleItemOutcome
from Modifier import MODIFIERS

from copy import deepcopy
from collections import deque
from typing import Any, Dict, List, Optional, Set, Tuple

def getSlammingOutcomes(item : Item, craftingElem: CraftingElement) -> list[PossibleItemOutcome]:
    if not all(item.satisfies(cond) for cond in craftingElem.conditions):
        #print(f"When slamming {craftingElem} on {item}, some conditions are not satisfied")
        return []

    outcomes : set[PossibleItemOutcome] = set()
    for outcome in craftingElem.possibleOutcomes:
        for modifier in outcome.addedModifiers:
            if item.hasOpenModifier(modifier.type) and item.substype in modifier.applicableItems and modifier not in item.modifiers:
                outcomes.add(PossibleItemOutcome(craftingElem.functionToApplyToItem(deepcopy(item), modifier), modifier,modifier.weight))
    return list(outcomes)

class CraftTreeNode:
    def __init__(self, outcome: PossibleItemOutcome, parent: Optional["CraftTreeNode"] = None, used_elem: Optional[CraftingElement] = None):
        self.outcome = outcome
        self.parent = parent
        self.used_elem = used_elem
        self.children: Dict[CraftingElement, List["CraftTreeNode"]] = {}

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
                lines.append(f"Using {step[0].name} weighs {step[1].weight}, and gives")
                lines.append(str(step[1].item))
        return "\n".join(lines)

class CraftingTree:
    def __init__(self, root_item: Item):
        self.root = CraftTreeNode(PossibleItemOutcome(root_item))

    def find_paths_to_target(self,target_item: Item,available_elements: List[CraftingElement],max_depth: int = 10) -> TreePath:
        found_paths = []
        visited: Set[int] = set()

        # BFS queue: (node, current_depth)
        queue = deque([(self.root, 0)])
        visited.add(hash(self.root.outcome))

        while queue:
            node, depth = queue.popleft()
            if depth >= max_depth:
                continue

            for elem in available_elements:
                for outcome in getSlammingOutcomes(node.outcome.item, elem):
                    outcome = outcome
                    h = hash(outcome)
                    if h in visited: continue
                    visited.add(h)
                    child = CraftTreeNode(outcome, parent=node, used_elem=elem)
                    node.add_child(elem, child)

                    if outcome.item == target_item:
                        found_paths.append(child.path_from_root())
                    else:
                        queue.append((child, depth + 1))

        return TreePath(found_paths)

    def __repr__(self) -> str:
        lines: List[str] = []

        def walk(node: CraftTreeNode, prefix: str = ""):
            #lines.append(f"{prefix}{node.outcome.item.name}")
            for elem, children in node.children.items():
                for i, child in enumerate(children):
                    branch = "└─" if i == len(children) - 1 else "├─"
                    lines.append(f"{prefix}{branch}[{elem.name}] {child.outcome.addedModifier} → {child.outcome.item.rarity.value} {child.outcome.item.name}")
                    next_prefix = prefix + ("   " if i == len(children) - 1 else "│  ")
                    walk(child, next_prefix)

        walk(self.root)
        return "\n".join(lines)