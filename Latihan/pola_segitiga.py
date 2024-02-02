for i in range(5, 0, -1):
    print(" " * (5 - i), end="") # end= -> parameter agar tidak pindah ke line selanjutnya
    for x in range(i):
        print("+ ", end="")
    print()
