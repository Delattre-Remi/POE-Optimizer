from enum import Enum
from CraftingElement import CraftingElement, CraftingCondition
from Modifier import MODIFIERS, ModifierType
from Outcome import PossibleCurrencyEffect
from CurrencyEffects import vaalItem, transformItem, augmentItem, regalItem, exaltItem, annulItem

transformOutcomes = []
augmentOutcomes = []
regalOutcomes= []
exaltedOrbOutcomes = []
sinistralOutcomes = []
vallOrbOutcomes = []
for mod in MODIFIERS.values():
    if mod.type == ModifierType.Prefix:
        sinistralOutcomes.append(PossibleCurrencyEffect(exaltItem, mod, mod.weight))
    if mod.type in [ModifierType.Prefix, ModifierType.Suffix]:
        transformOutcomes.append(PossibleCurrencyEffect(transformItem, mod, mod.weight))
        augmentOutcomes.append(PossibleCurrencyEffect(augmentItem, mod, mod.weight))
        regalOutcomes.append(PossibleCurrencyEffect(regalItem, mod, mod.weight))
        exaltedOrbOutcomes.append(PossibleCurrencyEffect(exaltItem, mod, mod.weight))
    if mod.type == ModifierType.Enchantment:
        vallOrbOutcomes.append(PossibleCurrencyEffect(vaalItem, mod, mod.weight))

class Currency(Enum):
    BaseItem = CraftingElement("BaseItem", [], [PossibleCurrencyEffect(lambda x: x)])
    TransformationOrb = CraftingElement("TransformationOrb", [CraftingCondition.isNormal], transformOutcomes)
    AugmentationOrb = CraftingElement("AugmentationOrb", [CraftingCondition.isMagic, CraftingCondition.hasLessThanTwoAffixes], augmentOutcomes)
    RegalOrb = CraftingElement("RegalOrb", [CraftingCondition.isMagic, CraftingCondition.hasTwoAffixes], regalOutcomes)
    ExaltedOrb = CraftingElement("ExaltedOrb", [CraftingCondition.isRare, CraftingCondition.hasOpenAffix], exaltedOrbOutcomes)
    VaalOrb = CraftingElement("VaalOrb", [CraftingCondition.isRare, CraftingCondition.isNotEnchanted], vallOrbOutcomes)
    AnnulmentOrb = CraftingElement("AnnulmentOrb", [CraftingCondition.isMagic], [PossibleCurrencyEffect(annulItem)])
    
class Omen(Enum):
    SinistralExaltation = CraftingElement("Omens Of Sinistral Exaltation", [CraftingCondition.isRare, CraftingCondition.hasOpenPrefix], sinistralOutcomes)