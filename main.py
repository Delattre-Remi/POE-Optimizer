from Enums import *
from utils import findWaysToMakeItem
from Modifier import MODIFIERS
from Currency import Currency
from Item import Item
import timeit

STRICT = True
VERBOSE = True

print("POE Craft Optimizer")

bow = Item("Normal Bow ilvl 82", ItemType.Weapon, ItemSubtype.Bow, ItemRarity.Normal, [], 82)

wanted_mods = [
    MODIFIERS["T1 X% Increased physical damage"],
    MODIFIERS["T1 Adds X to X lightning damage"],
    MODIFIERS["T1 Adds X to X physical damage"],
    MODIFIERS["T1 +X to level of all projectile skills"] 
]

available_currencies = [
    Currency.AugmentationOrb.value, 
    Currency.TransformationOrb.value, 
    Currency.ExaltedOrb.value,
    Currency.AnnulmentOrb.value
]

target_item = Item("Normal Bow ilvl 82", ItemType.Weapon, ItemSubtype.Bow, ItemRarity.Rare, wanted_mods, 82)
# nb_runs = 10000
# exec_time = timeit.timeit(lambda : findWaysToMakeItem(bow, target_item, available_currencies), number=nb_runs)
# print(f"Building tree took {exec_time*1000:.0f}ms to run {nb_runs:.0f} times, so {(exec_time/nb_runs)*1000:.2f}ms by single run")

tree, waysToMakeItem = findWaysToMakeItem(bow, target_item, available_currencies, max_steps=2)
print(tree)