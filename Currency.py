from enum import Enum
from CraftingElement import CraftingElement
from Enums import CraftingCondition, ModifierType
from Modifier import MODIFIERS
from Outcome import Outcome
from CurrencyEffects import vaalItem, transformItem, augmentItem, exaltItem

exaltedOrbOutcomes = []
vallOrbOutcomes = []
for mod in MODIFIERS.values():
    if mod.type in [ModifierType.Prefix, ModifierType.Suffix]:
        exaltedOrbOutcomes.append(Outcome([mod], mod.weight))
    if mod.type == ModifierType.Enchantment:
        vallOrbOutcomes.append(Outcome([mod], mod.weight))

class Currency(Enum):
    TransformationOrb = CraftingElement("TransformationOrb", [CraftingCondition.isNormal, CraftingCondition.hasOpenAffix], exaltedOrbOutcomes, transformItem)
    AugmentationOrb = CraftingElement("TransformationOrb", [CraftingCondition.isMagic, CraftingCondition.hasOpenAffix], exaltedOrbOutcomes, augmentItem)
    ExaltedOrb = CraftingElement("ExaltedOrb", [CraftingCondition.isRare, CraftingCondition.hasOpenAffix], exaltedOrbOutcomes, exaltItem)
    VaalOrb = CraftingElement("VaalOrb", [CraftingCondition.isRare, CraftingCondition.isNotEnchanted], vallOrbOutcomes, vaalItem)