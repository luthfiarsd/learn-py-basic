data_dict = {"key": "value", "hey": "mantap", "tes": 123}

# COPY DICT
datacopy = data_dict.copy()

# POP DICT, MENTRANSFER KELUAR DARI DICT
dataHey = data_dict.pop("hey")
print(dataHey)
print(data_dict)

# POPITEM, MENTRANSFER KELUAR DATA TERAKHIR DARI DICT
dataTerakhir = datacopy.popitem()
print(dataTerakhir)
print(datacopy)

# FROMKEY, BUAT DICTIONARY KOSONG DENGAN KEY YANG SUDAH ADA
mahasiswa_template = {
    'nama' : 'nama',
    'npm' : '0000000',
    'sks_lulus' : 0,
}
mahasiswa = dict.fromkeys(mahasiswa_template.keys())
print(mahasiswa)