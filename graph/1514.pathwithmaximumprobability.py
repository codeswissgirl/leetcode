"""
1514. Path with Maximum Probability" 
- graph problem
- maximum probability from start to end
- use dijkstras algorithm: finding the minimum distance, -> max probability 
  probability is equivalent to the product of the edge weights along the path

step-to-step:
1. create an adjacency list to represent the graph, each edge in the graph is associated with a probability (weight)
2. initialize a probabilites list with a size of n, setting all elements to 0, except for the start node which is set to 1
3. use a priority queue to store the nodes to be visited, prioritzing the node with the hightes probability, begin with the start node
4. for the current node, iterate through its neighbors 
- if probability of reaching a neighbor via the currrent node is higher than the previously known probability for this neighbor, update the neigbors proability in the probabilites list and push it into the queue.
5. repeat step 4 until the queue is empty or until weve processed the end node
5. return the max probability of reaching the end node, which is stored in the probabliites list

Time complexity: The time complexity is O(ElogE) where E is the number of edges. This is because in the worst case we add all edges to the heap.

Space complexity: The space complexity is O(N + E) where N is the number of nodes and E is the number of edges. This is due to the storage required for the adjacency list and the heap.
"""

import heapq

def maxProbability(n, edges, succProb, start, end):
    graph = [[] for _ in range(n)]
    for (x,y),prob in zip(edges,succProb): #x= source, y= destination
        graph[x].append((y,prob))
        graph[y].append((x,prob))
    pq=[(-1,start)] #-1 is neutral value,  and first node is start
    visit=set()
    while pq>0:
        prob,node=heapq.heappop(pq)
        visit.add(cur)
        if cur==end:
            return prob*-1
        for nei,edgeProb in graph[cur]:
            if nei not in visit:
                heapq.heappush(pq,(prob*edgeProb,nei))
    return 0
