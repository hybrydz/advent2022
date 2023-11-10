# with open('test_input.txt', "r") as file:
#     elfInventory = file.read().rstrip().split('\n\n')

with open('input_day1.txt', "r") as file:
    elfInventory = file.read().rstrip().split('\n\n')

# #  Part 1
# totalCalories = 0
# for invetory in elfInventory:
#     sum = 0
#     for item in invetory.split():
#         sum += int(item)
#     if sum > totalCalories:
#         totalCalories = sum

# print(totalCalories)

# Part 2 
totalCalories = []
for invetory in elfInventory:
    sumCal = 0
    for item in invetory.split():
        sumCal += int(item)
    totalCalories.append(sumCal)
totalCalories.sort(reverse=True)
print(sum(totalCalories[0:3]))

