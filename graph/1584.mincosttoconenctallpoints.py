"""
Solution:

This problem can be solved using Prim's Algorithm. In this context, Prim's Algorithm is a greedy algorithm that finds a minimum spanning tree for a connected weighted undirected graph, which means it finds a subset of the edges that forms a tree that includes every vertex, where the total weight of all the edges in the tree is minimized.

We start from the first point and keep adding points to our answer which have the minimum cost to connect and aren't already connected.
"""

from typing import List
import heapq

def minCostConnectPoints(points: List[List[int]]) -> int:
    n=len(points)
    adj={i:[]for i in range(n)} #i: list of [cost,node] each edge is weight
    for i in range(n):
        x1,y1=points[i]
        for j in range(i+1,n): #we dont compare with each, with other
            x2,y2=points[j]
            dist=abs(x1-x2)+(y1-y2)
            adj[i].append([dist,j])
            adj[j].append([dist,i])
    #prime:
    res=0
    visit=set()
    minHeap=[[0,0]] #cost,point

    while len(visit)<n:
        cost,i=heapq.heappop(minHeap)
        if i in visit:
            continue
        res+=cost
        visit.add(i)
        for neicost,nei in adj[i]:
            if nei not in visit:
                heapq.heappush(minHeap,[neicost,nei])
    return res
“““
Here's how Prim's Algorithm works:

Initialize: Start with an empty graph for the minimum spanning tree (MST) and a set (or list) of visited nodes. Pick any node from the graph as the starting node and add it to the visited set.
Find the minimum edge: Out of all edges that connect a node in the visited set to a node outside it, pick the edge with the smallest weight.
Add the new edge to the MST: Add the selected edge and the new node (the one that was outside the visited set) to the MST and the visited set, respectively.
Repeat: Continue this process until all nodes have been added to the MST (i.e., the visited set contains all nodes).
The result will be a tree that connects all nodes of the graph with the minimum possible total edge weight. Note that the tree may not be unique: if the graph has edges with equal weight, there might be different trees with the same total weight.

Prim's Algorithm is greedy because at each step, it picks the edge with the smallest weight, without worrying about the future consequences. This local optimal choice at each step leads to a global optimum, which is a characteristic of greedy algorithms.

The time complexity of Prim's Algorithm depends on how it's implemented. Using a binary heap, it can be run in O(E log E) time, where E is the number of edges in the graph. With a Fibonacci heap, it can run in O(E + V log V) time, where V is the number of vertices in the graph. Note that these complexities assume the graph is represented as an adjacency list; if it's an adjacency matrix, the time complexity will be different.
“““
