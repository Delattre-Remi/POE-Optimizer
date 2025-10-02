from enum import Enum
from CraftingElement import CraftingElement
from Enums import CraftingCondition
from Modifier import MODIFIERS
from Outcome import Outcome


exaltedOrbOutcomes = []
for mod in MODIFIERS.values():
    exaltedOrbOutcomes.append(Outcome([mod], mod.weight))

class Currency(Enum):
    ExaltedOrb = CraftingElement("ExaltedOrb", [CraftingCondition.isRare, CraftingCondition.hasOpenAffix], exaltedOrbOutcomes)