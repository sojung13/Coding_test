import sys
sys.stdin = open('input.txt','r')

ans = 0
n,k = map(int,input().split())
while n != k:
    m = k // n
    if m > 2:
        n = n * m
    ans += 1
    k -= 1
print(ans)