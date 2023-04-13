import sys
sys.stdin = open('input.txt','r')
n = int(input())
total = 0
count = 0
while True:
    count += 1
    total += count
    if total > n:
        break
print(count-1)