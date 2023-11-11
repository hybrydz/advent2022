with open('test_input.txt', "r") as file:
    lines = file.read().splitlines()

# with open('input_day6.txt', "r") as file:
#     lines = file.read().splitlines()

sum =0
for line in lines:
    startOfPacket = 0
    window = 4
    index =0
    while window<=len(line):
        # print(index,startOfPacket,window)
        # print(line[index],line[startOfPacket:window], line[startOfPacket:window].count(line[index]))
        if line[startOfPacket:window].count(line[index])>1:
            window +=1
            startOfPacket+=1
            index = startOfPacket
        else:
            if index == window:
                sum+=window
                print(window," ",line[startOfPacket:window])
                break
            else:
                index+=1
