import sys
sys.stdin = open('input.txt','r')

n,m = map(int,input().split())
rate = [input().split() for _ in range(n)]

def bs(rate, cnt):
    s, e = 0, len(rate)-1
    res = 0
    while s <= e:
        mid = (s + e) // 2
        if int(rate[mid][1]) >= cnt:
            e = mid - 1
            s = mid
        else:
            s = mid + 1
    return res
 ㅇ
for i in range(m):
    cnt = int(input())
    print(bs(rate,cnt))