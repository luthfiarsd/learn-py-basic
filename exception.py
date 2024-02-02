# EXCEPTION, SEBAGAI CODE YANG RUNNING KETIKA RUNTIME ERROR
# syntax try: except:

# CODE
while True:
    angka = int(input("Masukkan angka pembagi : "))
    try:
        hasil = 100 / angka
        print(hasil)

        isContinue = input("Apakah ingin melanjutkan? (y/n)")
        if isContinue == "n":
            break

    except:
        print("Error! Masukkan selain angka tersebut")
        break

# CRUD
try:
    file = open("data.txt", mode="r")
    print(file.read())
except:
    print("File tidak ditemukan, membuat file baru")
    file = open("exception.txt", mode="a")
    file.write("Anjay mabar")
