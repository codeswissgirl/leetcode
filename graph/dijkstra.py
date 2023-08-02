import heapq

def dijkstra(graph, start):
    # Initialize the distance dictionary with infinity values
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0

    # Initialize the priority queue with the start vertex
    pq = [(0, start)]

    while pq:
        # Get the vertex with the smallest weight from the priority queue
        current_distance, current_vertex = heapq.heappop(pq)

        # If the current distance is larger than the stored distance, skip it
        if current_distance > distances[current_vertex]:
            continue

        # Iterate over the neighbors of the current vertex
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # If the new distance is smaller than the stored distance, update it
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances
