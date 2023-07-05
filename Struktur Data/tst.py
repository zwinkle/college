import csv
import time

class TSTNode:
    def __init__(self, char):
        self.char = char
        self.left = None
        self.middle = None
        self.right = None
        self.value = None
        self.depth = 0

class TST:
    def __init__(self):
        self.root = None
    
    def insert(self, key, value):
        self.root = self.insert_node(self.root, key, value, 0)
    
    def insert_node(self, node, key, value, index):
        if index >= len(key):
            node.value = value
            return node
        
        c = key[index]
        
        if node is None:
            node = TSTNode(c)
        
        if c < node.char:
            node.left = self.insert_node(node.left, key, value, index)
        elif c > node.char:
            node.right = self.insert_node(node.right, key, value, index)
        elif index < len(key) - 1:
            node.middle = self.insert_node(node.middle, key, value, index + 1)
        else:
            node.value = value
        
        return node
    
    def search(self, key):
        return self.search_node(self.root, key, 0)
    
    def search_node(self, node, key, index):
        if node is None:
            return None
        
        if index >= len(key):
            return node
        
        c = key[index]
        
        if c < node.char:
            return self.search_node(node.left, key, index)
        elif c > node.char:
            return self.search_node(node.right, key, index)
        elif index < len(key) - 1:
            return self.search_node(node.middle, key, index + 1)
        else:
            return node

    def get_depth(self):
        return self.get_node_depth(self.root)

    def get_node_depth(self, node):
        if node is None:
            return -1
        
        left_depth = self.get_node_depth(node.left)
        middle_depth = self.get_node_depth(node.middle)
        right_depth = self.get_node_depth(node.right)
        
        return max(left_depth, middle_depth, right_depth) + 1

    def set_depth(self):
        self.set_node_depth(self.root, 0)

    def set_node_depth(self, node, depth):
        if node is None:
            return
        
        node.depth = depth

        self.set_node_depth(node.left, depth + 1)
        self.set_node_depth(node.middle, depth + 1)
        self.set_node_depth(node.right, depth + 1)


def r_csv(file_path):
    data = []
    
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            key = row['laptop_ID']
            value = {
                'Company': row['Company'],
                'Product': row['Product'],
                'TypeName': row['TypeName'],
                'Inches': row['Inches'],
                'ScreenResolution': row['ScreenResolution'],
                'Cpu': row['Cpu'],
                'Ram': row['Ram'],
                'Memory': row['Memory'],
                'Gpu': row['Gpu'],
                'OpSys': row['OpSys'],
                'Weight': row['Weight'],
                'Price_in_euros': row['Price_in_euros']
            }
            
            data.append((key, value))
    
    return data

# Menginput data yang akan dicari
input = input("Masukkan kata kunci data yang ingin dicari: ")

# Membaca data dari file CSV
csv_file = 'laptops.csv'
data = r_csv(csv_file)

# Membuat objek TST
tst = TST()

# Memasukkan data ke TST
for key, value in data:
    tst.insert(key, value)

# Mengukur waktu pencarian
start_time = time.time()

# Contoh penggunaan:
search_value = input

# Menghitung jumlah kedalaman maksimum
max_depth = tst.get_depth()

# Mengatur kedalaman setiap node
tst.set_depth()

results = []

# Mencari data pada TST
def search_tst(node, prefix, search_value):
    if node is None:
        return
    
    if node.value is not None:
        for val in node.value.values():
            if search_value.lower() in str(val).lower():
                results.append((prefix, node.value))
                break
    
    search_tst(node.left, prefix, search_value)
    search_tst(node.middle, prefix + node.char, search_value)
    search_tst(node.right, prefix, search_value)

search_tst(tst.root, '', search_value)

end_time = time.time()

# Menampilkan hasil
if results:
    print(f"Kata kunci ditemukan pada data '{search_value}':")
    for key, value in results:
        print("ID:", key)
        for attribute, val in value.items():
            print(f"{attribute}: {val}")
        print("Kedalaman tree:", tst.search(key).depth)  # Menampilkan kedalaman node
        print()
else:
    print(f"Tidak ada data yang ditemukan dengan kata kunci '{search_value}'")

print("="*3, "HASIL", "="*3)
print("\nANALISIS:")
print("Kedalaman maksimum:", max_depth)
print("Waktu mulai:", start_time)
print("Waktu selesai:", end_time)
total_time = round(end_time - start_time, 6)
print("Waktu pencarian:", total_time, "detik")
if total_time == 0.0:
    print("")
    print("="*13)
    print(f"\nINFO:\nWaktu menunjukkan {total_time} bukan berarti program tidak bisa menghitung waktunya ataupun kesalahan kode.\n\nBisa dilihat pada catatan diatas, Waktu mulai dan Waktu selesai memiliki angka yang sama, jika angka yang sama diselisihkan, maka hasilnya adalah 0.\n\nHal ini terjadi karena cepatnya algoritma mencari dan menampikan data pada layar.")
    print("")
    print("="*2, "SELESAI", "="*2)
    print("")