from collections import OrderedDict

# with open('test_input.txt', "r") as file:
#     lines = file.read().splitlines()

with open('input_day5.txt', "r") as file:
    lines = file.read().splitlines()
    
def rearrangement(procedure: str,stacks: dict):
    popCount = int(procedure.split(' ')[1])
    fromStack = int(procedure.split(' ')[3])
    toStack = int(procedure.split(' ')[5])
    if popCount>1:
        while popCount != 0:
            stacks[toStack].insert(0,stacks[fromStack].pop(popCount-1))
            popCount-=1
    else:
        stacks[toStack].insert(0,stacks[fromStack].pop(0))
    return stacks

stacks = {}
for line in lines:
    if not line.startswith('move') and not line == '' and not line.startswith(' 1'):
        countChar = 0
        print(line)
        sample = line.split(' ')
        for item in sample:
            countChar +=1
            if item != '':
                if ((countChar//4)+1) in stacks.keys():
                    stacks[(countChar//4)+1].append(item)
                else:
                    stacks[(countChar//4)+1] = [item]
                countChar += 3 
    elif line.startswith('move'):
        print(line)
        stacks = rearrangement(line,stacks)
        print(stacks)


topCrates = ''
stacks = OrderedDict(sorted(stacks.items()))
# print(stacks)
for key in stacks.keys():
    if len(stacks[key]):
        topCrates += stacks[key][0]

print(topCrates.replace('[','').replace(']',''))




