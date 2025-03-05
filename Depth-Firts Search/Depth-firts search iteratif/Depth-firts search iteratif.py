def telusuri_dfs_iteratif(peta, simpul_awal):
    sudah_dikunjungi = set()
    tumpukan = [simpul_awal]

    while tumpukan:
        simpul = tumpukan.pop()
        if simpul not in sudah_dikunjungi:
            print(simpul, end=" ")
            sudah_dikunjungi.add(simpul)
            tumpukan.extend(reversed(peta[simpul]))
    
    return sudah_dikunjungi

peta_hubungan = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print("Hasil Penelusuran DFS (Iteratif):")
telusuri_dfs_iteratif(peta_hubungan, 'A')