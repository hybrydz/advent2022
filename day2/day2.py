ROCK = 1
PAPER = 2
SCISSORS = 3
DEFEAT = 0
WIN = 6
DRAW = 3

with open('input_day2.txt', "r") as file:
    lines = file.readlines()

# PART 1
RPS = {'rock':['A','X'], 'paper':['B','Y'], 'scissors':['C','Z']}
# totalScore = 0
# for line in lines:
#     opponent = line.split()[0]
#     player = line.split()[1]
#     # Test Cases
#     # Player plays ROCK
#     if player in RPS['rock']:
#         #  Player Wins
#         if opponent in RPS['scissors']:
#             totalScore += WIN + ROCK
#         # Player Loses
#         elif opponent in RPS['paper']:
#             totalScore += DEFEAT + ROCK
#         else:
#             totalScore += DRAW + ROCK
#     # Player plays PAPER
#     elif player in RPS['paper']:
#         #  Player Wins
#         if opponent in RPS['rock']:
#             totalScore += WIN + PAPER
#         # Player Loses
#         elif opponent in RPS['scissors']:
#             totalScore += DEFEAT + PAPER
#         else:
#             totalScore += DRAW + PAPER
#     # Player plays SCISSORS
#     elif player in RPS['scissors']:
#         #  Player Wins
#         if opponent in RPS['paper']:
#             totalScore += WIN + SCISSORS
#         # Player Loses
#         elif opponent in RPS['rock']:
#             totalScore += DEFEAT + SCISSORS
#         else:
#             totalScore += DRAW + SCISSORS
# print(totalScore)

# PART 2
points = {'A':1, 'B':2, 'C':3}
totalScore = 0
for line in lines:
    opponent = line.split()[0]
    result = line.split()[1]
    if result == 'X':
        if opponent in RPS['rock']:
            totalScore += DEFEAT + SCISSORS
        elif opponent in RPS['paper']:
            totalScore += DEFEAT + ROCK
        else:
            totalScore += DEFEAT + PAPER  
    elif result == 'Y':
        totalScore += DRAW + points[opponent] 
    elif result == 'Z':
        if opponent in RPS['rock']:
            totalScore += WIN + PAPER
        elif opponent in RPS['paper']:
            totalScore += WIN + SCISSORS
        else:
            totalScore += WIN + ROCK     
print(totalScore)   
