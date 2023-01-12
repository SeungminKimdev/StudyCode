import sys
input = sys.stdin.readline

N = int(input())
a = [0]*10001
for _ in range(N):
    a[int(input())] += 1
    
for i in range(1,10001):
    if a[i] != 0:
        for _ in range(a[i]):
            print(i)