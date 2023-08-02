#djikstras algorithm: that finds the shortest path between nodes in a graph, which may repsrent road network
"""
starting at 2, how long would it take for the signal to go in each signal (node). we return -1 if impossible for nodes to receive the signal.
we have weights for each nodes. it is shown in the picture
"""
def networkDelayTime(times, n, k):
    graph=collections.defaultdict(list)
    for u,v,w in times: #w is weight
        graph[u].append((v,w))
    minHeap=[(0,k)] #datastructure
    visit=set()
    t=0 
    while minHeap>0:
        w1,n1=heapq.heappop(minHeap) #we delete weight and node
        if n1 in visit:
            continue
        visit.add(n1)
        t=max(t,w1)
        #breathfirstsearch
        for n2,w2 in graph[n1]: #that which we pop from neighbor
            if n2 not in visit:
                heapq.heappush(minHeap,(w2,n2))
    return t if len(visit)==n else -1 #what takes time to visit each node
