import pytest
from challenge01 import Graph
# Write your test here

def test_graph_breadth_first_traversal():
    graph = Graph()
    node_a = graph.add_node("A")
    node_b = graph.add_node("B")
    node_c = graph.add_node("C")
    node_d = graph.add_node("D")
    node_e = graph.add_node("E")
    graph.add_edge(node_a, node_b)
    graph.add_edge(node_a, node_c)
    graph.add_edge(node_b, node_c)
    graph.add_edge(node_c, node_d)
    graph.add_edge(node_d, node_e)
    actual = ['A', 'B', 'C', 'D', 'E']
    expected = graph.breadth_first_traversal(node_a)
    assert actual == expected


def test2_graph_breadth_first_traversal():
    graph = Graph()
    node_1 = graph.add_node(1)
    node_2 = graph.add_node(2)
    node_3 = graph.add_node(3)
    node_4 = graph.add_node(4)
    node_5 = graph.add_node(5)
    node_6 = graph.add_node(6)
    node_7 = graph.add_node(7)
    graph.add_edge(node_1, node_2)
    graph.add_edge(node_1, node_3)
    graph.add_edge(node_2, node_3)
    graph.add_edge(node_3, node_4)
    graph.add_edge(node_3, node_5)
    graph.add_edge(node_4, node_6)
    graph.add_edge(node_5, node_7)
    actual = graph.breadth_first_traversal(node_1)
    expected = [1, 2, 3, 4, 5, 6, 7]
    assert actual == expected

def test3_graph_breadth_first_traversal():
    graph = Graph()
    node1 = graph.add_node(1)
    node2 = graph.add_node(2)
    node3 = graph.add_node(3)
    node4 = graph.add_node(4)
    node5 = graph.add_node(5)
    graph.add_edge(node1, node2)
    graph.add_edge(node2, node3)
    graph.add_edge(node3, node4)
    graph.add_edge(node4, node5)
    actual = [5, 4, 3, 2, 1]
    expected = graph.breadth_first_traversal(node5)
    assert actual == expected