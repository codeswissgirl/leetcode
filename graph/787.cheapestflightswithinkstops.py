"""
There are n cities connected by m flights. Each flight starts from city u and arrives at v with a price w.

Now given all the cities and flights, together with starting city src and the destination dst, your task is to find the cheapest price from src to dst with up to k stops. If there is no such route, output -1.

Interview Questions:
Before diving into the solution, you might want to clarify a few things with the interviewer:

Can there be multiple flights between the same pair of cities?
Are the flights directional, i.e., if there's a flight from city u to v, does it necessarily mean there's a flight from v to u?
Are negative costs possible?
Is it possible to have a flight from a city to itself?
Once you have clarified these points, you can move on to the solution.

Easy-to-understand Solution Approach:
You could use Dijkstra's algorithm with a slight modification to keep track of the number of stops made. The traditional Dijkstra's algorithm does not work here because it discards the longer path between two nodes, but in this case, a longer path could have fewer stops and thus could potentially lead to a cheaper price.
"""
import heapq
def findCheapestPrice(n, flights, src, dst, K):
    graph=[[] for _ in range(n)]
    for u,v,w in flights:
        graph[u].append((v,w))
    heap=[(0, src,K+1)]
    while heap:
        cost,node,stops=heapq.heappop(heap)
        if node==dst:
            return cost
        if stops>0: 
            for v,w in graph[node]:
                heapq.heappush(heap,(cost+w,v,stops-1))
    return -1
