# DICT SEPERTI LIST, TETAPI INDEXING MEMAKAI KEY

data_dict = {"key": "value", "hey": "mantap", "tes": 123}
print(data_dict)
print(data_dict["hey"])

# PANJANG DICTIONARY
data_dict_length = len(data_dict)
print(data_dict_length)

# MENGECEK KEY SAJA
value = "hey"
checkValue = value in data_dict
print(checkValue)

# MENGAKSES VALUE DENGAN GET
print(data_dict.get("tes"))

# MENGUPDATE / MENAMBAH DATA
data_dict["tes"] = 666
data_dict["baru"] = "ini data baru"
print(data_dict)

# DELETE DATA
del data_dict["tes"]
print(data_dict)
