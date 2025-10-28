from Item import Item
from Modifier import Modifier

class Outcome:
    addedModifiers: list[Modifier]
    weight: int
    
    def __init__(self, addedModifiers: list[Modifier], weight: int) -> None:
        self.addedModifiers = addedModifiers
        self.weight = weight
        
    def __repr__(self) -> str:
        return f"Weight {self.weight} for {self.addedModifiers}"

class PossibleItemOutcome:
    item: Item
    weight:int
    
    def __init__(self, item: Item, weight: int) -> None:
        self.item = item
        self.weight = weight
        
    def __repr__(self) -> str:
        return f"<PossibleItemOutcome> {self.weight} Weight Hash : {self.item.__hash__()}\n{self.item}"

    def __hash__(self) -> int:
        return self.item.__hash__()

    def __eq__(self, value: object) -> bool:
        return self.__hash__() == value.__hash__()
    
    def __lt__(self, value) -> bool:
        return self.item < value.item