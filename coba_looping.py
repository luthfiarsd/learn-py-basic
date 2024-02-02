# LOOPING DENGAN LIST
angka = [0, 1, 2, 3, 4]

for i in angka:
    print("I sekarang adalah : " + str(i))

print()

# LOOPING DENGAN RANGE
for j in range(1, 10):
    print("J sekarang adalah : " + str(j))

print()

# LOOPING DENGAN STRING
mantap = "MANTAP"
for huruf in mantap:
    print(huruf)

print()

# WHILE LOOP
kondisi = False
incr = 0

while kondisi == False:
    print(incr)
    if incr == 5:
        kondisi = True
    incr += 1
