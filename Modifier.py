from Enums import ItemSubtype, ModifierType
from colorama import Fore, Back, Style

class Modifier:
    name: str
    type: ModifierType
    tier: int
    applicableItems: list[ItemSubtype]
    weight: int
    ilevel_requirement: int
    
    def __init__(self, name, _type, tier, applicableItems, weight, ilevel_requirement) -> None:
        self.name = name
        self.type = _type
        self.tier = tier
        self.applicableItems = applicableItems
        self.weight = weight
        self.ilevel_requirement = ilevel_requirement
        
    def __repr__(self) -> str:
        color_dic = {
            ModifierType.Enchantment:Fore.LIGHTRED_EX,
            ModifierType.Implicit:Fore.LIGHTWHITE_EX, 
            ModifierType.Prefix:Fore.LIGHTBLUE_EX, 
            ModifierType.Suffix:Fore.LIGHTGREEN_EX
        }
        return f"{color_dic[self.type]}{self.type.value} T{self.tier} {self.name}{Style.RESET_ALL}"
    
    def __hash__(self) -> int:
        return self.name.__hash__() + self.tier + self.type.value.__hash__()
    
    def __eq__(self, value: object) -> bool:
        return self.__hash__() == value.__hash__()
    
    def __lt__(self, other: "Modifier") -> bool:
        dic = {
            ModifierType.Enchantment:1,
            ModifierType.Implicit:2, 
            ModifierType.Prefix:3, 
            ModifierType.Suffix:4
        }
        return dic[self.type] > dic[other.type]
        

MODIFIERS = {
    "physDmgPercent" : Modifier("physDmgPercent", ModifierType.Prefix, 1, [ItemSubtype.Bow], 1, 82),
    "physDmgFlat"    : Modifier("physDmgFlat", ModifierType.Suffix, 1, [ItemSubtype.Bow], 10, 82)
}