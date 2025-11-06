from Enums import CraftingCondition
from Outcome import PossibleCurrencyEffect
from Item import Item
from Modifier import Modifier

class CraftingElement:
    name: str
    conditions: list[CraftingCondition]
    possibleCurrencyEffects: list[PossibleCurrencyEffect]
    
    def __init__(self, name: str, conditions: list[CraftingCondition], possibleCurrencyEffects: list[PossibleCurrencyEffect]) -> None:
        self.name = name 
        self.conditions = conditions
        self.possibleCurrencyEffects = possibleCurrencyEffects

    def getPossibleCurrencyEffectsFor(self, item: Item) -> list[PossibleCurrencyEffect]:
        possibleCurrencyEffects : list[PossibleCurrencyEffect] = []
        
        # Element needs to know the item state to have an effect
        if len(self.possibleCurrencyEffects) == 1 and self.possibleCurrencyEffects[0].functionParam == None : 
            currentPossibleCurrencyEffect = self.possibleCurrencyEffects[0]
            for modifier in item.modifiers:
                possibleCurrencyEffects.append(PossibleCurrencyEffect(currentPossibleCurrencyEffect.function, modifier, 1))
        else: # Element doesnt need to know the item state, but its mods have conditions
            for currentEffect in self.possibleCurrencyEffects:
                if not currentEffect : continue
                currentEffectModifier: Modifier = currentEffect.functionParam # type: ignore
                if  currentEffectModifier is not None \
                and currentEffectModifier not in item.modifiers \
                and item.substype in currentEffectModifier.applicableItems \
                and item.ilevel >= currentEffectModifier.ilevel_requirement \
                and item.hasOpenModifier(currentEffectModifier.type):
                    possibleCurrencyEffects.append(currentEffect)
        return possibleCurrencyEffects
        
    
    def __hash__(self) -> int:
        return hash(self.__repr__())
        
    def __repr__(self) -> str:
        return f"{self.name}"
        #return f"{self.name} <<{self.possibleOutcomes}>>"