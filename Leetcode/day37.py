from typing import List

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])
        INF = 10**18
        dist = [[INF]*m for _ in range(n)]
        dist[0][0] = 0
        pq = [(0, 0, 0)]  # (time, i, j)
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]

        while pq:
            t, i, j = heapq.heappop(pq)
            if t > dist[i][j]:
                continue
            if i == n-1 and j == m-1:
                return t
            for di, dj in dirs:
                ni, nj = i+di, j+dj
                if 0 <= ni < n and 0 <= nj < m:
                    # Correct arrival time:
                    nt = max(t, moveTime[ni][nj]) + 1
                    if nt < dist[ni][nj]:
                        dist[ni][nj] = nt
                        heapq.heappush(pq, (nt, ni, nj))

        return dist[n-1][m-1]