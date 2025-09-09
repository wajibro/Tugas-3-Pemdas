i = 1
j = 0

while i < 10: # Mengecek apakah i < 10
  i += 1      # Kemudian i akan bertambah sebanyak 1
  j += 2*2    # Disaat yang bersamaan j juga bertambah sebanyak (2*2) atau 4

# Karena print berada di luar scope while, maka hanya menampilkan nilai terakhir setelah while
print(i) # Line 1
print(j) # Line 2