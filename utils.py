 
from CraftingElement import CraftingElement
from Item import Item
from Outcome import PossibleItemOutcome

VERBOSE = True

def getSlammingOutcomes(item : Item, craftingElem: CraftingElement) -> list[PossibleItemOutcome]:
    assert all(item.satisfies(cond) for cond in craftingElem.conditions), f"When slamming {craftingElem} on {item}, some conditions are not satisfied"
    
    outcomes : set[PossibleItemOutcome] = set()
    for outcome in craftingElem.possibleOutcomes:
        for modifier in outcome.addedModifiers:
            if item.hasOpenModifier(modifier.type) and modifier not in item.modifiers:
                newItem = Item(
                    name=item.name,
                    type=item.type,
                    substype=item.substype,
                    rarity=item.rarity,
                    modifiers=item.modifiers,
                    ilevel=item.ilevel
                )
                newItem.addModifier(modifier)
                outcomes.add(PossibleItemOutcome(newItem, modifier.weight))
            elif VERBOSE :
                print(f"Item > getSlammingOutcomes > Skipped Outcome {modifier}")
    return list(outcomes)