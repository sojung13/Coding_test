import sys
sys.stdin = open('input.txt','r')

word = input()
n = int(input())
arr = []
for i in range(n):
    i1, i2 = map(input().split())
    i1 = int(i1)
    arr[i][0].append(int(i1))
    arr[i][1].append(i2)
arr.sort(key=lambda x:x[0])
print(arr)