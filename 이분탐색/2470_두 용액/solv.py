import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

n = int(input())
water = list(map(int,input().split()))
water.sort()

start, end = 0, n-1
ans = abs(water[start] + water[end])
final = [water[start] ,water[end]]
while start < end:
    left = water[start]
    right = water[end]
    sum = left + right
    if abs(sum) < ans:
        ans = abs(sum)
        final = [left, right]
        if ans == 0:
            break
    if sum < 0:
        start += 1
    else:
        end -= 1
print(final[0], final[1])
