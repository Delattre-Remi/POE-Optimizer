
from enum import Enum

class ModifierType(Enum):
    Corrupted = "Corrupted"
    Prefix = "Prefix"
    Suffix = "Suffix"
    Implicit = "Implicit"
    Enchantment = "Enchantment"
    Special = "Special"

class ItemType(Enum):
    Weapon = "Weapon"
    Armor = "Armor"
    Accessory = "Accessory"

class ItemSubtype(Enum):
    Bow = "Bow"
    Ring = "Ring"

class ItemRarity(Enum):
    Normal = "Normal"
    Magic = "Magic"
    Rare = "Rare"
    Unique = "Unique"

class CraftingCondition(Enum):
    hasOpenPrefix = "hasOpenPrefix"
    hasOpenSuffix = "hasOpenSuffix"
    hasOpenAffix = "hasOpenAffix"
    isNormal = "isNormal"
    isMagic = "isMagic"
    isRare = "isRare"
    isNotEnchanted = "isNotEnchanted"