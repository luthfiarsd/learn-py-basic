# LIST BISA UNTUK TIPE DATA APA SAJA
data_boolean = [True, False, True, False, False]
print(data_boolean)

# BISA CAMPURAN
campuran = ["bala-bala", 2, "cireng", False, 12.4]
print(campuran)

# CARA MEMBUAT LIST
data_range = range(0, 10)
list_data_range = list(data_range)
print(list_data_range)

# MEMBUAT LIST DENGAN FOR LOOP
listfor = [i for i in range(0, 10)]
print(listfor)

listfor = [i**2 for i in range(0, 10)]
print(listfor)

# MEMBUAT LIST DENGAN FOR IF
listforif = [i for i in range(0, 10) if i % 2 != 0]
print(listforif)

# BERSIFAT SAMA SEPERTI ARRAY
coba_array = ["satu", "dua", "tiga", "empat"]
print(coba_array[0])
print(len(coba_array))