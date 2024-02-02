# 1. UNTUK MENYAMBUNG PROGRAM MENGAMBIL DARI EKSTERNAL
import import_dummy1

# 2. IMPORT DENGAN DATA
import import_dummy2

print(import_dummy2.data)
# IMPORT DENGAN OPERASI DSB
import import_dummy3

tes = import_dummy3.pangkat(3.1, 2)
print(tes)

# MODULE IMPORT DENGAN FROM
from import_dummy3 import tambah

teslagi = tambah(2, 3, 4, 7, 11, 1000)
print(teslagi)

# ALIAS FROM
from import_dummy3 import tambah as cokk

teslagi2 = cokk(11, 2, 2, 311)
print(teslagi2)
