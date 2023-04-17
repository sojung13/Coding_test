import sys
sys.stdin = open('./input.txt','r')

n = int(input())
arr = list(map(int,input().split()))
dp = [1 for _ in range(n)]

for i in range(1,n): 
    for j in range(i):
        # 만약에 뒷 숫자가 앞 숫자보다 작으면
        if arr[i] < arr[j]:
            dp[i] = max(dp[i],dp[j]+1)
        # 만약에 앞 숫자가 더 작으면 감소 수열이 안된다
        # else:
        #     dp[i] = max(dp[i],)
print(max(dp))