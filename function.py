def pangkat(angka1, angka2):
    hasilPangkat = angka1**angka2
    return hasilPangkat


mantap = 2
oke = 3
printPangkat = pangkat(mantap, oke)
print(printPangkat)

#! FUNGSI DENGAN RETURN BANYAK


def operasi(angka1, angka2):
    a = angka1 + angka2
    b = angka1 - angka2
    c = angka1 * angka2
    d = angka1 / angka2
    return a, b, c, d


w = operasi(mantap, oke)
print(w)

x, y, z, m = operasi(mantap, oke)
print(x, m, z, y)

#! FUNGSI DEFAULT ARGUMENT


def fungsi(input1=12, input2=5):
    keren = input1 + input2
    return keren


print(fungsi(2))
print(fungsi())
print(fungsi(input2=8))


#! FUNGSI DENGAN TYPE HINTS
def typehints(parameter: int) -> str:
    parameter *= 2
    return parameter


x = typehints(12.2)
print(x)
