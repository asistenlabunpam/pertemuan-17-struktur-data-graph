# Pembuatan dan Manipulasi Graph Menggunakan NetworkX

def demo_networkx_graph():
    try:
        import networkx as nx
        
        # Creating a Graph
        G = nx.Graph()

        # Add a node
        G.add_node(1)
        G.add_nodes_from([2, 3])

        # Add edges
        G.add_edge(1, 2)
        e = (2, 3)
        G.add_edge(*e)
        G.add_edges_from([(1, 2), (1, 3)])

        print("=== Informasi Graph NetworkX ===")
        print("Daftar Node (Simpul):", list(G.nodes()))
        print("Daftar Edge (Tepi):", list(G.edges()))
        print("Derajat Node 1:", G.degree[1])

    except ImportError:
        print("Modul networkx tidak terinstal. Menjalankan fallback sederhana:")
        # Fallback versi dict sederhana
        graph_dict = {
            1: [2, 3],
            2: [1, 3],
            3: [1, 2]
        }
        print("Daftar Node (Simpul):", list(graph_dict.keys()))
        print("Daftar Edge (Tepi):", [(k, v) for k, vals in graph_dict.items() for v in vals if k < v])

if __name__ == "__main__":
    demo_networkx_graph()
