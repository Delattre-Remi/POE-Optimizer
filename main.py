from Enums import *
from Modifier import MODIFIERS
from Currency import Currency
from utils import getSlammingOutcomes
from Item import Item

STRICT = True
VERBOSE = True

bow = Item("Bow", ItemType.Weapon, ItemSubtype.Bow, ItemRarity.Rare, [MODIFIERS["T1 X% Increased physical damage"]], 82)

outcomesAfter1Exalt = getSlammingOutcomes(bow, Currency.ExaltedOrb.value)

outcomesAfter2Exalts = set()

for outcome in outcomesAfter1Exalt:
    outcomes = getSlammingOutcomes(outcome.item, Currency.ExaltedOrb.value)
    for oc in outcomes:
        outcomesAfter2Exalts.add(oc)
    
outcomesAfter3Exalts = set()
for outcome in list(outcomesAfter2Exalts):
    outcomes = getSlammingOutcomes(outcome.item, Currency.ExaltedOrb.value)
    for oc in outcomes:
        outcomesAfter3Exalts.add(oc)   

outcomesAfterVaal = set()
for outcome in list(outcomesAfter3Exalts):
    outcomes = getSlammingOutcomes(outcome.item, Currency.VaalOrb.value)
    for oc in outcomes:
        outcomesAfterVaal.add(oc)  

print(sorted(list(outcomesAfterVaal)))
print(len(outcomesAfterVaal))