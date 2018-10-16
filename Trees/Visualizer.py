import networkx as nx
import matplotlib.pyplot as plt


def create_graph(G, node, pos={}, x=0, y=0, layer=1):
    pos[node.val] = (x, y)
    if node.lchild:
        G.add_edge(node.val, node.lchild.val)
        l_x, l_y = x - 1 / 2 ** layer, y - 1
        l_layer = layer + 1
        create_graph(G, node.lchild, x=l_x, y=l_y, pos=pos, layer=l_layer)
    if node.rchild:
        G.add_edge(node.val, node.rchild.val)
        r_x, r_y = x + 1 / 2 ** layer, y - 1
        r_layer = layer + 1
        create_graph(G, node.rchild, x=r_x, y=r_y, pos=pos, layer=r_layer)
    return G, pos


def draw_tree(root):
    """
    Draw a binary tree with the parameter root being its root node.
    """
    graph = nx.DiGraph()
    graph, pos = create_graph(graph, root)
    nx.draw_networkx(graph, pos, node_size=300)
    plt.show()
