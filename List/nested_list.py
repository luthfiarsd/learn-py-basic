orang1 = ["Alif", 25, "Laki-laki"]
orang2 = ["Dewi", 28, "Perempuan"]
data_2d = [orang1, orang2]
print(data_2d)

for orang in data_2d:
    print("Nama             : ", orang[0])
    print("Umur             : ", orang[1])
    print("Jenis Kelamin    : ", orang[2])
    print()

# MENGAMBIL DATA DARI NESTED LIST
data = data_2d[0][2]
print(data)

# MELAKUKAN DEEP COPY PADA NESTED LIST
from copy import deepcopy

data_2d_deepcopy = deepcopy(data_2d)
data_2d_deepcopy[0][1] = 19
print(data_2d_deepcopy)
print("list awal : ", data_2d)
print()
for orang in data_2d_deepcopy:
    print("Nama             : ", orang[0])
    print("Umur             : ", orang[1])
    print("Jenis Kelamin    : ", orang[2])
    print()
