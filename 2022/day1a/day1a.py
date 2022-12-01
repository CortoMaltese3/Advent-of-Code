import numpy as np

inventory = []
with open("inventory.txt", "r") as file:
    data = file.read().split("\n")
    temp_inventory = []
    for item in data:
        if item:
            temp_inventory.append(int(item))
        else:
            inventory.append(temp_inventory)
            temp_inventory = []


max_calories = 0
for item in inventory:
    item_sum = np.sum(item)
    if item_sum > max_calories:
        max_calories = item_sum

print(max_calories)
