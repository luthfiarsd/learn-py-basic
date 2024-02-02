inputUser = int(input("Masukkan nilai : "))
cekUser = (
    ((inputUser >= 0) and (inputUser <= 5)) or (inputUser >= 8) and (inputUser <= 10)
)
print(cekUser, inputUser)
inputUser *= 3
print(inputUser)

b = 3
c = ~b

print("\nNilai b:", b, " dalam bntk binary:", format(b, "08b"))
print("---------------------------------------( ~ )")
print("Nilai c:", c, " dalam bntk binary:", format(c & 0xFF, "08b"))
