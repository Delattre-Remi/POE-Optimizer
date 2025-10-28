from copy import deepcopy
from CraftingElement import CraftingElement
from Item import Item
from Outcome import PossibleItemOutcome
from Currency import Currency
from Modifier import MODIFIERS

VERBOSE = True

def log(x):
    global VERBOSE
    if VERBOSE :
        print(x)

def getSlammingOutcomes(item : Item, craftingElem: CraftingElement) -> list[PossibleItemOutcome]:
    assert all(item.satisfies(cond) for cond in craftingElem.conditions), f"When slamming {craftingElem} on {item}, some conditions are not satisfied"

    for mod in item.modifiers:
        if mod.name == "Corrupted" :
            return [PossibleItemOutcome(item, 1)]

    outcomes : set[PossibleItemOutcome] = set()
    for outcome in craftingElem.possibleOutcomes:
        for modifier in outcome.addedModifiers:
            if item.hasOpenModifier(modifier.type) and item.substype in modifier.applicableItems and modifier not in item.modifiers:
                outcomes.add(PossibleItemOutcome(craftingElem.functionToApplyToItem(deepcopy(item), modifier), modifier.weight))
            elif VERBOSE :
                log(f"Skipped Outcome {modifier}")
                continue
    return list(outcomes)