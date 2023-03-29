import sys
sys.stdin = open('input.txt','r')

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))
arr.sort(key=lambda x:x[1])
answer = end = 0
for s,e in arr:
    if s >= end:
        answer += 1
        end = e
print(answer)
