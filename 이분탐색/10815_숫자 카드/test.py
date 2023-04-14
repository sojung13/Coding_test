import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

n = int(input())
card = list(map(int,input().split()))
card.sort()
m = int(input())
whether = list(map(int,input().split()))

def bs(target):
    start,end = 0, n
    while start <= end:
        mid = (start + end) // 2  # 2
        if card[mid] == target:
            return 1
        elif card[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return 0

for i in whether:
    print(bs(i),end=' ')