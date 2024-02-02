prefix = "Luthfi"
suffix = "Hamam Arsyada~"

fullname = prefix + " " + suffix
print(fullname)
print("Panjangnya adalah = " + str(len(fullname)))

# CEK ADA KOMPONEN CHAR ATAU STRING
a = "a"
status = a in fullname
print("Apakah huruf a di fullname = ", status)

# MENGULANG STRING
print("wk" * 10)
print("\n")

# INDEXING
print("indeks ke -1 = " + fullname[-1])
print("indeks dari 0-3 = " + fullname[0:4])
print("indeks dari 3-7 = " + fullname[3:8])  # ditambahin 1 di akhirnya 7+1 = 8
print("indeks dari 0, 2, 4, 6, 8, 10 = " + fullname[0:11:2])

# URUTAN (UNTUK STRING SESUAI ASCII)
print("urutan paling kecil = " + min(fullname))
print("urutan paling besar = " + max(fullname))

data = 117
print("ASCII 117 adalah = " + chr(data))
print("\n")

# OPERASI DALAM BENTUK METHOD
banyaknyaM = fullname.count("m")
print("banyaknya m pada fullname adalah = " + str(banyaknyaM))
print("\n")

# MENGUBAH SEMUA KE UPPERCASE ATAU LOWERCASE
coba = "testing"
print("normal       = " + coba)
print("uppercase    = " + coba.upper())
cobain = "TESTING"
print("normal       = " + cobain)
print("lowercase    = " + cobain.lower())


# PENGECEKAN isX METHOD 
mantap = "mantap"
mantappu = "Mantap"
print("\n", mantap.islower(), mantappu.islower())
# isalpha() = mengecek semuanya alfabet
# isdecimal() = mengecek semuanya angka
# isalnum() = mengecek angka dan huruf
# istitle() = semua kata dimulai dengan huruf besar
# isspace() = spasi, tab, newline

# startswith() endswith() mulai dengan/akhiri dengan
# join() menggabungkan
# split() memisahkan

pisah = ["tes", "satu", "dua", "tiga"]
print(pisah)

gabungan = "tes.satu.dua.tiga"
pisahan = gabungan.split(".")
print(pisahan)

# rjust() ljust() center() alokasi karakter
#strip menghilangkan efek dari rjust() ljust() center()
