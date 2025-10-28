from Enums import CraftingCondition, ItemRarity, ItemSubtype, ItemType, ModifierType
from Modifier import Modifier

class Item:
    name: str
    type: ItemType
    substype: ItemSubtype
    rarity: ItemRarity
    modifiers: list[Modifier]
    ilevel: int
    
    def __init__(self, name: str, type: ItemType, substype: ItemSubtype, rarity: ItemRarity, modifiers: list[Modifier], ilevel: int) -> None:
        self.name = name
        self.type = type
        self.substype = substype
        self.rarity = rarity
        self.modifiers = modifiers
        self.ilevel = ilevel
        
    def __repr__(self) -> str:
        nbEquals = 25
        mods_str = f"\n"
        base_str = f"{'='*nbEquals} {self.rarity.value} {self.name} ilvl{self.ilevel} {self.substype.value} {'='*nbEquals}"
        for mod in self.modifiers:
            mods_str += f"| {mod}" + " "*(6 + len(base_str)-len(str(mod))) + "|\n"
        return base_str + mods_str + '='*len(base_str) + "\n"
    
    def __hash__(self):
        return hash((
            self.name,
            self.type,
            self.substype,
            self.rarity,
            tuple(self.modifiers),
            self.ilevel
        ))
    
    def __eq__(self, other) -> bool:
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
        self.modifiers.sort()
        
    def satisfies(self, condition : CraftingCondition):
        match condition:
            case CraftingCondition.hasOpenPrefix:
                return self.hasOpenModifier(ModifierType.Prefix)
            case CraftingCondition.hasOpenSuffix:
                return self.hasOpenModifier(ModifierType.Suffix)
            case CraftingCondition.hasOpenAffix:
                return self.hasOpenModifier(ModifierType.Prefix) or self.hasOpenModifier(ModifierType.Suffix)
            case CraftingCondition.isNormal:
                return self.rarity == ItemRarity.Normal
            case CraftingCondition.isMagic:
                return self.rarity == ItemRarity.Magic
            case CraftingCondition.isRare:
                return self.rarity == ItemRarity.Rare
            case CraftingCondition.isNotEnchanted:
                for mod in self.modifiers:
                    if mod.type == ModifierType.Enchantment:
                        return False
                return True 
            case _:
                exit(404)