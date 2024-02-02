list_mahasiswa = [100, 22, "luthfi"]


def fungsi1(mantap):
    nama = mantap[2]
    umur = mantap[1]
    keren = mantap[0]
    print(f"nama saya {nama}, umur saya {umur}, kekerenenan {keren}")


fungsi1(list_mahasiswa)


#! args PADA FUNGSI
def fungsi2(*args):
    nama = args[2]
    umur = args[1]
    keren = args[0]
    print(f"nama saya {nama}, umur saya {umur}, kekerenenan {keren}")


fungsi2(22, 33, "andi")


#! STUDI KASUS
def tambah(*data):
    output = 0
    for angka in data:
        output += angka
    return output


x = tambah(1, 2, 3, 4, 4, 5, 6, 6)
print(x)


#! kwargs UNTUK DICTIONARY
def fungsi3(mantap):
    print(mantap)


fungsi3({"nama": "luthfi", "kelas": "kuliah"})


def fungsi4(**keren):
    nama = keren["nama"]
    kelas = keren["kelas"]
    return f"nama saya {nama}, kelas {kelas}"


a = fungsi4(nama="luthfi", kelas="kuliah")
print(a)
