import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

n = int(input())
stones = list(map(int,input().split()))
