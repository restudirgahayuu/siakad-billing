
import pytest

from siakad_billing.billing import hitung_tagihan


def test_hitung_tagihan_normal():
    assert hitung_tagihan(3, 100000) == 300000


def test_hitung_tagihan_nol():
    assert hitung_tagihan(0, 100000) == 0


def test_jumlah_negatif():
    with pytest.raises(ValueError):
        hitung_tagihan(-1, 100000)


def test_biaya_negatif():
    with pytest.raises(ValueError):
        hitung_tagihan(2, -100000)
