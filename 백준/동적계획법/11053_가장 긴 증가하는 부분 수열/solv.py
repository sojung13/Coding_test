import sys
sys.stdin = open('input.txt','r')

# n = int(input())
# arr = list(map(int,input().split()))
# dp = [0 for _ in range(n)]
# dp[0] = 1

# for i in range(n):
#     for j in range(i):
#         if arr[i] > arr[j]:
#             dp[i] = max(dp[i],dp[j]+1)

# print(dp)

x = int(input())

arr = list(map(int, input().split()))

dp = [1 for i in range(x)]

for i in range(x):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))