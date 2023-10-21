import sys

values = sys.stdin.readline().rstrip('\n').split(" ")

n = values[0]
t = int(values[1])

values = sys.stdin.readline().rstrip('\n').split(" ")


for x in range(len(values)):
    size = len(values)
    pointer = x
    times = 0
    for i in range(len(values)-1):
        if pointer == size:
            pointer = x
        else:
            pointer+=1
        times += int(values[pointer])

    if times<=t:
        print("0")

    else:
        print("1")

        


