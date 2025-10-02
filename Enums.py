
from enum import Enum

class ModifierType(Enum):
    Prefix = "Prefix"
    Suffix = "Suffix"
    Implicit = "Implicit"
    Enchantment = "Enchantment"
    
class ItemType(Enum):
    Weapon = "Weapon"
    Armor = "Armor"
    Accessory = "Accessory"

class ItemSubtype(Enum):
    Bow = "Bow"
    
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