import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

n,c = map(int,input().split())
house = [int(input()) for _ in range(n)]
house.sort()

start, end = 0, house[-1]
result = []
while start <= end:
    mid = (start + end) // 2
    count = 1
    current = house[0]
    for i in house:
        if current + mid <= i:
            count += 1
            current = i
    if count >= c:
        start = mid + 1
        result.append(mid)
    else:
        end = mid - 1
print(max(result))
