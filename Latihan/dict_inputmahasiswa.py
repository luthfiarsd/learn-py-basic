import os

dict_mahasiswa = {}
i = 1
while True:
    os.system("cls")
    print(f"{"FORM INPUT MAHASISWA":^40}")
    print("-"*40)
    print()
    
    mahasiswa = {}
    print(f"Mahasiswa {i}")
    nama = input("Nama Mahasiswa\t: ")
    npm = input("NPM\t\t: ")
    sks = int(input("Banyaknya SKS\t: "))

    mahasiswa["nama"] = nama
    mahasiswa["npm"] = npm
    mahasiswa["sks"] = sks

    dict_mahasiswa[f"MHS-{i}"] = mahasiswa

    isLanjut = input("Lanjutkan? (y/n)")
    i += 1
    print()
    if isLanjut == "n":
        break

print(f"{'INDEX':<8} | {'NAMA':<20} | {'NPM':<8} | {'SKS':<3}")
print("-"*48)
for mhs, info_mhs in dict_mahasiswa.items():
    namaMhs = info_mhs["nama"]
    npmMhs = info_mhs["npm"]
    sksMhs = info_mhs["sks"]

    print(f"{mhs:<11}{namaMhs:<23}{npmMhs:11}{sksMhs:<5}")

print("\nDatabase;", dict_mahasiswa)
