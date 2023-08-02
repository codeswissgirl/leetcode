"""
Topological sorting for Directed Acyclic Graph (DAG) is a linear ordering of vertices such that for every directed edge u->v, vertex u comes before v in the ordering. Topological Sorting for a graph is not possible if the graph is not a DAG.

Here's the algorithm for Topological Sorting:

Step 1: Identify vertices that have no incoming edges, i.e., those which have in-degree 0.
Step 2: Start with any vertex with in-degree 0 and remove it from the graph. Add it to the topological sort.
Step 3: Removing the vertex reduces the in-degree of vertices it was pointing to. This may result in new vertices with in-degree 0. Repeat step 2 with these vertices.
Step 4: Repeat steps 2-3 until there are no more vertices left in the graph.

The time complexity of the algorithm is O(V+E), where V is the number of vertices and E is the number of edges in the graph, as we process all nodes and edges once. The space complexity is also O(V+E), to store the graph, the in-degree of each node, and the queue for sources.
"""
from collections import deque

def topological_sort(vertices, edges):
    sorted_order = []
    if vertices <= 0:
        return sorted_order

    # a. Initialize the graph
    in_degree = {i: 0 for i in range(vertices)}  # count of incoming edges
    graph = {i: [] for i in range(vertices)}  # adjacency list graph

    # b. Build the graph
    for edge in edges:
        parent, child = edge[0], edge[1]
        graph[parent].append(child)
        in_degree[child] += 1

    # c. Find all sources i.e., all vertices with 0 in-degrees
    sources = deque()
    for key in in_degree:
        if in_degree[key] == 0:
            sources.append(key)

    # d. For each source, add it to the sorted_order and subtract one from all of its children's in-degrees
    # if a child's in-degree becomes zero, add it to the sources queue
    while sources:
        vertex = sources.popleft()
        sorted_order.append(vertex)
        for child in graph[vertex]:  # get the node's children to decrement their in-degrees
            in_degree[child] -= 1
            if in_degree[child] == 0:
                sources.append(child)

    # topological sort is not possible as the graph has a cycle
    if len(sorted_order) != vertices:
        return []

    return sorted_order
