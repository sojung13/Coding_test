import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

n,m = map(int,input().split())
tree = list(map(int,input().split()))
tree.sort()

start, end = 1, max(tree)

while start <= end:
    mid = (start + end) // 2
    rest = 0
    for i in tree:
        if i > mid:
            rest += (i-mid)
    if rest >= m:
        start = mid + 1
    else:
        end = mid - 1
print(end)