deret = [2, 4, 2, 3, 2, 3, 2, 2, 5, 6, 6, 7]

print("Indeks angka 2 dalam deret = ", end="")

banyak = 0
for i in range(len(deret)):
    if deret[i] == 2:
        print(i, end=" ")
        banyak += 1

print()
print("Banyaknya angka 2 = ", banyak)

deret.sort()
print(deret)
