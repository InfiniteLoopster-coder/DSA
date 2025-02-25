from collections import deque
from typing import List


class Graph:

    def dfsOfGraph(self, adj):
        visited = [False]*len(adj)
        result = []

        def dfs(node):
            visited[node]=True
            result.append(node)
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    dfs(neighbor)


        dfs(0)
        return result
    

    def bfsOfGraph(self, adj: List[List[int]]) -> List[int]:
        def bfs(node):
            visited = [False]*len(adj)
            result = []
            visited[0] = True
            queue = deque([0])

            while queue:
                node = queue.popleft()
                result.append(node)
                for neighbor in adj[node]:
                    visited = True
                    if not visited[neighbor]:
                        queue.append(neighbor)

            return result
        





if __name__ == "__main__":
    sol = Graph()
    #   # Example BFS
    adj = [[2, 3, 1], [0], [0, 4], [0], [2]]
    ans = sol.bfsOfGraph(adj)
    print(ans)  # Expected Output: [0, 2, 3, 1, 4]

#     # Example DFS
#     adj1 = [[2, 3, 1], [0], [0, 4], [0], [2]]
#     print(sol.dfsOfGraph(adj1))  # Expected Output: [0, 2, 4, 3, 1]
    
#     # Example 2
#     adj2 = [[1, 2], [0, 2], [0, 1, 3, 4], [2], [2]]
#     print(sol.dfsOfGraph(adj2))  # Expected Output: [0, 1, 2, 3, 4]  





          