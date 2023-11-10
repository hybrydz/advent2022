# with open('test_input.txt', "r") as file:
#     elfInventory = file.read().rstrip().split('\n\n')

with open('input_day1.txt', "r") as file:
    elfInventory = file.read().rstrip().split('\n\n')

totalCalories = []
for invetory in elfInventory:
    sumCal = 0
    for item in invetory.split():
        sumCal += int(item)
    totalCalories.append(sumCal)
totalCalories.sort(reverse=True)

## Part 1
print(totalCalories[0])

## Part 2
print(sum(totalCalories[0:3]))

