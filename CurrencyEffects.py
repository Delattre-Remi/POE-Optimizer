from Item import Item, ItemRarity
from Modifier import Modifier, MODIFIERS, ModifierType

def vaalItem(item: Item, modifier: Modifier) -> Item:
    assert modifier.type == ModifierType.Enchantment
    assert item.rarity in [ItemRarity.Rare, ItemRarity.Unique]
    item.addModifier(modifier)
    item.addModifier(MODIFIERS["Corrupted"])
    return item

def transformItem(item: Item, modifier: Modifier) -> Item:
    assert modifier.type in [ModifierType.Prefix, ModifierType.Suffix]
    assert item.rarity == ItemRarity.Normal
    item.addModifier(modifier)
    item.rarity = ItemRarity.Magic
    return item

def augmentItem(item: Item, modifier: Modifier) -> Item:
    assert modifier.type in [ModifierType.Prefix, ModifierType.Suffix]
    assert item.rarity == ItemRarity.Magic
    assert len(item.modifiers) < 2
    item.addModifier(modifier)
    return item

def regalItem(item: Item, modifier: Modifier) -> Item:
    assert modifier.type in [ModifierType.Prefix, ModifierType.Suffix]
    assert item.rarity == ItemRarity.Magic
    item.addModifier(modifier)
    item.rarity = ItemRarity.Rare
    return item

def exaltItem(item: Item, modifier: Modifier) -> Item:
    assert modifier.type in [ModifierType.Prefix, ModifierType.Suffix]
    assert item.rarity == ItemRarity.Rare
    item.addModifier(modifier)
    return item

def annulItem(item: Item, modifier: Modifier) -> Item:
    item.removeModifier(modifier)
    return item