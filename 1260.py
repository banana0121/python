import sys
from collections import deque


def bfs(g, v):
    visited = []
    queue = deque([v])

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            queue.extend(g[n])
    
    return " ".join(str(i) for i in visited)

def dfs(g, v):
    visited = []
    stack = deque([v])
    #stack = [v]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            stack.extend(reversed(g[n]))
            
    
    return " ".join(str(i) for i in visited)


N, M, V = map(int, (sys.stdin.readline().split()))
graph = {}

for i in range(1, N+1):
    graph[i] = list()

for i in range(M):
    a, b = map(int, (sys.stdin.readline().split()))

    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N+1):
    graph[i].sort()

print(dfs(graph, V))
print(bfs(graph, V))



#" ".join(str(i) for i in visited)
#"".join() ""사이에 구분자 넣어서 매개변수들을 문자열로 합침.a
