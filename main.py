from Enums import *
from utils import findWaysToMakeItem
from Modifier import MODIFIERS
from Currency import Currency, Omen
from Item import Item
import timeit

STRICT = True
VERBOSE = True

print("POE Craft Optimizer")

'''
=====
Tests
=====
'''



assert Item(ItemType.Weapon, ItemSubtype.Bow, ItemRarity.Normal, [MODIFIERS["T1 X% Increased physical damage"], MODIFIERS["T1 Adds X to X lightning damage"]], 82) == Item(ItemType.Weapon, ItemSubtype.Bow, ItemRarity.Normal, [MODIFIERS["T1 Adds X to X lightning damage"], MODIFIERS["T1 X% Increased physical damage"]], 82)


base_mods = [
    #MODIFIERS["T1 X% Increased physical damage"]
]

rarity = ItemRarity.Normal
if len(base_mods) in [1, 2] : rarity = ItemRarity.Magic
elif len(base_mods) > 2 : rarity = ItemRarity.Rare

bow = Item(ItemType.Weapon, ItemSubtype.Bow, rarity, base_mods, 82)

wanted_mods = [
    MODIFIERS["T1 X% Increased physical damage"],
    MODIFIERS["T1 Adds X to X lightning damage"],
    MODIFIERS["T1 Adds X to X physical damage"],
    MODIFIERS["T1 +X to level of all projectile skills"]
]

available_currencies = [
    Currency.AugmentationOrb.value, 
    Currency.TransformationOrb.value, 
    Currency.RegalOrb.value,
    Currency.ExaltedOrb.value,
    Omen.SinistralExaltation.value,
    #Currency.AnnulmentOrb.value
]

target_item = Item(ItemType.Weapon, ItemSubtype.Bow, ItemRarity.Rare, wanted_mods, 82)
nb_runs = 100
exec_time = timeit.timeit(lambda : findWaysToMakeItem(bow, target_item, available_currencies), number=nb_runs)
print(f"Building tree took {exec_time*1000:.0f}ms to run {nb_runs:.0f} times, so {(exec_time/nb_runs)*1000:.2f}ms by single run")

tree, waysToMakeItem, skips = findWaysToMakeItem(bow, target_item, available_currencies, max_steps=5)
#print(tree)
print("Skips :", skips)
# print(waysToMakeItem)