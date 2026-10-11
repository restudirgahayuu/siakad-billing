# SIAKAD Billing

Proyek latihan modul billing SIAKAD menggunakan Python. Proyek ini menerapkan pengelolaan dependensi dengan uv, konfigurasi environment menggunakan Pydantic Settings, dan unit testing menggunakan pytest.

## 1. Persyaratan

- Python 3.11 atau lebih baru
- Git
- uv

## 2. Instalasi

Clone repository:

```powershell
git clone URL_REPOSITORY
cd siakad-billing
```

Pasang dependensi:

```powershell
uv sync
```

## 3. Konfigurasi Environment

Salin file template:

```powershell
Copy-Item .env.example .env
```

Sesuaikan nilai konfigurasi pada `.env` jika diperlukan.

## 4. Menjalankan Unit Test

Jalankan pengujian otomatis:

```powershell
uv run pytest -v
```

Pengujian mencakup perhitungan tagihan normal, jumlah nol, jumlah negatif, dan biaya negatif.

## 5. Struktur Proyek

- `src/siakad_billing/`: kode program.
- `tests/`: unit test.
- `config.py`: konfigurasi aplikasi.
- `.env.example`: template konfigurasi.
- `pyproject.toml`: metadata dan dependensi proyek.
- `uv.lock`: lockfile dependensi.

## 6. Keamanan

File `.env` dan `.venv` tidak boleh diunggah ke repository. Gunakan `.env.example` sebagai template konfigurasi yang dapat dibagikan.