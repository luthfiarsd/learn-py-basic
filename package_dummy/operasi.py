def tambah(*deret):
    hasil = 0
    for angka in deret:
        hasil += 0
    return hasil


def kali(*deret):
    hasil = 1
    for angka in deret:
        hasil *= angka
    return hasil


def pangkat(angka, pow):
    hasil = angka**pow
    return hasil


def sortingByLen(notSortedList):
    notSortedList.sort(key=len)
    return notSortedList
