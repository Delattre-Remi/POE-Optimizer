from copy import deepcopy
from CraftingElement import CraftingElement
from Item import Item
from Outcome import PossibleItemOutcome
from CraftingTree import CraftingTree, CraftTreeNode, getSlammingOutcomes

VERBOSE = False

def log(x):
    global VERBOSE
    if VERBOSE :
        print(x)

def _findWaysToMakeItem(base_item : Item, target_item : Item, available_craftingElements : list[CraftingElement], max_steps = 10):
    candidatesForNextStep : list[Item] = [deepcopy(base_item)]
    explored_items : set[int] = set()
    for step in range(max_steps + 1):
        candidates = candidatesForNextStep
        candidatesForNextStep : list[Item] = []
        print(f"{'='*50}\nStep {step} : Candidates : {len(candidates)}")
        for candidate in candidates:
            for craftElem in available_craftingElements:
                outcomes = getSlammingOutcomes(candidate, craftElem)
                if len(outcomes) == 0 : continue
                log(f"> Candidate\n{candidate}Got {len(outcomes)} outcomes with {craftElem.name}")
                explored_items.add(hash(candidate))
                for outcome in outcomes:
                    if outcome in explored_items:
                        continue
                    if outcome.item == target_item:
                        print("FOUND")
                        return 
                    candidatesForNextStep.append(deepcopy(outcome.item))

def findWaysToMakeItem(base_item : Item, target_item : Item, available_craftingElements : list[CraftingElement], max_steps = 10):
    tree = CraftingTree(base_item)
    x = tree.find_paths_to_target(target_item, available_craftingElements, max_steps)
    print(tree)
    print(x)