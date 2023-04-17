import sys
sys.stdin = open('input.txt','r')
import heapq
input = sys.stdin.readline

n = int(input())
arr = []
answer = 1

for _ in range(n):
    arr.append(list(map(int,input().split())))
arr.sort(key=lambda x:x[0])

heap = []

heapq.heappush(heap, arr[0][1])
for i in range(1,n):
    if heap[0] > arr[i][0]:
        heapq.heappush(heap, arr[i][1])
    else:
        heapq.heappop(heap)
        heapq.heappush(heap, arr[i][1])
print(len(heap))