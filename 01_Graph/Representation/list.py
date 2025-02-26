from collections import defaultdict

class Graphlist:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u:int, v:int):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def display(self):
        for vertices,neighbir in self.graph.items():
            print(f"{vertices}:{neighbir}")


if __name__ == "__main__":
    g_list = Graphlist()
    g_list.add_edge(0, 1)
    g_list.add_edge(0, 4)
    g_list.add_edge(1, 2)
    g_list.add_edge(1, 3)
    g_list.add_edge(1, 4)
    g_list.add_edge(2, 3)
    g_list.add_edge(3, 4)

    print("\nAdjacency List Representation:")
    g_list.display()
