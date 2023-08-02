def prim(graph):
    n=len(graph)
    visited=[False]*n
    key=[float('inf')]*n
    parent=[-1]*n
    key[0]=0
    for _ in range(n):
        min_key=float('inf')
        for i in range(n):
            if not visited[i] and key[i]<min_key:
                min_key=key[i]
                u=i
        visited[u]=True
        for v in range(n):
            if graph[u][v]>0 and not visited[v] and graph[u][v]<key[v]:
                key[v]=graph[u][v]
                parent[v]=u
    for i in range(1, n):
        print(f"Edge: {parent[i]}-{i}, Weight: {graph[i][parent[i]]}")
graph = [[0, 2, 0, 6, 0],
         [2, 0, 3, 8, 5],
         [0, 3, 0, 0, 7],
         [6, 8, 0, 0, 9],
         [0, 5, 7, 9, 0]]

print(prim(graph))
