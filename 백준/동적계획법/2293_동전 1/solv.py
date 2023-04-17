import sys
sys.stdin = open('input.txt','r')

n,k = map(int,input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))
dp =[0 for _ in range(k+1)]
dp[0] = 1

for i in arr:   # 1,2,5
    for j in range(i, k+1):
        a = dp[j-i]
        dp[j] += a
print(dp[k])