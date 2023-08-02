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

Discussing Time and Space Complexity:
Time Complexity: The time complexity is O(E + N * log(N)), where E is the total number of flights and N is the number of cities. This is due to the fact that we potentially visit all edges and the heap operations take log(N) time.
Space Complexity: The space complexity is O(N + E) since we need to store the graph and the min-heap in memory.
Handling Edge Cases and Assumptions:
If src is the same as dst and k is 0, we can return 0, as no travel is required.
If the cities are disconnected and there is no path from src to dst, the function will return -1 as required.
Optimizations and Follow-up:
Discuss if any other algorithms could be applicable here, such as Bellman-Ford.
Discuss how this solution can be extended for various other scenarios or constraints.
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

def findCheapestPrice(n, flights, src, dst, K):
    #bellmon ford algorithm. 
    prices=[float('inf')]*n
    prices[src]=0
    for i in range(k+1):
        tmpPrices=prices.copy()
        for s,d,p in flights:
            if prices[s]==float('inf'):
                continue
            if prices[s]+p<tmpPrices[d]:
                tmpPrices[d]=prices[s]+p
        prices=tmpPrices
    return prices[dst]
n = 3
flights = [[0,1,100],[1,2,100],[0,2,500]]
src = 0
dst = 2
k = 1
result = findCheapestPrice(n, flights, src, dst, k)
print(result)

