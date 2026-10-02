# Laporan Advanced Git dan GitHub Variant A

## Lingkup dan status submission

Lima tugas Variant A dan Final Challenge sudah dijalankan pada repository latihan yang dibuat untuk tugas ini. Dokumen sumber tidak menyediakan URL repository maupun implementasi bug, sehingga fixture e-commerce dibuat untuk mereproduksi seluruh skenario. Identitas commit `DevOps Lab Student <student@example.invalid>` adalah identitas latihan, bukan identitas mahasiswa. Seluruh hash di bawah berasal dari eksekusi Git aktual.

**Status:** kode, tes, workflow, riwayat Git, konflik, bisect, revert, rebase, cherry-pick, dan tag telah diverifikasi lokal. Clone dan push pada bukti menggunakan bare remote lokal. Publikasi GitHub, Pull Request, merge melalui GitHub, proteksi branch, serta screenshot GitHub Actions belum dilakukan. Gambar di laporan adalah visualisasi transkrip asli, bukan screenshot desktop. Submission belum memenuhi seluruh persyaratan bukti GitHub sampai langkah pada `GITHUB_SUBMISSION.md` dilengkapi.

## Task 1 Emergency Production Hotfix

Bug awal menjumlahkan harga dan jumlah barang. `19.99` dengan quantity `3` menghasilkan `22.99`, padahal seharusnya `59.97`. Tes regresi mereproduksi kegagalan sebelum perbaikan dan lulus sesudah operator diganti menjadi perkalian. Decimal menjaga perhitungan uang dan pembulatan dua desimal.

Hotfix commit: `39250ce42533a581b732c294d62a0d7ed2028def`. Branch `hotfix/payment-bug` dibuat dari `main`, didorong ke remote lokal, lalu digabung ke main menggunakan merge commit. Tag `v1.0.1` menunjuk release hotfix pada main. Perbaikan juga disinkronkan ke `develop` dengan `git merge main`. File `src/new_checkout.py` yang belum selesai tetap hanya terdapat pada develop.

Branch harus dibuat dari main karena main mewakili kode produksi. Jika dibuat dari develop, perubahan fitur yang belum selesai dapat ikut masuk produksi, memperluas perubahan darurat, dan menambah risiko regresi. PR menuju main di GitHub masih memerlukan repository tujuan; merge lokal di bawah tidak diklaim sebagai PR GitHub.

![Actual local command output task1-hotfix part 1](evidence/task1-hotfix-01.png)

![Actual local command output task1-hotfix part 2](evidence/task1-hotfix-02.png)

![Actual local command output task1-hotfix part 3](evidence/task1-hotfix-03.png)

![Actual local command output task1-hotfix part 4](evidence/task1-hotfix-04.png)

![Actual local command output task1-hotfix part 5](evidence/task1-hotfix-05.png)

## Task 2 Complex Merge Conflict

Developer A pada `feature/password-policy` menetapkan minimum 12 karakter dan angka wajib. Developer B pada `feature/security-rules` menetapkan minimum 16 karakter dan simbol wajib. Merge kedua branch benar-benar menghasilkan konflik pada file yang sama. `git status` dan `git diff` digunakan untuk membaca keadaan merge sebelum file diselesaikan.

Konfigurasi akhir adalah `minimum_password_length = 16`, `require_numbers = True`, dan `require_symbols = True`. Minimum 16 memenuhi kedua batas minimum; angka dan simbol mempertahankan persyaratan masing-masing developer. File adalah Python sehingga boolean memakai `True`, setara dengan `true` pada pseudocode tugas. Tes memeriksa ketiga nilai, lalu penyelesaian dikomit setelah `git add`.

![Actual local command output task2-conflict part 1](evidence/task2-conflict-01.png)

![Actual local command output task2-conflict part 2](evidence/task2-conflict-02.png)

![Actual local command output task2-conflict part 3](evidence/task2-conflict-03.png)

## Task 3 Git Forensics

`git log --oneline`, `git show`, dan `git diff` digunakan untuk investigasi. `git bisect start`, `git bisect bad`, `git bisect good 78e6b7e181dadb7430fadf187ff6b9cc378ebae2`, dan `git bisect run` menjalankan tes otomatis untuk menemukan commit pertama yang merusak autentikasi.

- Bad commit: `dc479613366627aa33cba8463cf40febe3617eaa`.
- Author dan date: tercatat verbatim pada output `git show --format=fuller` di bawah.
- Changed files: `src/auth.py`.
- Problem: pembanding `==` diganti `!=`; password benar ditolak dan password salah diterima.
- Recommended solution: pulihkan perbandingan equality dan pertahankan tes valid user, wrong password, serta unknown user.
- Bonus: `git revert dc479613366627aa33cba8463cf40febe3617eaa` dijalankan setelah `git bisect reset`. Revert mencatat pembatalan dalam commit baru tanpa menghapus commit audit yang lebih baru. Tag `lab/auth-first-bad` dan `lab/auth-recovered` menyimpan titik bukti pada branch `lab/auth-forensics`.

![Actual local command output task3-forensics part 1](evidence/task3-forensics-01.png)

![Actual local command output task3-forensics part 2](evidence/task3-forensics-02.png)

![Actual local command output task3-forensics part 3](evidence/task3-forensics-03.png)

![Actual local command output task3-forensics part 4](evidence/task3-forensics-04.png)

![Actual local command output task3-forensics part 5](evidence/task3-forensics-05.png)

## Task 4 Rebase and Clean History

Branch `feature/payment` berisi tiga commit dokumentasi ketika main mendapat dua commit baru. Branch feature didorong dahulu agar perubahan hash setelah rebase dapat diperiksa. Setelah `git fetch origin`, `git rebase main` menerapkan ulang tiga commit di atas main terbaru. `git merge-base --is-ancestor main feature/payment` memverifikasi bahwa main adalah ancestor hasil rebase. Tidak terjadi konflik pada rebase ini karena perubahan berada pada file terpisah.

Merge mempertahankan identitas commit lama dan, ketika branch divergen, menghasilkan merge commit dengan dua parent. Rebase menerapkan ulang commit feature di atas base baru; parent dan hash commit berubah dan riwayat menjadi linear. Karena branch sudah dipush sebelum rebase, pembaruan menggunakan `git push --force-with-lease` terhadap remote lokal. Opsi ini memeriksa apakah tip remote masih sesuai nilai yang diharapkan, sehingga tidak menimpa pembaruan rekan yang belum diketahui. `--force` tidak melakukan pemeriksaan lease. Hindari rebase branch bersama tanpa koordinasi; background fetch juga dapat memperbarui nilai remote-tracking yang dipakai lease default.

![Actual local command output task4-rebase part 1](evidence/task4-rebase-01.png)

![Actual local command output task4-rebase part 2](evidence/task4-rebase-02.png)

![Actual local command output task4-rebase part 3](evidence/task4-rebase-03.png)

![Actual local command output task4-rebase part 4](evidence/task4-rebase-04.png)

## Task 5 GitHub CI Pipeline

`.github/workflows/test.yml` merespons PR opened, synchronize, reopened, dan ready_for_review menuju main atau develop; push ke kedua branch dan workflow_dispatch juga didukung. Job `build-test-security` checkout repository, menyiapkan Python 3.12, memasang requirements, memeriksa build melalui compileall, menjalankan unittest, lalu menjalankan pemeriksaan keamanan AST lokal. Requirements kosong secara sengaja karena aplikasi dan tes hanya memakai standard library.

Bonus security check mendeteksi panggilan langsung eval/exec, pickle.load/loads, os.system, dan shell=True di src. Ini pemeriksaan sempit untuk fixture, bukan pemindai kerentanan lengkap; alias import dan pola dinamis tidak seluruhnya tercakup. Exit nonzero pada build, tes, atau security check menggagalkan job.

Workflow saja tidak melarang tombol merge. Untuk memenuhi kriteria prevent merging when tests fail, aktifkan aturan proteksi main dan develop dengan Require a pull request before merging, Require status checks to pass, pilih `build-test-security`, Require branches to be up to date, serta larang bypass dan force push. Aturan perlu diterapkan di GitHub setelah job pertama terdaftar. Status penerapan saat ini: belum diterapkan karena repository GitHub belum tersedia.

Pemeriksaan setara job dijalankan lokal dan lulus. Ini bukan bukti run GitHub Actions; screenshot dan URL run harus ditambahkan setelah publikasi.

![Actual local command output task5-ci part 1](evidence/task5-ci-01.png)

## Final Challenge Both Variants

Final Challenge disertakan karena berlaku untuk kedua varian, tanpa mengerjakan Task 1 sampai 5 Variant B. Commit buruk sudah diidentifikasi dengan bisect dan dibatalkan dengan revert pada Task 3. Dua branch baru `feature-A` dan `feature-B` menimbulkan konflik release_config. Main berubah saat fitur berlangsung, lalu kedua feature direbase ke main terbaru.

Commit receipt helper `cfe3e212da0c51dd8cff1df4a1a0d1efeff0cca2` dibuat pada branch yang salah. `git cherry-pick` menyalin perubahan ke feature-A dan `git revert` membatalkannya pada feature-B. Ini memindahkan perubahan secara semantik tanpa menghapus sejarah. Merge final mempertahankan `retry_limit = 5` dan `enable_receipts = True`; tes memverifikasi gabungan konfigurasi dan receipt. Tag `lab/final-release` menandai hasil yang lulus tes lokal. Merge lokal memperagakan integrasi; sebelum merge PR di GitHub, status CI wajib lulus sesuai aturan proteksi.

Perintah dipilih sesuai tujuan: merge untuk integrasi, rebase untuk perubahan base, bisect untuk isolasi regresi, cherry-pick untuk memindahkan perubahan, revert untuk pembatalan yang menjaga sejarah, dan tag untuk release. Reset, reflog, dan stash tidak dibutuhkan pada skenario ini.

![Actual local command output final-challenge part 1](evidence/final-challenge-01.png)

![Actual local command output final-challenge part 2](evidence/final-challenge-02.png)

![Actual local command output final-challenge part 3](evidence/final-challenge-03.png)

![Actual local command output final-challenge part 4](evidence/final-challenge-04.png)

![Actual local command output final-challenge part 5](evidence/final-challenge-05.png)

## Verifikasi riwayat dan branch

![Actual local command output verification part 1](evidence/verification-01.png)

![Actual local command output verification part 2](evidence/verification-02.png)

![Actual local command output verification part 3](evidence/verification-03.png)

## Bukti GitHub yang harus dilengkapi

1. URL repository GitHub dan identitas mahasiswa atau tim yang benar.
2. Screenshot history dan daftar branch pada repository GitHub.
3. URL dan screenshot PR hotfix ke main serta status merged.
4. Screenshot run GitHub Actions berhasil beserta commit yang diuji.
5. Screenshot PR dengan tes gagal dan merge diblokir oleh required check.
6. Screenshot konfigurasi proteksi branch dan required check.

Jangan mengganti bagian ini dengan hasil simulasi. Langkah publikasi dan pembuatan PR demonstrasi tersedia di `GITHUB_SUBMISSION.md`; bukti baru harus berasal dari GitHub yang sebenarnya. Untuk mempertahankan PR historis hotfix yang sudah digabung lokal, gunakan replay ke repository GitHub baru sebagaimana dijelaskan dalam panduan tersebut.

## Referensi teknis

- [Git bisect](https://git-scm.com/docs/git-bisect)
- [Git rebase](https://git-scm.com/docs/git-rebase)
- [Git push dan force with lease](https://git-scm.com/docs/git-push)
- [GitHub protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)
- [GitHub status checks](https://docs.github.com/en/pull-requests/reference/status-checks)
