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
        self.dic = None
        self.cached_hash = None

    def __repr__(self) -> str:
        color_dic = {
            ModifierType.Corrupted:Fore.LIGHTRED_EX,
            ModifierType.Enchantment:Fore.LIGHTYELLOW_EX,
            ModifierType.Implicit:Fore.LIGHTWHITE_EX,
            ModifierType.Prefix:Fore.LIGHTBLUE_EX,
            ModifierType.Suffix:Fore.LIGHTGREEN_EX
        }
        if self.type == ModifierType.Special : return ''
        tier_str = f"T{self.tier} " if self.type != ModifierType.Corrupted else ''
        return f"{color_dic[self.type]}{tier_str}{self.name}{Style.RESET_ALL}"

    def __hash__(self) -> int:
        if self.cached_hash is None :
            self.cached_hash = hash((self.name, self.tier))
        return self.cached_hash
    
    def __eq__(self, value) -> bool:
        return self.name == value.name and self.tier == value.tier

    def __lt__(self, other: "Modifier") -> bool:
        try :
            if self.dic[self.type] != self.dic[other.type]: # type: ignore
                return self.dic[self.type] > self.dic[other.type] # type: ignore
        except :
            self.dic = {
                ModifierType.Special:999,
                ModifierType.Enchantment:4,
                ModifierType.Implicit:3,
                ModifierType.Prefix:2,
                ModifierType.Suffix:1,
                ModifierType.Corrupted:0
            }
            if self.dic[self.type] != self.dic[other.type]:
                return self.dic[self.type] > self.dic[other.type]
        return self.name > other.name

MODS = [
    Modifier("X% Increased physical damage", ModifierType.Prefix, 1, [ItemSubtype.Bow], 1, 82),
    Modifier("X% Increased physical damage", ModifierType.Prefix, 2, [ItemSubtype.Bow], 10, 80),
    Modifier("Adds X to X physical damage", ModifierType.Prefix, 1, [ItemSubtype.Bow], 2, 82),
    Modifier("Adds X to X physical damage", ModifierType.Prefix, 2, [ItemSubtype.Bow], 20, 82),
    Modifier("Adds X to X fire damage", ModifierType.Prefix, 1, [ItemSubtype.Bow], 3, 82),
    Modifier("Adds X to X fire damage", ModifierType.Prefix, 2, [ItemSubtype.Bow], 30, 82),
    Modifier("Adds X to X lightning damage", ModifierType.Prefix, 1, [ItemSubtype.Bow], 5, 82),
    #Modifier("Adds X to X cold damage", ModifierType.Prefix, 1, [ItemSubtype.Bow], 10, 82),
    Modifier("+X to level of all projectile skills", ModifierType.Suffix, 1, [ItemSubtype.Bow], 1, 82),
    Modifier("+X to level of all projectile skills", ModifierType.Suffix, 2, [ItemSubtype.Bow], 5, 72),
    Modifier("+X to level of all projectile skills", ModifierType.Suffix, 3, [ItemSubtype.Bow], 25, 62),
    Modifier("+X to level of all projectile skills", ModifierType.Suffix, 4, [ItemSubtype.Bow], 50, 52),
    Modifier("+X to maximum life", ModifierType.Suffix, 1, [ItemSubtype.Ring], 10, 82),
    Modifier("+X to intelligence", ModifierType.Enchantment, 1,[ItemSubtype.Bow], 1, 0),
    Modifier("+X to strength", ModifierType.Enchantment, 1,[ItemSubtype.Bow], 1, 0),
    Modifier("+X to dexterity", ModifierType.Enchantment, 1,[ItemSubtype.Bow], 1, 0),
]

MODIFIERS : dict[str, Modifier] = {}
for mod in MODS :
    MODIFIERS[f"T{mod.tier} {mod.name}"] = mod

MODIFIERS["Corrupted"] = Modifier("Corrupted", ModifierType.Corrupted, 1, [ItemSubtype.Bow], 1, 0)
MODIFIERS["Base"] = Modifier("Base", ModifierType.Special, 1, [], 1, 0)