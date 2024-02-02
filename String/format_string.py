# FORMAT STRING F
nama = "mantap"
formatstr = f"weh {nama}"
print(formatstr)
# bisa angka, boolean dll

# AUTO DETEKSI RIBUAN
ribu = 2000000
formatribu = f"Rp {ribu:,}"
print(formatribu)

# MANIPULASI DESIMAL
angka = 200.654321
formatangka1 = f"2 angka desimal ke belakang {angka:.2f}"
print(formatangka1)
# leading zero
formatangka2 = f"9 angka total {angka:010.2f}"  # titik dihitung juga
print(formatangka2)

# FORMAT PERSEN
persen = 0.45
formatpersen = f"persenan {persen:.0%}"
formatpersen2 = f"persenan kedua {persen:.5%}"
print(formatpersen)
print(formatpersen2)

# OPERASI ARITMATIKA DALAM PLACEHOLDER
harga = 10000
jumlah = 50
hasil = f"hasilnya adalah {harga*jumlah:,}"
print(hasil)

# FORMAT ANGKA LAIN
angka = 255
formatbinary = f"biner = {bin(angka)}"
formathex = f"hex = {hex(angka)}"
formatoctal = f"oktal = {oct(angka)}"
print(formatbinary)
print(formatoctal)
print(formathex)
