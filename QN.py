import sys
n = int(input())
peoples = []


inputs = sys.stdin.readline().strip('\n')

sortedList = inputs.split(" ")

intlist = []
for x in sortedList:
    intlist.append(int(x))

intlist.sort()

diver = n//3
total = 0

for x in range(diver, len(intlist), 2):
    total += intlist[x]

print(total)