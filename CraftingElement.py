from typing import Callable
from Enums import CraftingCondition
from Outcome import Outcome

class CraftingElement:
    name: str
    conditions: list[CraftingCondition]
    possibleOutcomes: list[Outcome]
    functionToApplyToItem: Callable
    
    def __init__(self, name: str, conditions: list[CraftingCondition], possibleOutcomes: list[Outcome], functionToApplyToItem: Callable) -> None:
        self.name = name 
        self.conditions = conditions
        self.possibleOutcomes = possibleOutcomes
        self.functionToApplyToItem = functionToApplyToItem
        
    def __repr__(self) -> str:
        return f"{self.name}\n"
        #return f"{self.name} <<{self.possibleOutcomes}>>"