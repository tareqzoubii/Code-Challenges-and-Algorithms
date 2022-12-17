# Write here the code challenge solution
class Node:
    def __init__(self, value=None):
        self.value = value

    def __str__(self):
        return self.value

class Edge:
    def __init__(self,vertex,weight=0):
        self.vertex = vertex
        self.weight = weight

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_node(self,value):
        new_vertex = Node(value)
        self.adj_list[new_vertex] = []
        return new_vertex

    def add_edge(self,node1,node2,weight=0):

        if not node1 in self.adj_list.keys():
            return("this node does not exist")

        if not node2 in self.adj_list.keys():
            return("this node does not exist")

        edge1 = Edge(node2,weight)
        self.adj_list[node1].append(edge1)

        edge2 = Edge(node1,weight)
        self.adj_list[node2].append(edge2)

    def breadth_first_traversal(self, input_value):
        visited = []
        queue = [input_value]
        while queue:
            current_node = queue.pop(0)
            if current_node.value not in visited:
                visited.append(current_node.value)
                for edge in self.adj_list[current_node]:
                    queue.append(edge.vertex)
        return visited


if __name__ == "__main__":
    graph = Graph()
    a = graph.add_node('A')
    b = graph.add_node('B')
    c = graph.add_node('C')
    d = graph.add_node('D')
    e = graph.add_node('E')
    f = graph.add_node('F')
    g = graph.add_node('G')
    h = graph.add_node('H')
    i = graph.add_node('I')
    k = graph.add_node('K')


    graph.add_edge(a, c)
    graph.add_edge(a, e)
    graph.add_edge(a, b)
    graph.add_edge(e, f)
    graph.add_edge(e, g)
    graph.add_edge(e, d)
    graph.add_edge(f, i)
    graph.add_edge(h, k)
    graph.add_edge(b, d)
    graph.add_edge(g, h)
    graph.add_edge(i, k)
    graph.add_edge(c, f)
    graph.add_edge(f, h)


    print(graph.breadth_first_traversal(a))


