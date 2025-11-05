from Enums import *
from utils import findWaysToMakeItem
from Modifier import MODIFIERS
from Currency import Currency
from Item import Item

STRICT = True
VERBOSE = True

print("POE Craft Optimizer")

bow = Item("Bow", ItemType.Weapon, ItemSubtype.Bow, ItemRarity.Normal, [], 82)

wanted_mods = [
    MODIFIERS["T1 X% Increased physical damage"],
    MODIFIERS["T1 Adds X to X lightning damage"],
    MODIFIERS["T1 Adds X to X physical damage"],
    MODIFIERS["T1 +X to level of all projectile skills"] 
]

target_item = Item("Bow", ItemType.Weapon, ItemSubtype.Bow, ItemRarity.Rare, wanted_mods, 82)

findWaysToMakeItem(bow, target_item, [Currency.AugmentationOrb.value, Currency.TransformationOrb.value, Currency.ExaltedOrb.value])