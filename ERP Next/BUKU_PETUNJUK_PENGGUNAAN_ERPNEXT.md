# BUKU PETUNJUK PENGGUNAAN SISTEM ERPNEXT LOCALHOST
## PANDUAN LENGKAP PENGOPERASIAN MODUL MANUFAKTUR, LOGISTIK, PENJUALAN & AKUNTANSI
### Studi Kasus: Meli Dwi Company (MDC) - Produksi Meja Belajar Kayu Minimalis

**Penyusun:** Meli Dwi A (`melidwyy@gmail.com`)  
**Mata Kuliah:** Enterprise Resource Planning (ERP) - Semester 7  
**Alamat Sistem:** [http://localhost:8080](http://localhost:8080)  
**Versi ERP:** ERPNext v16 (Frappe Framework) on Docker Compose  

---

## DAFTAR ISI
1. **BAB I: PENGANTAR SISTEM & ARSITEKTUR LOCALHOST**
   * 1.1 Mengenal ERPNext & Docker Stack
   * 1.2 Cara Menjalankan, Memeriksa, dan Mematikan Server
   * 1.3 Akses URL dan Kredensial Login
2. **BAB II: NAVIGASI ANTARMUKA PENGGUNA (DESK NAVIGATION)**
   * 2.1 Bilah Pencarian Utama (*Awesome Bar*)
   * 2.2 Bilah Sisi (*Sidebar*) dan Ruang Kerja (*Workspaces*)
   * 2.3 Tampilan Data: Daftar (*List View*), Formulir (*Form View*), dan Laporan (*Report View*)
3. **BAB III: PANDUAN PENGOPERASIAN PER MODUL OPERASIONAL**
   * 3.1 Modul Stok (*Stock*) - Manajemen Item & Gudang
   * 3.2 Modul Pengadaan (*Buying*) - Permintaan Material, Penawaran & Pembelian
   * 3.3 Modul Manufaktur (*Manufacturing*) - Formula BOM & Perintah Produksi
   * 3.4 Modul Penjualan (*Selling*) - Penawaran, Order Penjualan & Pengiriman
   * 3.5 Modul Aset Tetap (*Assets*) - Pencatatan & Kategori Mesin Pabrik
   * 3.6 Modul Akuntansi (*Accounts*) - Penagihan, Pembayaran Kas & Jurnal Otomatis
4. **BAB IV: CARA MENARIK & MENGUNDUH LAPORAN KEUANGAN / OPERASIONAL**
   * 4.1 Laporan Posisi Saldo Stok (*Stock Balance*)
   * 4.2 Laporan Laba Rugi (*Profit and Loss Statement*)
   * 4.3 Laporan Neraca (*Balance Sheet*)
   * 4.4 Cara Mencetak & Ekspor ke PDF / Excel
5. **BAB V: PANDUAN PENANGANAN MASALAH (TROUBLESHOOTING)**
   * 5.1 Penanganan Kontainer Berhenti / Lemot
   * 5.2 Masalah Batas Memori WSL2
   * 5.3 Reset File Kunci Wizard Setup

---

## BAB I: PENGANTAR SISTEM & ARSITEKTUR LOCALHOST

### 1.1 Mengenal ERPNext & Docker Stack
ERPNext dijalankan menggunakan containerization Docker di sistem operasi Windows (berbasis WSL2). Stack ini terdiri dari 9 layanan terintegrasi:
1. `frontend` (Nginx reverse proxy di port `8080:8080`).
2. `backend` (Aplikasi Python Gunicorn ERPNext v16).
3. `db` (Database MariaDB 11.8 penyimpanan data transaksi).
4. `redis-cache` (Penyimpanan memori sementara untuk kecepatan respons UI).
5. `redis-queue` (Antrean background job).
6. `queue-short` & `queue-long` (Worker pemroses laporan berat dan transaksi berantai).
7. `scheduler` (Pemroses tugas otomatis berkala).
8. `websocket` (Notifikasi instan real-time antarmuka pengguna).

### 1.2 Cara Menjalankan, Memeriksa, dan Mematikan Server
Buka terminal **PowerShell** pada direktori proyek (`ENTERPRISE RESOURCE PLANNING (ERP)`):

* **Menjalankan Server (Start):**
  ```powershell
  docker compose up -d
  ```
  *Tunggu 1–2 menit agar seluruh database dan web server selesai inisialisasi.*

* **Memeriksa Status Kontainer (Status Check):**
  ```powershell
  docker compose ps
  ```
  *Pastikan semua layanan berstatus `Up` atau `Up (healthy)`.*

* **Melihat Log Aplikasi (Jika terjadi kendala):**
  ```powershell
  docker compose logs -f frontend
  ```

* **Mematikan Server (Stop / Shutdown Aman):**
  ```powershell
  docker compose down
  ```
  *Catatan: Menjalankan `docker compose down` tidak akan menghapus data karena data tersimpan permanen di Docker Volumes (`db-data`, `sites`).*

### 1.3 Akses URL dan Kredensial Login
* **URL Browser:** Buka Google Chrome / Microsoft Edge, ketik:  
  **`http://localhost:8080`**
* **Username / ID Pengguna:** `Administrator`
* **Email:** `melidwyy@gmail.com`
* **Password:** *(Gunakan sandi akun administrator yang telah dikonfigurasi saat instalasi)*

---

## BAB II: NAVIGASI ANTARMUKA PENGGUNA (DESK NAVIGATION)

Antarmuka ERPNext dirancang modern dan terpusat (*Single-Page Application*):

### 2.1 Bilah Pencarian Utama (*Awesome Bar*)
* Terletak di bagian atas tengah layar.
* Berfungsi sebagai navigasi tercepat ke dokumen atau laporan mana pun.
* **Contoh penggunaan:**
  * Ketik `Stock Balance` lalu tekan **Enter** -> Langsung membuka Laporan Stok.
  * Ketik `Profit and Loss` lalu tekan **Enter** -> Langsung membuka Laporan Laba Rugi.
  * Ketik `BOM List` -> Membuka daftar resep produksi.
  * Ketik `New Sales Order` -> Langsung membuat pesanan penjualan baru.

### 2.2 Bilah Sisi (*Sidebar*) dan Ruang Kerja (*Workspaces*)
* **Home / Dashboard:** Menampilkan ringkasan ringkas performa bisnis.
* **Manufacturing:** Berisi BOM, Work Order, Job Card, dan Operasi Pabrik.
* **Stock:** Berisi Master Item, Gudang, Bukti Pengeluaran/Penerimaan Stok.
* **Buying:** Berisi Supplier, Permintaan Material, PO, dan Penerimaan Pembelian.
* **Selling:** Berisi Customer, Quotation, Sales Order, dan Surat Jalan.
* **Accounting:** Berisi Bagan Akun (Chart of Accounts), Invoice, Kas, dan Laporan Keuangan.
* **Assets:** Berisi daftar Aset Tetap, Nilai Perolehan, dan Penyusutan Mesin.

### 2.3 Status Dokumen di ERPNext
Setiap dokumen transaksi di ERPNext memiliki siklus status resmi:
1. **Draft (Status 0):** Dokumen baru dibuat dan dapat diedit secara bebas. Belum mempengaruhi stok atau jurnal keuangan.
2. **Submitted (Status 1):** Dokumen telah divalidasi resmi. Mengunci transaksi, mencatat jurnal buku besar otomatis, dan menggerakkan saldo stok.
3. **Cancelled (Status 2):** Dokumen dibatalkan resmi. Sistem membuat jurnal pembalik otomatis.

---

## BAB III: PANDUAN PENGOPERASIAN PER MODUL OPERASIONAL

### 3.1 Modul Stok (*Stock*)
#### A. Melihat Master Data Item
1. Ketik **Item List** pada Awesome Bar.
2. Anda akan melihat daftar item yang telah terdaftar:
   * `MB-001`: Meja Belajar Kayu Minimalis (Barang Jadi / Mantap).
   * `BB-001`: Papan Kayu Mahoni 120x60.
   * `BB-002`: Kaki Meja Besi Hollow.
   * `BB-003`: Baut & Sekrup Baja.
   * `BB-004`: Cat Vernis Wood Finish.
3. Klik salah satu item untuk melihat detail unit pengukuran (UOM), harga standar, dan saldo stok terkini.

#### B. Mengelola Gudang (*Warehouses*)
1. Ketik **Warehouse Tree** pada Awesome Bar.
2. Tiga gudang operasional perusahaan terletak di bawah cabang utama `Meli Dwi Company`:
   * `Gudang Bahan Baku - MDC`
   * `Gudang Work In Progress - MDC`
   * `Gudang Barang Jadi - MDC`

---

### 3.2 Modul Pengadaan (*Buying*)
#### A. Membuat Permintaan Material (*Material Request*)
* **Fungsi:** Bagian produksi meminta pengadaan bahan ke bagian pembelian.
* **Navigasi:** Masuk ke menu **Buying > Material Request > Add Material Request**.
* **Langkah:**
  1. Pilih *Purpose*: `Purchase`.
  2. Masukkan tanggal kebutuhan (*Required Date*).
  3. Masukkan item yang dibutuhkan dan kuantitasnya pada tabel *Items*.
  4. Klik tombol **Save**, kemudian klik **Submit**.

#### B. Membuat Pesanan Pembelian (*Purchase Order / PO*)
* **Fungsi:** Mengirim pesanan resmi ke pemasok.
* **Navigasi:** **Buying > Purchase Order > Add Purchase Order**.
* **Langkah:**
  1. Pilih *Supplier* (contoh: `CV Kayu Lestari Abadi`).
  2. Pada tabel item, masukkan item dan harga satuan yang disepakati.
  3. Pastikan gudang tujuan adalah `Gudang Bahan Baku - MDC`.
  4. Klik **Save** lalu **Submit**.

#### C. Menerima Fisik Bahan Baku (*Purchase Receipt*)
* **Fungsi:** Mencatat barang datang secara fisik ke gudang.
* **Langkah Cepat:**
  1. Buka dokumen PO yang telah berstatus *Submitted*.
  2. Klik tombol **Create > Receipt** di pojok kanan atas.
  3. Periksa kuantitas yang diterima secara fisik.
  4. Klik **Save** dan **Submit**.
  *Stok fisik di Gudang Bahan Baku akan langsung bertambah seketika.*

---

### 3.3 Modul Manufaktur (*Manufacturing*)
#### A. Melihat / Membuat Resep Produksi (*Bill of Materials / BOM*)
* **Dokumen Aktif:** `BOM-MB-001-001`
* **Navigasi:** **Manufacturing > Bill of Materials > BOM**.
* **Struktur Resep 1 Unit Meja Belajar (`MB-001`):**
  * 1 Papan Kayu Mahoni (`BB-001`) = Rp 120.000
  * 4 Kaki Meja Besi Hollow (`BB-002`) = Rp 180.000
  * 16 Baut & Sekrup Baja (`BB-003`) = Rp 24.000
  * 0.5 Liter Cat Vernis (`BB-004`) = Rp 24.500
  * **Total HPP Standar per unit:** **Rp 348.500,00**
* *Pastikan kolom "Is Active" dan "Is Default" tercentang.*

#### B. Menjalankan Perintah Kerja Produksi (*Work Order*)
* **Navigasi:** **Manufacturing > Work Order > Add Work Order**.
* **Langkah Operasi:**
  1. Pilih *Item to Produce*: `MB-001`.
  2. Sistem secara otomatis memanggil `BOM-MB-001-001`.
  3. Masukkan *Qty to Manufacture* (misal: `10`).
  4. Tentukan *Target Warehouse*: `Gudang Barang Jadi - MDC`.
  5. Tentukan *WIP Warehouse*: `Gudang Work In Progress - MDC`.
  6. Klik **Save** lalu **Submit**.
  7. **Tahap Transfer Bahan:** Klik tombol **Create > Start**. Simpan dan submit *Stock Entry (Material Transfer for Manufacture)*.
  8. **Tahap Penyelesaian Produksi:** Klik tombol **Create > Finish**. Simpan dan submit *Stock Entry (Manufacture)*.
  *Hasil: 10 unit meja belajar resmi bertambah di Gudang Barang Jadi, dan stok bahan mentah berkurang otomatis.*

---

### 3.4 Modul Penjualan (*Selling*)
#### A. Penawaran Harga Pelanggan (*Quotation*)
* **Navigasi:** **Selling > Quotation > Add Quotation**.
* Digunakan saat pelanggan (seperti *Yayasan Bina Prestasi Mandiri*) meminta estimasi harga meja sebelum menerbitkan pesanan pasti.

#### B. Pesanan Penjualan (*Sales Order*)
* **Navigasi:** **Selling > Sales Order**.
* **Dokumen yang telah dieksekusi:** `SAL-ORD-2026-00006` (Customer: *PT Graha Furniture Nusantara*, 5 unit @ Rp 550.000 = Rp 2.750.000).

#### C. Pengiriman Barang (*Delivery Note / Surat Jalan*)
* Dari Sales Order yang berstatus *To Deliver*, klik **Create > Delivery**.
* Nomor dokumen pengiriman: `MAT-DN-2026-00001`.
* Ketika disubmit, 5 meja dikeluarkan secara sah dari `Gudang Barang Jadi - MDC`.

#### D. Penerbitan Faktur Penjualan (*Sales Invoice*)
* Dari Delivery Note atau Sales Order, klik **Create > Invoice**.
* Dokumen Faktur: `ACC-SINV-2026-00006`.
* Menagihkan piutang ke pelanggan sebesar Rp 2.750.000.

---

### 3.5 Modul Manajemen Aset Tetap (*Assets*)
1. Ketik **Asset List** pada Awesome Bar.
2. Anda akan melihat 2 unit aset mesin operasional pabrik:
   * `ACC-ASS-2026-00001`: **Mesin Pemotong Kayu Serbaguna (Table Saw)** senilai **Rp 8.500.000,00**.
   * `ACC-ASS-2026-00002`: **Kompresor & Spray Gun Finishing Cat** senilai **Rp 3.200.000,00**.
3. Keduanya terdaftar pada Kategori `Mesin & Peralatan Pabrik` dengan lokasi fisik di `Pabrik Utama`.
4. Nilai aset ini otomatis masuk dan menambah kekayaan modal pada Neraca Perusahaan (*Balance Sheet*).

---

### 3.6 Modul Akuntansi & Penerimaan Kas (*Accounts*)
1. **Mencatat Kas Masuk Pelunasan Pelanggan:**
   * Buka Faktur Penjualan `ACC-SINV-2026-00006`.
   * Klik **Create > Payment**.
   * Dokumen Pembayaran `ACC-PAY-2026-00006` mencatatkan uang masuk sebesar **Rp 2.750.000,00** ke akun:  
     `1111.002 - Kas Besar - MDC`.
2. **Buku Besar (*General Ledger*):**
   * Ketik **General Ledger** di Awesome Bar untuk melihat aliran mutasi debit dan kredit secara kronologis dan real-time.

---

## BAB IV: CARA MENARIK & MENGUNDUH LAPORAN KEUANGAN / OPERASIONAL

### 4.1 Laporan Posisi Saldo Stok (*Stock Balance*)
1. Pada Awesome Bar, ketik: **Stock Balance** dan tekan Enter.
2. Pada filter atas, pilih:
   * **Company:** `Meli Dwi Company`
3. Layar akan menampilkan rincian barang:
   * `BB-001` di *Gudang Bahan Baku*: **20.0 Unit** (Nilai: Rp 2.360.000,00).
   * `MB-001` di *Gudang Barang Jadi*: **5.0 Unit** (Nilai: Rp 1.742.500,00).

### 4.2 Laporan Laba Rugi (*Profit and Loss Statement*)
1. Ketik **Profit and Loss Statement** pada Awesome Bar.
2. Pilih Company: `Meli Dwi Company`.
3. Tampilan laporan memperlihatkan:
   * **Income (Pendapatan):** Rp 2.750.000,00
   * **Cost of Goods Sold (HPP):** (Rp 1.742.500,00)
   * **Net Profit (Laba Bersih):** **Rp 1.007.500,00**

### 4.3 Laporan Neraca (*Balance Sheet*)
1. Ketik **Balance Sheet** pada Awesome Bar.
2. Tampilan laporan memperlihatkan:
   * Kas Besar: Rp 2.750.000,00
   * Persediaan Barang: Rp 4.102.500,00
   * Aktiva Tetap (Mesin & Peralatan): Rp 11.700.000,00
   * **Total Aset:** **Rp 18.552.500,00**

### 4.4 Cara Mencetak & Ekspor ke PDF / Excel
* Di setiap halaman laporan (Stock Balance, Laba Rugi, Neraca), terdapat ikon menu titik tiga (`...`) atau tombol **Actions** di pojok kanan atas.
* Klik **Export** -> Pilih format **Excel (.xlsx)** atau **CSV** untuk olah data tugas.
* Klik ikon **Print** -> Pilih orientasi landscape -> Klik **PDF** untuk mengunduh laporan berformat siap cetak.

---

## BAB V: PANDUAN PENANGANAN MASALAH (TROUBLESHOOTING)

### 5.1 Jika Web Browser Menampilkan "502 Bad Gateway" atau Tidak Bisa Dibuka
* **Penyebab:** Kontainer backend atau frontend Docker sedang dalam proses inisialisasi awal.
* **Solusi:**
  1. Tunggu sekitar 30–60 detik lalu refresh browser (`Ctrl + F5`).
  2. Buka terminal PowerShell dan jalankan:
     ```powershell
     docker compose ps
     ```
  3. Jika ada kontainer berstatus `Exited`, jalankan:
     ```powershell
     docker compose up -d
     ```

### 5.2 Masalah Batas Memori WSL2 di Windows
* File konfigurasi limit RAM telah diatur di `C:\Users\melid\.wslconfig`:
  ```ini
  [wsl2]
  memory=2GB
  swap=6GB
  ```
* Jika laptop terasa berat, cukup jalankan `wsl --shutdown` di PowerShell, lalu buka Docker Desktop kembali.

### 5.3 Menjaga Keamanan Data
Semua data transaksi tersimpan di Docker Named Volumes (`enterpriseresourceplanningerp_db-data`). Selama volume Docker tidak dihapus dengan perintah flag `-v` (`docker compose down -v`), **seluruh database transaksi Anda dijamin aman 100% dan tidak akan hilang**.
