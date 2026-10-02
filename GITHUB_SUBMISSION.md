# Publikasi dan bukti submission GitHub

## Status

Paket ini sudah diverifikasi lokal. URL dan akses repository GitHub belum diberikan. Jangan menyerahkan sebagai submission lengkap sebelum PR, Actions, dan proteksi branch nyata dilengkapi. Gunakan repository GitHub baru yang kosong agar tidak menimpa pekerjaan lain.

## Publikasi dengan riwayat lengkap

Setelah membuat repository kosong di GitHub, gunakan URL yang benar:

```bash
git remote add github https://github.com/USERNAME/REPOSITORY.git
git push github --all
git push github --tags
```

Jangan menggunakan `git push --mirror` atau force terhadap repository yang berisi pekerjaan lain. Publikasi ini mempertahankan semua riwayat lokal, tetapi hotfix sudah terdapat di main sehingga GitHub tidak bisa membuat PR baru dengan diff hotfix yang sama. Untuk bukti PR hotfix historis yang sesungguhnya, lakukan replay pada repository kosong sebelum push main final.

## Replay PR hotfix pada repository kosong

Clone bundle ke folder latihan baru, gunakan remote GitHub kosong sebagai origin. Publikasikan main pada titik sebelum hotfix tanpa menulis ulang main lokal hasil final:

```bash
git remote set-url origin https://github.com/USERNAME/REPOSITORY.git
git push origin lab/production-before-hotfix:refs/heads/main
git push origin hotfix/payment-bug
```

Di GitHub, buat PR `hotfix/payment-bug` ke `main`. Tunggu CI lulus. Baseline main sengaja memiliki bug; pengujian baseline boleh gagal, sedangkan PR hotfix harus lulus. Catat URL dan ambil screenshot PR serta hasil job. Setelah job terdaftar, aktifkan required status check `build-test-security` pada main, wajibkan PR dan branch terbaru, dan larang bypass/force push. Untuk tugas solo, required approving review hanya diaktifkan bila ada rekan reviewer; penulis PR tidak bisa menyetujui PR sendiri.

Merge PR menggunakan **Create a merge commit**, bukan squash/rebase. SHA merge GitHub akan berbeda dari merge lokal, jadi catat SHA GitHub dalam REPORT. Buat tag release GitHub `v1.0.1` pada merge PR tersebut; tag lokal yang sudah ada menunjuk merge lokal, sehingga jangan push tag lokal v1.0.1 bila melakukan replay ini.

Untuk mengintegrasikan hasil latihan final tanpa force pada main yang diproteksi, fetch main GitHub lalu buat branch integrasi dari main lokal final. Merge `origin/main` ke branch itu untuk menyatukan kedua riwayat. Push branch integrasi dan buat PR ke main; tunggu CI lulus lalu merge. Periksa setiap konflik sebelum menyelesaikannya. Branch dan tag bukti lain boleh dipush secara eksplisit. Develop dari latihan sudah mencakup hotfix; dapat dipush jika target develop belum ada.

## Bukti merge diblokir ketika tes gagal

Buat branch demonstrasi dari main GitHub terbaru. Ubah operator pembayaran `value * quantity` menjadi `value + quantity`, commit, push, dan buat PR ke main. Tunggu job gagal lalu ambil screenshot status failed dan merge diblokir. Jangan merge branch demonstrasi tersebut. Pulihkan operator pada branch PR dan push lagi, lalu ambil screenshot job berhasil. PR boleh ditutup setelah bukti lengkap.

## Screenshot yang perlu dimasukkan ke REPORT

Simpan bukti asli di `evidence/github/` dan tambahkan link Markdown ke REPORT untuk history, branches, PR hotfix merged, Actions sukses, PR gagal yang diblokir, dan aturan proteksi branch. Cantumkan URL PR/run dan SHA yang bersangkutan. Gambar transkrip lokal yang sudah ada menjelaskan konflik serta perintah; jika pengajar mensyaratkan screenshot terminal, jalankan kembali perintah history dan gunakan screenshot terminal asli.

## Identitas dan checklist terakhir

Tambahkan nama dan student ID pada REPORT. Identitas commit latihan tidak boleh dianggap sebagai identitas asli. Pastikan README, src, tests, test.yml, REPORT tersedia di default branch dan seluruh tautan bukti terbuka. Jalankan tes sekali lagi sesudah perubahan publikasi. Jangan mencantumkan token, password, atau secret dalam screenshot.
