def telusuri_dfs(peta, simpul_awal, sudah_dikunjungi=None):
    if sudah_dikunjungi is None:
        sudah_dikunjungi = set()
    sudah_dikunjungi.add(simpul_awal)
    print(simpul_awal, end=" ")
    
    for tetangga in peta[simpul_awal]:
        if tetangga not in sudah_dikunjungi:
            telusuri_dfs(peta, tetangga, sudah_dikunjungi)
    
    return sudah_dikunjungi

peta_hubungan = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print("Hasil Penelusuran DFS (Rekursif):")
telusuri_dfs(peta_hubungan, 'A')
