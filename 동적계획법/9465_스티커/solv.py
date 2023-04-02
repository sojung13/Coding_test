import sys
sys.stdin = open('input.txt','r')

t = int(input())
for _ in range(t):
    n = int(input())
    arr = []
    dp = []
    for _ in range(2):
        arr.append(list(map(int,input().split())))
        dp.append([0 for _ in range(n)])

    # # 초기값 세팅해주기
    dp[0][0] = arr[0][0]
    dp[1][0] = arr[1][0]
    dp[0][1] = arr[0][1] + arr[1][0]
    dp[1][1] = arr[0][0] + arr[1][1]

    for j in range(2,n):
        # 돌리기
        dp[0][j] += max(dp[1][j-1] + arr[0][j],dp[1][j-2] + arr[0][j])
        dp[1][j] += max(dp[0][j-1] + arr[1][j], dp[0][j-2] + arr[1][j])
    print(max(dp[0][n-1],dp[1][n-1]))
