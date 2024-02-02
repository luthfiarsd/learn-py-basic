# MEMBUKA FILE MODE WRITE OVERWRITE (MENGHAPUS ISI FILE, LALU DIGANTI YANG BARU)
file = open("b.txt", mode="w")

# WRITE METODE OVERWRITE
file.write("Mantap")

# CLOSE FILE
file.close()

# MEMBUKA FILE MODE WRITE APPEND (MENAMBAHKAN ISI FILE)
file = open("c.txt", mode="a")

# WRITE MODE APPEND
file.write("WADAW\n")
file.close()

# MEMBUKA FILE MODE MENIMPA (TIDAK OVERWRITE SELURUH FILE)
file = open("c.txt", mode="r+")
file.write("WOW")
file.write("mantap")
file.close()
