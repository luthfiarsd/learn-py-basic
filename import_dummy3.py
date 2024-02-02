def pangkat(angka: float, pow: int) -> float:
    hasil = angka**pow
    return hasil

def tambah(*deret):
    hasil = 0
    for angka in deret:
        hasil += angka
    return hasil
