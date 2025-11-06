from copy import deepcopy
from typing import Callable
from Item import Item
from Modifier import Modifier      

class PossibleItemOutcome:
    item: Item
    functionParam: Modifier|None
    probability:int

    def __init__(self, item: Item, functionParam: Modifier|None = None, probability: int = 0) -> None:
        self.item = item
        self.functionParam = functionParam
        self.probability = probability

    def __repr__(self) -> str:
        return f"<PossibleItemOutcome> {self.functionParam} {self.probability} Weight Hash : {self.item.__hash__()}\n{self.item}"

    def __hash__(self) -> int:
        return hash((self.item, self.functionParam, self.probability))

    def __eq__(self, value: object) -> bool:
        return self.__hash__() == value.__hash__()

    def __lt__(self, value) -> bool:
        return self.item < value.item
    
class PossibleCurrencyEffect:
    function: Callable
    functionParam: Modifier|None
    weight: int

    def __init__(self, function: Callable, functionParam: Modifier|None = None, weight: int = 0) -> None:
        self.function = function
        self.functionParam = functionParam
        self.weight = weight

    def __repr__(self) -> str:
        if self.functionParam is None : return "No effect"
        return f"{self.functionParam} Weight {self.weight}"
    
    def applyEffectOn(self, item: Item, probability: int) -> PossibleItemOutcome:
        return PossibleItemOutcome(self.function(deepcopy(item), self.functionParam), self.functionParam, probability)