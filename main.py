from Enums import *
from Modifier import MODIFIERS
from Currency import Currency
from utils import getSlammingOutcomes
from Item import Item

STRICT = True
VERBOSE = True

bow = Item("Bow", ItemType.Weapon, ItemSubtype.Bow, ItemRarity.Rare, [MODIFIERS["physDmgPercent"]], 82)

print(getSlammingOutcomes(bow, Currency.ExaltedOrb.value))