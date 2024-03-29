import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int,input().split())
inDegree = [0] * (n+1)
graph = {i:[] for i in range(1,n+1)}
for _ in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    inDegree[b] += 1
    
ans = []
q = deque()
for i in range(1,n+1):
    if inDegree[i] == 0:
        q.append(i)
        
while q:
    now = q.popleft()
    ans.append(now)
    
    for i in graph[now]:
        inDegree[i] -= 1
        if inDegree[i] == 0:
            q.append(i)

print(*ans,sep=' ')