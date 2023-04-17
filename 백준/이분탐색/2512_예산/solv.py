import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

n = int(input())
money = list(map(int,input().split()))
m = int(input())
start, end = 0, max(money)

while start <= end:
    mid = (start + end) // 2
    total = 0
    for i in money:   # 120 110 140 150
        if i > mid:
            total += mid
        else:
            total += i
    if total <= m:
        start = mid + 1
    else:
        end = mid - 1
print(end)