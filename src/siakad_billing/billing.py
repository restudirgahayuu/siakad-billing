
def hitung_tagihan(jumlah: int, biaya_per_unit: int) -> int:
    if jumlah < 0:
        raise ValueError("Jumlah tidak boleh negatif")

    if biaya_per_unit < 0:
        raise ValueError("Biaya tidak boleh negatif")

    return jumlah * biaya_per_unit
