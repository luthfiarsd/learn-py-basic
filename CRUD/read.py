# MEMBUKA FILE UNTUK MODE READ
file = open("CRUD/a.txt", mode="r")

# MEMBACA SEMUANYA
# print(file.read())

# MEMBACA PER BARIS
print(file.readline(), end="")

# MEMBACA SEMUA BARIS LALU MENJADIKAN LIST
TextContainer = file.readlines()  # SINTAKS READ UTAMA

textClean = []
i = 0
for text in TextContainer:
    textClean.append(text.strip())

print(textClean)

# MENUTUP FILE
file.close()
print()

# METODE KEDUA YAITU DENGAN MENGGUNAKAN with
with open("CRUD/a.txt", mode="r") as file:
    content = file.read()
    print(content)
    file.closed
file.closed
