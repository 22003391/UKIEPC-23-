import sys

values = sys.stdin.readline().rstrip('\n').split(" ")
#print(values)

piers = int(values[0])
cards = int(values[1])
events = int(values[2])

dictionary = {}
for i in range(events):
    event = []
    event = sys.stdin.readline().rstrip('\n').split(" ")
    dictionary[event[1]].append[dictionary[event[0]]]

print(dictionary)
