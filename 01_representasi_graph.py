# Representasi Graph: Adjacency List dan Adjacency Matrix

# 1. Representasi Adjacency List (Kota Skotlandia)
adj_list_scotland = {
    'Inverness': [('Aberdeen', 103), ('Glasgow', 168), ('Edinburgh', 154)],
    'Aberdeen': [('Inverness', 103), ('Glasgow', 139), ('Edinburgh', 119)],
    'Glasgow': [('Inverness', 168), ('Aberdeen', 139), ('Edinburgh', 44)],
    'Edinburgh': [('Inverness', 154), ('Aberdeen', 119), ('Glasgow', 44)]
}

# 2. Representasi Adjacency Matrix
cities = ['Inverness', 'Aberdeen', 'Glasgow', 'Edinburgh']
adj_matrix = [
    [0,   103, 168, 154],
    [103, 0,   139, 119],
    [168, 139, 0,   44],
    [154, 119, 44,  0]
]

if __name__ == "__main__":
    print("=== Representasi Graph: Adjacency List ===")
    for kota, tetangga in adj_list_scotland.items():
        print(f"Simpul [{kota}]:")
        for t in tetangga:
            print(f"  -> {t[0]} (Jarak: {t[1]} mil)")

    print("\n=== Representasi Graph: Adjacency Matrix ===")
    print("           ", "  ".join(f"{c[:4]:>4}" for c in cities))
    for i, row in enumerate(adj_matrix):
        print(f"{cities[i]:<10}", "  ".join(f"{val:>4}" for val in row))
