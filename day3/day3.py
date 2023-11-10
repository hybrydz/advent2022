# with open('test_input.txt', "r") as file:
#     elfPair = file.read().rstrip().splitlines()

with open('input_day3.txt', "r") as file:
    rucksacks = file.read().rstrip().splitlines()

sum = 0
Priority = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26,'A': 27, 'B': 28, 'C': 29, 'D': 30, 'E': 31, 'F': 32, 'G': 33, 'H': 34, 'I': 35, 'J': 36, 'K': 37, 'L': 38, 'M': 39, 'N': 40, 'O': 41, 'P': 42, 'Q': 43, 'R': 44, 'S': 45, 'T': 46, 'U': 47, 'V': 48, 'W': 49, 'X': 50, 'Y': 51, 'Z': 52}
# PART 1
for rucksack in rucksacks:
    compartment1 = rucksack[0:(len(rucksack)//2)]
    for item in compartment1:
        if item in rucksack[(len(rucksack)//2):]:
            sum += Priority[item]
            break
print(sum)


# PART 2
index =0
sum =0
while index<len(rucksacks):
    for item in rucksacks[index]:
        if item in rucksacks[index+1] and item in rucksacks[index+2]  :
            print(item)
            sum += Priority[item]
            break
    index += 3
print(sum)


# from string import ascii_lowercase
# print({v:k+1 for k,v in enumerate(ascii_lowercase)})

# from string import ascii_uppercase
# print({v:k+27 for k,v in enumerate(ascii_uppercase)})