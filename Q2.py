
import sys
n = int(input())
peoples = []


#inputs = sys.stdin.readline().strip('\n')
inputs = input()

unsorted = inputs.split(" ")


sortedlist = []

for x in unsorted:
    sortedlist.append(int(x))

sortedlist.sort()

for x in range(n):
    newlist = [] 
    newlist.append(sortedlist[-1])
    newlist.append(sortedlist[-2])
    newlist.append(sortedlist[0])

    sortedlist.remove(sortedlist)
    sortedlist.remove(-1)
    sortedlist.remove(0)    

    peoples.append(newlist)


total = 0
for x in newlist:
    total += x[1]

print(total)