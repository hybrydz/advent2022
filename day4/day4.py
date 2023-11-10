
# with open('test_input.txt', "r") as file:
#     elfPair = file.read().rstrip().splitlines()

with open('input_day4.txt', "r") as file:
    elfPair = file.read().rstrip().splitlines()

count = 0  #Part 1
overlap = 0 #Part 2
for pair in elfPair:
    firstPair = pair.split(',')[0].split('-')
    secondPair = pair.split(',')[1].split('-')
    #  Test Cases
    if (firstPair == secondPair):
        count += 1
        overlap += 1 
    elif (int(firstPair[0])<= int(secondPair[0])) and (int(firstPair[1])>= int(secondPair[1])):
        count += 1
        overlap += 1 
    elif (int(secondPair[0])<= int(firstPair[0])) and (int(secondPair[1])>= int(firstPair[1])) :
        count += 1
        overlap += 1   
    # Part2
    else:
        if int(secondPair[0]) <= int(firstPair[0]) <= int(secondPair[1]):
            overlap += 1
        elif int(secondPair[0]) <= int(firstPair[1]) <= int(secondPair[1]):
            overlap += 1

print(count)
print(overlap)