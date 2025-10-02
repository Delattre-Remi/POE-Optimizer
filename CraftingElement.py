from Enums import CraftingCondition
from Outcome import Outcome

class CraftingElement:
    name: str
    conditions: list[CraftingCondition]
    possibleOutcomes: list[Outcome]
    
    def __init__(self, name: str, conditions: list[CraftingCondition], possibleOutcomes: list[Outcome]) -> None:
        self.name = name 
        self.conditions = conditions
        self.possibleOutcomes = possibleOutcomes
        
    def __repr__(self) -> str:
        return f"{self.name} <<{self.possibleOutcomes}>>"