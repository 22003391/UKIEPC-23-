import sys

wordConv = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "point"]

array = []
n = int(input())
for i in range(n):
    array.append(sys.stdin.readline().rstrip('\n'))
    
for i in range(n):
    input=array[i].strip("L")

    #get rid of the L
    input = float(input)
    if input == int(input):
        input = int(input)

    values = str(input)

    for i in range(len(values)):
        if values[i] == ".":
            print(wordConv[10], end="")
        else:
            print(wordConv[int(values[i])], end="")
    print("")

