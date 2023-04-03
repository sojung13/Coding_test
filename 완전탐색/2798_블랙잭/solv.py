import sys
sys.stdin = open('input.txt','r')

n,m = map(int,input().split())
arr = list(map(int,input().split()))
li = []
for i in range(n):  
    for j in range(i+1,n):  
        for k in range(j+1,n):
            if arr[i] + arr[j] + arr[k] <= m:
                li.append(arr[i] + arr[j] + arr[k])
print(max(li))