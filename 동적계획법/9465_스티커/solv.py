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
    print(arr)
    print(dp)