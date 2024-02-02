# MENAMBAHKAN DATA DALAM LIST
coba_array = ["satu", "dua", "tiga", "empat"]
coba_array.insert(0, "sepuluh")  # 0 berarti indeks yang mau ditaruh
print(coba_array)
# taruh data baru di akhir
coba_array.append("enam sembilan")
print(coba_array)

# MENYATUKAN LIST DENGAN LIST
coba_array0 = ["mantap", "oke", "sip", "iya"]
print(coba_array0)
print()
coba_array0.extend(coba_array)
print(coba_array0)

# MENGHAPUS DATA
coba_array0.remove(coba_array0[0])
coba_array0.remove("dua")
print(coba_array0)
# menghapus data paling belakang
coba_array0.pop()
print(coba_array0)

# MENGHITUNG BANYAK DATA
deret = [2, 4, 5, 8, 1, 1, 2, 2, 4, 4, 5, 6, 7, 3, 3, 2, 2, 4]
print("Banyaknya 2 pada list deret = ", deret.count(2))

# AMBIL POSISI DATA
data = ["apa", "afah", "aph", "apah"]
print("Indeks aph pada list data = ", data.index("aph"))

# MENGURUTKAN DATA
deret.sort()
print(deret)  # yang diprint deretnya, sort operasi saja tidak bisa ditampilkan
data.sort()
print(data)  # jika string maka yang disort dimulai dari depan
data.sort(key=len)
print(data)  # sorting berdasarkan length

# MEMBALIK LIST
data.reverse()
print(data)

# MENDUPLIKAT LIST, DALAM PYTHON VARIABEL BERSIFAT BY REFERENCE
print()
asli = [7, 6, 4, 2, 5, 2, 4, 6]
duplikat = asli.copy()

print(asli)
duplikat.sort()
print(duplikat)

# LIST DALAM LIST (NESTED LIST)

orang1 = ["Alif", 25, "Laki-laki"]
orang2 = ["Dewi", 28, "Perempuan"]
data_2d = [orang1, orang2]
print(data_2d)

for orang in data_2d:
    print("Nama             : ", orang[0])
    print("Umur             : ", orang[1])
    print("Jenis Kelamin    : ", orang[2])
    print()
