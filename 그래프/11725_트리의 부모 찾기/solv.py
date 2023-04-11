import sys
sys.stdin = open('./input.txt','r')

n = int(input())
Tree = [[]for _ in range(n+1)]
parents = [0 for _ in range(n+1)]

for _ in range(n-1):
    a,b = map(int,input().split())
    Tree[a].append(b)
    Tree[b].append(a)

def dfs(start,Tree,parents):
    for i in Tree[start]:
        if parents[i] == 0:
            parents[i] = start
            dfs(i,Tree,parents)
dfs(1,Tree,parents)
for i in range(2,n+1):
    print(parents[i])