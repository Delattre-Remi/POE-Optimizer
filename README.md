# POE Craft Optimizer

A Python-based utility to explore and enumerate crafting paths in Path of Exile. 

Given a base item, a target item with desired modifiers, and a list of available currencies, this tool will build and traverse a crafting tree to find all possible ways to transform the base item into the target item within a specified depth.

## Features
- Builds a crafting tree where each node is an Item and each edge is a crafting action (using a currency).
- Supports configurable depth (max_steps) to limit search.
- Tracks visited item states to avoid infinite loops.
- Outputs all distinct paths from a base item to a target item.
- Verbose logging for step-by-step debugging (optional).