import sys
sys.stdin = open('input.txt','r')

n,k = map(int,input().split())
arr = list(map(int,input().split()))

sum_dict = {0:1}

sum_ = 0
answer = 0

for i in arr:
    sum_ += i
    if sum_ - k in sum_dict.keys():
        answer += sum_dict[sum_ - k]
    sum_dict[sum_] = sum_dict.get(sum_,0) + 1
print(answer)