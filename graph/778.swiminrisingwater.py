

import heapq

def swimInWater(grid):
    N = len(grid)
    time = [[float('inf')]*N for _ in range(N)]
    time[0][0] = grid[0][0]
    pq = [(grid[0][0], 0, 0)]

    while pq:
        t, x, y = heapq.heappop(pq)
        if t > time[x][y]:
            continue
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                new_time = max(t, grid[nx][ny])
                if new_time < time[nx][ny]:
                    time[nx][ny] = new_time
                    heapq.heappush(pq, (new_time, nx, ny))
    return time[N-1][N-1]
