"""
Valid tree is:
- has no cycle
- is connected
for an undirected graph with 'n' nodes to be a tree, it should satisfy the following two conditions:
1. the graph should contian n-1 edges
2. the graph should be connected

In this code, we first check the number of edges. If it's not equal to n - 1, we return False immediately. Then, we construct a graph as an adjacency list. We use DFS to check if the graph is connected. If we can visit all nodes starting from node 0 and no cycles exist, it's a tree.
Time Complexity: The time complexity is O(n) as we visit each node once.
Space Complexity: The space complexity is O(n) to store the graph and the seen set.
"""

import collections
def validTree(n: int, edges: List[List[int]]) -> bool:
    if len(edges) != n - 1:  # condition 1
        return False
    graph=collections.defauldict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    seen=set()
    def dfs(node,parent):
        seen.add(node)
        for neighbor in graph[node]:
            if neighbor ==graph[node]:
                continue
            if neighbor in seen or not dfs[neighbor,node]: return False
        return True
    return dfs(0,0) and len(seen)==n 
