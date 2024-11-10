#!/usr/bin/env python
# coding: utf-8

# In[4]:


from itertools import permutations

# Matriks jarak antara node
distance_matrix = [
    [0, 10, 12, 15, 10, 20],  
    [10, 0, 8, 12, 9, 14],   
    [12, 8, 0, 6, 11, 13],    
    [15, 12, 6, 0, 7, 9],    
    [10, 9, 11, 7, 0, 5],     
    [20, 14, 13, 9, 5, 0]     
]

nodes = ['A', 'B', 'C', 'D', 'E', 'F']

# Fungsi untuk menghitung jarak total dari rute tertentu
def calculate_route_distance(route, distance_matrix):
    distance = 0
    for i in range(len(route)):
        # Tambahkan jarak antara node yang berurutan dalam rute
        distance += distance_matrix[route[i]][route[(i + 1) % len(route)]]
    return distance

# Fungsi untuk menemukan rute Hamiltonian dengan jarak terpendek
def find_shortest_hamiltonian_route(distance_matrix):
    shortest_distance = float('inf')
    shortest_route = None

    # Buat semua kemungkinan rute (permutasi node)
    for route in permutations(range(len(distance_matrix))):
        # Hitung jarak untuk rute saat ini
        distance = calculate_route_distance(route, distance_matrix)
        
        # Periksa apakah jarak ini lebih pendek dari yang ditemukan sebelumnya
        if distance < shortest_distance:
            shortest_distance = distance
            shortest_route = route

    # Konversi rute dari indeks ke nama node untuk keluaran yang lebih mudah dibaca
    shortest_route_named = [nodes[i] for i in shortest_route]
    return shortest_route_named, shortest_distance

# Temukan rute Hamiltonian dengan jarak terpendek
shortest_route, shortest_distance = find_shortest_hamiltonian_route(distance_matrix)

# Cetak hasil
print("Rute tercepat:", " → ".join(shortest_route))
print("Jarak total:", shortest_distance)


# In[ ]:




