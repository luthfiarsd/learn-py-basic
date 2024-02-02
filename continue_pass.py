# PASS -> SEBAGAI DUMMY, TIDAK AKAN DIEKSEKUSI

# CONTINUE -> NGECUT CODE DI BAWAHNYA, MELONCAT KE ITERASI SELANJUTNYA
angka = 0
while angka < 5:
    angka += 1
    if angka == 3:
        continue
    print(angka)

print()
# BREAK -> KELUAR DARI LOOPING
number = 0
while number < 10:
    print(number)
    number += 2
    if number == 6:
        break
