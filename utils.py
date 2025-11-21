from CraftingElement import CraftingElement
from Item import Item
from CraftingTree import CraftingTree

VERBOSE = False

def log(x):
    global VERBOSE
    if VERBOSE :
        print(x)

def findWaysToMakeItem(base_item : Item, target_item : Item, available_craftingElements : list[CraftingElement], max_steps = 10):
    tree = CraftingTree(base_item)
    x, skips = tree.find_paths_to_target(target_item, available_craftingElements, max_steps)
    return tree, x, skips