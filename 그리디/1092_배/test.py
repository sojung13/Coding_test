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
# 박스 배로 못옮기는 경우
if cranes[0] < boxes[0]:
    answer = -1

while boxes:
    for crane in cranes:
        for box in boxes:
            if crane >= box:
                boxes.remove(box)
                break
    answer += 1

print(answer)