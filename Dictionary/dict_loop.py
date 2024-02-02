data_dict = {"key": "value", "hey": "mantap", "tes": 123}

# BERBEDA DENGAN LOOPING PADA LIST, INI HANYA MENGAMBIL KEYNYA SAJA
for data in data_dict:
    print(data)
print()

# GUNAKAN INI UNTUK MENGAKSES DICT
# OPERATOR UNTUK MENGAMBIL ITERABLES/KEY
for key in data_dict.keys():
    print(key, end=" ")
    print(data_dict[key])

# OPERATOR UNTUK MENGAMBIL VALUESNYA
for value in data_dict.values():
    print(value)

# OPERATOR UNTUK MENGAMBIL ITEMS (KEY BESERTA VALUENYA)
for item in data_dict.items():
    print(item)

for key, value in data_dict.items():
    print(key, value)
