list_mahasiswa = {}

i = 1
while True:
    nama = input(f"Masukkan mahasiswa ke-{i}: ")
    nilai_input = input("Masukkan nilai: ")
    nilai = list(map(int, nilai_input.split()))

    list_mahasiswa[f"mahasiswa-{i}"] = nama
    list_mahasiswa[f"nilaiMahasiswa-{i}"] = nilai

    isCont = input("Lanjut? (y/n)\n")
    if isCont == "n":
        break
    i += 1

print(list_mahasiswa)
