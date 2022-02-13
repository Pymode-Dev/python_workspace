# This is a program about a fantasy video game and whereby
# the inventories use in the game will be collected and add together
# using dictionary with keys and values

inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


def display_inventory(invent):
    total_items = 0
    for k, v in invent.items():
        total_items += v
        print(str(v), k)
    print('Total number of items: ', total_items)


dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', 'ruby', 'arrow', 'dagger']


def add_to_inventory(invent, added_items=None):
    if added_items is None:
        added_items = []
    for items in added_items:
        invent.setdefault(items, 0)
        invent[items] += 1


add_to_inventory(inventory, dragon_loot)
display_inventory(inventory)
