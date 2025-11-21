from functools import lru_cache
from Enums import ItemRarity, ItemSubtype, ItemType, ModifierType
from Modifier import Modifier

class Item:
    name: str
    type: ItemType
    substype: ItemSubtype
    rarity: ItemRarity
    modifiers: list[Modifier]
    ilevel: int

    def __init__(self, type: ItemType, substype: ItemSubtype, rarity: ItemRarity, modifiers: list[Modifier], ilevel: int) -> None:
        self.name = str(substype.value) + " ilvl" + str(ilevel)
        self.type = type
        self.substype = substype
        self.rarity = rarity
        self.modifiers = modifiers
        self.ilevel = ilevel
        self.cached_hash = None

    def __repr__(self) -> str:
        nbEquals = 25
        mods_str = f"\n"
        base_str = f"{'='*nbEquals} {self.rarity.value} {self.name} ilvl{self.ilevel} {self.substype.value} {'='*nbEquals}"
        self.modifiers.sort()
        for mod in self.modifiers:
            mods_str += f"| {mod}" + " "*(6 + len(base_str)-len(str(mod))) + "|\n"
        return base_str + mods_str + '='*len(base_str) + "\n"

    def __hash__(self) -> int:
        if self.cached_hash is None : 
            h = 0
            for x in self.modifiers:
                h ^= hash(x)
            self.cached_hash = h
        return self.cached_hash

    def __eq__(self, other) -> bool:
        if len(self.modifiers) != len(other.modifiers) : return False
        return self.__hash__() == other.__hash__()

    def __lt__(self, other) -> bool:
        return self.__repr__() < other.__repr__()

    def countModifier(self, modifierType: ModifierType):
        return sum(1 for mod in self.modifiers if mod.type == modifierType)

    def hasOpenModifier(self, modifierType: ModifierType, numberOfOpenPrefixWanted = 1):
        assert numberOfOpenPrefixWanted > 0
        numberOfPrefix = self.countModifier(modifierType)
        return (3 - numberOfPrefix) >= numberOfOpenPrefixWanted

    def addModifier(self, modifier: Modifier):
        assert self.hasOpenModifier(modifier.type)
        assert modifier not in self.modifiers
        self.modifiers.append(modifier)
        self.cached_hash = None

    def removeModifier(self, modifier: Modifier):
        assert modifier in self.modifiers
        self.modifiers.remove(modifier)
        self.cached_hash = None