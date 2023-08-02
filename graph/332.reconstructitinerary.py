"""
We can solve this problem using Hierholzer's algorithm to find an Eulerian path in the graph. The graph here is represented by the list of tickets where each ticket is an edge from the departure airport to the arrival airport.
In this solution, we first construct a graph where each airport maps to a min-heap of its neighbors. We then perform a depth-first search from the 'JFK' airport. As we visit each airport, we remove it from the current airport's list of destinations. Finally, we append the airport to the route and return the route in reverse order.

Time Complexity: The time complexity is O(n log n), where n is the number of tickets. We have to sort the tickets, and each insertion into a heap is O(log n).

Space Complexity: The space complexity is O(n) to store the graph and the route.


"""

def findItinerary(tickets):
    graph=collections.defaultdict(list)
    for start, end in sorted(tickets)[::-1]:
        graph[start].append(end) #graph building adjecent 
        print(graph)
    route=[]
    def visit(airport):
        print(graph)
        while graph[airport]:
            visit(graph[airport].pop())
        route.append(airport)
    visit('JFK') #start airport

    return route[::-1]
tickets=[['MUC','LHR'], ['JFK','MUC'], ['SFO','SJC'], ['LHR','SFO']]
tickets2=[['JFK','SFO'], ['JFK','ATL'], ['SFO','ATL'], ['ATL','JFK'],['ATL', "SFO"]]
