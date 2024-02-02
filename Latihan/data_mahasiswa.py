list_mahasiswa = []

while True:
    nama = input("Nama Mahasiswa\t: ")
    npm = input("NPM Mahasiswa\t: ")
    nilai_tugas = input("Nilai Tugas\t: ")
    nilai_kuis = input("Nilai Kuis\t: ")
    nilai_ujian = input("Nilai Ujian\t: ")

    mahasiswa = [nama, npm, nilai_tugas, nilai_kuis, nilai_ujian]
    list_mahasiswa.append(mahasiswa)
    print()
    isLanjut = input("Lanjut? (y/n) -> ")
    if isLanjut == "n":
        break
    print()

i = 1
for mahasiswa in list_mahasiswa:
    print(f"MAHASISWA {i}")
    print("Nama\t\t : ", mahasiswa[0])
    print("NPM\t\t : ", mahasiswa[1])
    print("Nilai Tugas\t : ", mahasiswa[2])
    print("Nilai Kuis\t : ", mahasiswa[3])
    print("Nilai Ujian\t : ", mahasiswa[4])
    print()
    i += 1
