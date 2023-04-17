import heapq
import sys
sys.stdin = open('input.txt','r')

n = int(input())
arr = []
answer = 1

for _ in range(n):
    arr.append(list(map(int,input().split())))
arr.sort(key=lambda x:x[0])

rooms = [0]
for i in range(n):
    if arr[i][0] >= rooms[0]:
        heapq.heappop(rooms)
    else:
        answer += 1
    heapq.heappush(rooms, arr[i][1])
print(answer)