import sys
sys.stdin = open('input.txt','r')
import heapq

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))
arr.sort(key=lambda x:x[0])
# print(arr)

rooms = [0]
answer = 1
for s,e in arr:
    if s >= rooms[0]:
        heapq.heappop(rooms)
    else:
        answer += 1
    heapq.heappush(rooms,e)
print(answer)