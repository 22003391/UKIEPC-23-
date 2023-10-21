import sys

player1 = sys.stdin.readline().rstrip('\n').split(" ")
player2 = sys.stdin.readline().rstrip('\n').split(" ")

for x in range(len(player1)):
    player1[x] = int(player1[x])
    player2[x] = int(player2[x])

value1=(player2[0]/player1[1])
if value1==int(value1):
    value1-=1
timeToKill1=int(value1) * player1[2]
value2=(player1[0]/player2[1])
if value2==int(value2):
    value2-=1
timeToKill2=int(value2) * player2[2]

if timeToKill1+0.5<timeToKill2:
    print("player one")
elif timeToKill2+0.5<timeToKill1:
    print("player two")
else:
    print("draw")
