import sys
sys.stdin = open('input.txt','r')
from itertools import permutations

n = int(input())
k = int(input())
arr = []
for _ in range(n):
    arr.append(input())
answer = set()
for i in permutations(arr,k):
    answer.add(''.join(i))
print(len(answer))