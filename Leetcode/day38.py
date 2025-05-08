from typing import List


class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n,m = len(moveTime), len(moveTime[0])
        INF = 10**18
        dist = [[[INF, INF] for _ in range(m)] for __ in range(n)]
        dist[0][0][0] = 0 

        pq = [(0, 0, 0, 0)]
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]

        while pq:
            t, i, j, p = heapq.heappop(pq)
            if t > dist[i][j][p]:
                continue
            if i == n-1 and j == m-1:
                return t
            step_cost = 1 if p == 0 else 2
            next_parity = 1 - p

            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if not (0 <= ni < n and 0 <= nj < m):
                    continue
                start_time = max(t, moveTime[ni][nj])
                arrive_time = start_time + step_cost

                if arrive_time < dist[ni][nj][next_parity]:
                    dist[ni][nj][next_parity] = arrive_time
                    heapq.heappush(pq, (arrive_time, ni, nj, next_parity))
        return -1