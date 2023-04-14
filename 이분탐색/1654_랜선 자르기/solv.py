import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

k,n = map(int,input().split())
line = []
for _ in range(k):
    line.append(int(input()))
line.sort()

start, end = 1, max(line)
while start <= end:
    lines = 0
    mid = (start + end) // 2
    for i in line:
        lines += i // mid
    if lines >= n:
        start = mid + 1
    else:
        end = mid - 1
print(end)