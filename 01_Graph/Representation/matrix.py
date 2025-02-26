class GraphMatrix:
    def __init__(self, vertices:int):
        self.V = vertices
        self.matrix = [[0]* vertices for _ in range(vertices)]

    def add_edge(self, u:int, v:int, weight:int=1):
        self.matrix[u][v] = weight
        self.matrix[v][u] = weight


    def display(self):
        for row in self.matrix:
            print("".join(map(str,row)))


if __name__ == "__main__":
    g_matrix = GraphMatrix(5)
    g_matrix.add_edge(0, 1)
    g_matrix.add_edge(0, 4)
    g_matrix.add_edge(1, 2)
    g_matrix.add_edge(1, 3)
    g_matrix.add_edge(1, 4)
    g_matrix.add_edge(2, 3)
    g_matrix.add_edge(3, 4)
    print("Adjacency Matrix Representation:")
    g_matrix.display()


