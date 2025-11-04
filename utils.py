from copy import deepcopy
from CraftingElement import CraftingElement
from Item import Item
from Outcome import PossibleItemOutcome

VERBOSE = False

def log(x):
    global VERBOSE
    if VERBOSE :
        print(x)

def getSlammingOutcomes(item : Item, craftingElem: CraftingElement) -> list[PossibleItemOutcome]:
    if not all(item.satisfies(cond) for cond in craftingElem.conditions):
        log(f"When slamming {craftingElem} on {item}, some conditions are not satisfied")
        return []

    outcomes : set[PossibleItemOutcome] = set()
    for outcome in craftingElem.possibleOutcomes:
        for modifier in outcome.addedModifiers:
            if item.hasOpenModifier(modifier.type) and item.substype in modifier.applicableItems and modifier not in item.modifiers:
                outcomes.add(PossibleItemOutcome(craftingElem.functionToApplyToItem(deepcopy(item), modifier), modifier.weight))
            elif VERBOSE :
                log(f"Skipped Outcome {modifier}")
                continue
    return list(outcomes)

def findWaysToMakeItem(base_item : Item, target_item : Item, available_craftingElements : list[CraftingElement], max_steps = 10):
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
