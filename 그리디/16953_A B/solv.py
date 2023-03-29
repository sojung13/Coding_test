import sys
sys.stdin = open('input.txt','r')

a,b = map(int,input().split())
answer = 1
while a != b:
    answer += 1
    temp = b
    if b % 10 == 1:
        b //= 10
    elif b % 2 == 0:
        b //=2
    
    if temp == b:
        print(-1)
        break
else:
    print(answer)