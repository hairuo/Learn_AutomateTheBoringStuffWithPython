
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

# def ItemTotal(inventory):
#     item_total = 0
#     for k in inventory.keys():
#         item_total = item_total + inventory.get(k, 0)
#     return item_total
#
# print('Inventory')
#
# for k, v in stuff.items():
#     print(str(v) + ' ' + k)
#
# print('Total number of items: ' + str(ItemTotal(stuff)))

def displayInventory(inventory):
    print('Inventory:')
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v
    print('Total number of items: ' + str(item_total))

displayInventory(stuff)