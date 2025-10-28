from Enums import ItemRarity
from Item import Item
from Modifier import Modifier, MODIFIERS

def vaalItem(item:Item, modifier:Modifier) -> Item:
    item.addModifier(modifier)
    item.addModifier(MODIFIERS["Corrupted"])
    return item

def transformItem(item:Item, modifier:Modifier) -> Item:
    item.addModifier(modifier)
    item.rarity = ItemRarity.Magic
    return item

def augmentItem(item:Item, modifier:Modifier) -> Item:
    item.addModifier(modifier)
    item.rarity = ItemRarity.Rare
    return item

def exaltItem(item:Item, modifier:Modifier) -> Item:
    item.addModifier(modifier)
    return item