# LAMBDA FUNCTION
# output = lambda argument: expression

kuadrat = lambda angka: angka**2
print(kuadrat(3))

pangkat = lambda angka, pow: angka**pow
print(pangkat(2, 4))

list_nama = ["Rafi", "Alghifary", "Edi", "Junaedi"]
list_nama.sort(key=lambda nama: len(nama))
print(list_nama)

# SINTAKS FILTER DENGAN ARGUMEN FUNGSI BIASA
list_angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def kurang_dari_lima(angka):
    if angka < 5:
        return angka


list_angka_baru = list(filter(kurang_dari_lima, list_angka))
print(list_angka_baru)

# DENGAN LAMBDA
data_angka_baru = list(filter(lambda angka: angka > 4, list_angka))
print(data_angka_baru)

ganjil = list(filter(lambda angka: angka % 2 != 0, list_angka))
print(ganjil)
genap = list(filter(lambda angka: angka % 2 == 0, list_angka))
print(genap)


# ANONIMOUS FUNCTION
# MEMBUAT VARIABEL MENJADI FUNGSI
def pangkat(n):
    return lambda angka: angka**n


pangkatDua = pangkat(2)
pangkatTiga = pangkat(3)
pangkatLima = pangkat(5)

print(pangkatDua(6))
print(pangkatLima(2))
print(pangkatTiga(5))
