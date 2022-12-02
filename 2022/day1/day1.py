import numpy as np

inventory = []
# Read puzzle_input_day1.txt file into data object
with open("puzzle_input_day1.txt", "r") as file:
    data = file.read().split("\n")

temp_inventory = []
max_calories = 0
# While there is no empty line add data to temp_inventory list.
# When empty row is found, the sum of the items before is calculated.
# If the sum is the largest, the max_calories is updated
for item in data:
    if item:
        temp_inventory.append(int(item))
    else:
        item_sum_calories = np.sum(temp_inventory)
        temp_inventory = []
        if item_sum_calories > max_calories:
            max_calories = item_sum_calories

print(max_calories)  # 66487
