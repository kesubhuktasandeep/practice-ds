import networkx as nx

G = nx.Graph()

G.add_edges_from([(1, 2), (1, 3), (2, 3), (2, 4), (3, 4)])

# Print Adjacency List
print("Adjacency List:")
for node, neighbors in G.adjacency():
    print(f"{node}: {list(neighbors)}")

# Print Adjacency Matrix
adjacency_matrix = nx.to_numpy_matrix(G)
adjacency_matrix_list = adjacency_matrix.tolist()
print("Adjacency Matrix:")
for row in adjacency_matrix_list:
    print(row)