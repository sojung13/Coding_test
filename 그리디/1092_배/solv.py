import sys
sys.stdin = open('input.txt','r')
input= sys.stdin.readline

n = int(input())
cranes = list(map(int,input().split()))
m = int(input())
boxes = list(map(int,input().split()))

cranes.sort(reverse=True)
boxes.sort(reverse=True)

answer = 0
if max(boxes) > max(cranes):
    answer = -1
else:
    while len(boxes) > 0:
        answer += 1
        for crane in cranes:
            for box in boxes:
                if crane >= box:
                    boxes.pop()
                    break
print(answer)