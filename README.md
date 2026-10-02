# Advanced Git and GitHub Variant A

Submission ini mengerjakan Task 1 sampai Task 5 Variant A serta Final Challenge yang berlaku untuk kedua varian. Contoh aplikasi e-commerce menggunakan Python 3.12 dan standard library. Variant B tidak dikerjakan.

## Jalankan pemeriksaan

```bash
python -m pip install -r requirements-dev.txt
python -m compileall -q src tests
python -m unittest discover -s tests -v
python scripts/security_check.py
```

## Isi repository

- `src/`: kalkulasi pembayaran, fixture autentikasi, kebijakan password, dan fitur receipt.
- `tests/`: tes pembayaran, autentikasi, konfigurasi hasil konflik, dan receipt.
- `.github/workflows/test.yml`: build, test, dan security check untuk setiap PR.
- `REPORT.md`: keputusan, commit aktual, perintah, dan bukti eksekusi lokal.
- `evidence/`: transkrip asli dan gambar hasil perintah lokal.
- `GITHUB_SUBMISSION.md`: langkah publikasi serta bukti GitHub yang masih harus dilengkapi.

## Riwayat Git

Repository lokal menyimpan seluruh branch dan tag latihan. ZIP juga memuat `variant-a-history.bundle`; clone bundle untuk mengembalikan riwayat jika folder `.git` tidak disertakan oleh platform pengiriman:

```bash
git clone variant-a-history.bundle restored-variant-a
cd restored-variant-a
git branch -a
git log --graph --oneline --all --decorate
```

Remote `origin` pada pengerjaan lokal adalah bare repository lokal, bukan GitHub. Autentikasi dalam `src/auth.py` hanya fixture pendidikan dan tidak layak digunakan sebagai autentikasi produksi karena memakai password plaintext.
