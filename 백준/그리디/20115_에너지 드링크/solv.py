import sys
sys.stdin = open('input.txt','r')

n = int(input())
arr = list(map(int,input().split()))
arr.sort(reverse=True)

sum = arr[0]
for i in range(1,n):
    sum += arr[i]/2
print('%g'%sum)