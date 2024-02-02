# LIST COMPREHENSION
data = ["tes", 1, 6, 7, 3, "abcd", "anqnpsda6"]

[print(i, end=" ") for i in data]
print()

angka = [5, 2, 4, 2, 1, 8, 6, 2, 9]
angka_kuadrat = [i**2 for i in angka]
print(angka_kuadrat)

# ENUMERATE
data_list = data.copy()
for index, data in enumerate(data_list):
    print(index, data)
