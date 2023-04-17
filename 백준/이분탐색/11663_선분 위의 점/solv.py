import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

n,m = map(int,input().split())
data = list(map(int,input().split()))
data.sort()

def bs(target, dir):
    start, end = 0, n-1
    while start <= end:
        mid = (start + end) // 2
        if data[mid] == target:
            return mid
        if data[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    if dir == 0:
        return start
    else:
        return end

for _ in range(m):
    s,e = map(int,input().split())
    l,r = bs(s,0), bs(e,1)
    print(r-l+1)