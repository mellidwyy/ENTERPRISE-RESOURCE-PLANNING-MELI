# KUMPULAN SOAL UJIAN, KASUS PRAKTIK & KUNCI JAWABAN AKUNTANSI ERP
## MODUL MANUFAKTUR, PENGADAAN, PENJUALAN & SISTEM BUKU BESAR ERPNEXT
### Program Studi Sistem Informasi / Manajemen / Akuntansi - Mata Kuliah ERP Semester 7

**Entitas Bisnis:** Meli Dwi Company (`MDC`)  
**Studi Kasus:** Manufaktur Meja Belajar Kayu Minimalis (`MB-001`)  
**Sistem Aplikasi:** ERPNext v16 Database Terintegrasi  

---

## BAGIAN I: SOAL PILIHAN GANDA KONSEPTUAL & ANALITIS ERP

### Soal 1: Fungsi Bill of Materials (BOM)
**Pertanyaan:**  
Dalam industri manufaktur berbasis sistem ERP, dokumen *Bill of Materials* (BOM) berfungsi sebagai:
* A. Bukti pengiriman produk ke tangan pelanggan.
* B. Daftar formula standar kebutuhan bahan baku, kuantitas, dan biaya untuk membuat satu satuan produk jadi.
* C. Faktur tagihan atas pembelian bahan baku dari pemasok.
* D. Surat perintah penagihan piutang dagang yang jatuh tempo.

> **Kunci Jawaban: B**  
> **Pembahasan:** BOM adalah dokumen inti (*master formula*) dalam modul manufaktur ERP yang merinci seluruh komponen, sub-rakitan, bahan mentah, serta biaya standar (*standard valuation*) yang diperlukan untuk memproduksi unit barang jadi (`MB-001`).

---

### Soal 2: Integrasi Persediaan Perpetual (Perpetual Inventory)
**Pertanyaan:**  
Ketika dokumen *Purchase Receipt* (Penerimaan Barang) disubmit pada sistem ERPNext, jurnal akuntansi otomatis yang terbentuk pada metode persediaan perpetual adalah:
* A. Debit: Kas Besar | Kredit: Pendapatan Penjualan
* B. Debit: Persediaan Bahan Baku | Kredit: Hutang Belum Ditagih (*Stock Received But Not Billed*)
* C. Debit: Beban Pokok Penjualan | Kredit: Piutang Usaha
* D. Debit: Modal Pemilik | Kredit: Persediaan Barang Jadi

> **Kunci Jawaban: B**  
> **Pembahasan:** Pada sistem perpetual ERP, penerimaan fisik barang sebelum faktur datang diakui dengan mendebit akun persediaan gudang dan mengkredit akun liabilitas sementara (*Stock Received But Not Billed*). Ketika faktur pembelian (*Purchase Invoice*) terbit, akun sementara ini akan dibalik (*cleared*) ke Utang Usaha (*Accounts Payable*).

---

### Soal 3: Pemindahan Material ke Lantai Produksi (WIP)
**Pertanyaan:**  
Pada saat perintah kerja (*Work Order*) dijalankan, transaksi *Stock Entry* bertipe *Material Transfer for Manufacture* bertujuan untuk:
* A. Menjual bahan baku langsung ke pelanggan ritel.
* B. Memindahkan saldo stok dan nilai persediaan dari Gudang Bahan Baku ke Gudang *Work In Progress* (WIP).
* C. Menghapus persediaan bahan baku yang rusak atau usang (*scrap*).
* D. Mengurangi modal disetor perusahaan.

> **Kunci Jawaban: B**  
> **Pembahasan:** Bahan mentah yang dikeluarkan untuk dirakit harus dialihkan ke area pabrik (*Work In Progress*). Nilai persediaannya berpindah dari akun persediaan bahan baku ke akun persediaan barang dalam proses sampai meja selesai dirakit secara fisik.

---

### Soal 4: Pengakuan Beban Pokok Penjualan (HPP / COGS)
**Pertanyaan:**  
Kapan Harga Pokok Penjualan (HPP) atas produk jadi Meja Belajar (`MB-001`) diakui secara otomatis dalam buku besar (*General Ledger*) sistem ERPNext?
* A. Saat penawaran harga (*Customer Quotation*) dikirim ke calon pembeli.
* B. Saat pesanan penjualan (*Sales Order*) disetujui manajer pemasaran.
* C. Saat barang secara fisik dikeluarkan dan diserahkan melalui dokumen *Delivery Note* (Surat Jalan).
* D. Saat uang kas pelunasan disetorkan oleh pembeli ke rekening bank perusahaan.

> **Kunci Jawaban: C**  
> **Pembahasan:** Sesuai prinsip penandingan beban dan pendapatan (*matching principle*), pengeluaran fisik barang dari gudang melalui *Delivery Note* secara otomatis memicu pengakuan HPP (*Debit: Cost of Goods Sold*) dan pengurangan saldo persediaan produk jadi (*Kredit: Finished Goods Inventory*).

---

### Soal 5: Sifat Dokumen Permintaan Material (Material Request)
**Pertanyaan:**  
Dokumen *Material Request* diterbitkan oleh divisi produksi untuk meminta 20 lembar kayu mahoni. Bagaimana pengaruh dokumen ini terhadap Laporan Laba Rugi dan Neraca perusahaan?
* A. Mengakibatkan penurunan laba bersih seketika.
* B. Menambah kewajiban utang dagang di neraca sebesar nilai penawaran kayu.
* C. Tidak menimbulkan jurnal akuntansi keuangan apapun (tidak mempengaruhi neraca maupun laba rugi).
* D. Mengurangi saldo kas perusahaan secara langsung.

> **Kunci Jawaban: C**  
> **Pembahasan:** *Material Request* merupakan dokumen komitmen internal (*non-financial operational document*) yang digunakan sebagai dasar perencanaan pengadaan oleh tim *Purchasing*, sehingga belum ada hak atau kewajiban finansial yang timbul dan tidak ada jurnal akuntansi yang dicatat.

---

## BAGIAN II: SOAL KASUS TRANSAKSI OPERASIONAL & KUNCI JURNAL AKUNTANSI

Berikut adalah kronologi 8 transaksi operasional nyata yang telah dieksekusi pada sistem ERPNext **Meli Dwi Company (MDC)**.

---

### Kasus Transaksi 1: Pengadaan Bahan Baku Awal (Batch 1)
**Deskripsi Kasus:**  
Perusahaan membeli bahan baku secara kredit dari 3 pemasok untuk keperluan produksi awal meja belajar dengan rincian:
1. Dari *CV Kayu Lestari Abadi*: 10 Lembar Kayu Mahoni @ Rp 120.000 = **Rp 1.200.000,00**.
2. Dari *PT Logam Perkasa Indonesia*: 40 Batang Kaki Besi (@ Rp 45.000) dan 160 Pcs Baut (@ Rp 1.500) = **Rp 2.040.000,00**.
3. Dari *Toko Cat Warna Indah*: 5 Liter Cat Vernis @ Rp 49.000 = **Rp 245.000,00**.  
Barang telah diterima di `Gudang Bahan Baku - MDC` (Penerimaan Barang `MAT-PRE-2026-00001` s/d `00003`) dan faktur pembelian telah ditagihkan (`ACC-PINV-2026-00007` s/d `00009`).

**Pertanyaan:**  
Buatlah jurnal umum saat penerimaan barang (*Purchase Receipt*) dan saat pengakuan faktur pembelian (*Purchase Invoice*)!

#### Kunci Jawaban & Jurnal Akuntansi:
**A. Saat Penerimaan Fisik Barang (Purchase Receipt):**
| Tanggal | Kode & Nama Akun | Debit (Rp) | Kredit (Rp) |
| :---: | :--- | :---: | :---: |
| 2026-09-22 | `1141.000 - Persediaan Bahan Baku - MDC` | **3.485.000,00** | - |
| | `2112.000 - Hutang Belum Ditagih (SRNB) - MDC` | - | **3.485.000,00** |
*(Mencatat penambahan stok fisik bahan baku 10 kayu, 40 kaki besi, 160 baut, 5L cat di gudang)*

**B. Saat Penerbitan Faktur Pembelian (Purchase Invoice):**
| Tanggal | Kode & Nama Akun | Debit (Rp) | Kredit (Rp) |
| :---: | :--- | :---: | :---: |
| 2026-09-22 | `2112.000 - Hutang Belum Ditagih (SRNB) - MDC` | **3.485.000,00** | - |
| | `2111.000 - Hutang Dagang (Accounts Payable) - MDC` | - | **3.485.000,00** |
*(Menghapus akun liabilitas sementara dan mengakui utang dagang definitif ke 3 supplier)*

---

### Kasus Transaksi 2: Pengalihan Bahan Baku ke Proses Perakitan (WIP)
**Deskripsi Kasus:**  
Divisi Produksi merilis Work Order `MFG-WO-2026-00001` untuk membuat **10 unit Meja Belajar Kayu Minimalis (`MB-001`)**. Seluruh bahan baku awal (10 kayu, 40 kaki besi, 160 baut, 5L cat) senilai total **Rp 3.485.000,00** ditransfer dari `Gudang Bahan Baku` ke `Gudang Work In Progress` via Stock Entry `MAT-STE-2026-00001`.

**Pertanyaan:**  
Buatlah jurnal akuntansi atas pemindahan material tersebut!

#### Kunci Jawaban & Jurnal Akuntansi:
| Tanggal | Kode & Nama Akun | Debit (Rp) | Kredit (Rp) |
| :---: | :--- | :---: | :---: |
| 2026-09-22 | `1142.000 - Persediaan Barang Dalam Proses (WIP) - MDC` | **3.485.000,00** | - |
| | `1141.000 - Persediaan Bahan Baku - MDC` | - | **3.485.000,00** |
*(Mencatat pengalihan aset bahan baku menjadi persediaan barang dalam proses perakitan)*

---

### Kasus Transaksi 3: Penyelesaian Manufaktur 10 Unit Meja Belajar Jadi
**Deskripsi Kasus:**  
Proses pemotongan, perakitan, dan finishing 10 unit Meja Belajar (`MB-001`) selesai dikerjakan tanpa cacat (*zero defect*). Meja jadi dipindahkan ke `Gudang Barang Jadi - MDC` via Stock Entry `MAT-STE-2026-00002`. Nilai barang jadi dihitung berdasarkan akumulasi biaya bahan (10 unit x Rp 348.500 = **Rp 3.485.000,00**).

**Pertanyaan:**  
Buatlah jurnal akuntansi atas penyelesaian produk jadi manufaktur tersebut!

#### Kunci Jawaban & Jurnal Akuntansi:
| Tanggal | Kode & Nama Akun | Debit (Rp) | Kredit (Rp) |
| :---: | :--- | :---: | :---: |
| 2026-09-22 | `1143.000 - Persediaan Barang Jadi (Finished Goods) - MDC`| **3.485.000,00** | - |
| | `1142.000 - Persediaan Barang Dalam Proses (WIP) - MDC` | - | **3.485.000,00** |
*(Mencatat timbulnya 10 unit Meja Belajar siap jual dan mengosongkan saldo persediaan WIP)*

---

### Kasus Transaksi 4: Pengiriman 5 Unit Meja Belajar ke Pelanggan
**Deskripsi Kasus:**  
Pelanggan *PT Graha Furniture Nusantara* memesan 5 unit Meja Belajar (`SAL-ORD-2026-00006`) dengan harga jual Rp 550.000 per unit. Perusahaan mengirimkan barang menggunakan Surat Jalan `MAT-DN-2026-00001`. Biaya pokok 5 unit meja yang keluar adalah **Rp 1.742.500,00** (5 unit x Rp 348.500).

**Pertanyaan:**  
Buatlah jurnal akuntansi yang terbentuk otomatis saat Surat Jalan (*Delivery Note*) disubmit!

#### Kunci Jawaban & Jurnal Akuntansi:
| Tanggal | Kode & Nama Akun | Debit (Rp) | Kredit (Rp) |
| :---: | :--- | :---: | :---: |
| 2026-09-22 | `4210.000 - Harga Pokok Penjualan (HPP) - MDC` | **1.742.500,00** | - |
| | `1143.000 - Persediaan Barang Jadi - MDC` | - | **1.742.500,00** |
*(Mengakui beban pokok penjualan dan mengurangi saldo fisik persediaan meja jadi dari 10 menjadi 5 unit)*

---

### Kasus Transaksi 5: Penagihan Faktur Penjualan (Sales Invoice)
**Deskripsi Kasus:**  
Bagian penagihan menerbitkan Faktur Penjualan `ACC-SINV-2026-00006` kepada *PT Graha Furniture Nusantara* atas 5 unit meja belajar dengan total tagihan sebesar **Rp 2.750.000,00** (5 unit x Rp 550.000).

**Pertanyaan:**  
Buatlah jurnal akuntansi atas pengakuan piutang dan pendapatan penjualan!

#### Kunci Jawaban & Jurnal Akuntansi:
| Tanggal | Kode & Nama Akun | Debit (Rp) | Kredit (Rp) |
| :---: | :--- | :---: | :---: |
| 2026-09-22 | `1131.000 - Piutang Usaha (Debtors) - MDC` | **2.750.000,00** | - |
| | `4110.000 - Pendapatan Penjualan - MDC` | - | **2.750.000,00** |
*(Mengakui timbulnya hak tagih piutang usaha dan mencatat omzet penjualan)*

---

### Kasus Transaksi 6: Penerimaan Kas Pelunasan dari Pelanggan
**Deskripsi Kasus:**  
*PT Graha Furniture Nusantara* melunasi seluruh kewajibannya sebesar **Rp 2.750.000,00** secara tunai/transfer ke kas perusahaan. Transaksi dicatat pada dokumen *Payment Entry* `ACC-PAY-2026-00006`.

**Pertanyaan:**  
Buatlah jurnal akuntansi atas penerimaan kas pelunasan piutang tersebut!

#### Kunci Jawaban & Jurnal Akuntansi:
| Tanggal | Kode & Nama Akun | Debit (Rp) | Kredit (Rp) |
| :---: | :--- | :---: | :---: |
| 2026-09-22 | `1111.002 - Kas Besar - MDC` | **2.750.000,00** | - |
| | `1131.000 - Piutang Usaha (Debtors) - MDC` | - | **2.750.000,00** |
*(Mencatat penerimaan uang kas masuk dan melunasi saldo piutang pelanggan hingga bersaldo 0)*

---

### Kasus Transaksi 7: Pencatatan Aset Tetap Mesin Pabrik
**Deskripsi Kasus:**  
Perusahaan mendaftarkan 2 unit aktiva tetap operasional pabrik yang siap pakai di `Pabrik Utama`:
1. Mesin Pemotong Kayu (*Table Saw Machine*): Nilai Perolehan **Rp 8.500.000,00** (`ACC-ASS-2026-00001`).
2. Kompresor & Spray Gun Finishing: Nilai Perolehan **Rp 3.200.000,00** (`ACC-ASS-2026-00002`).  
Total nilai aset tetap pabrik: **Rp 11.700.000,00**.

**Pertanyaan:**  
Bagaimana perlakuan akuntansi atas pendaftaran aset tetap ini dan buatlah jurnal perolehan aktiva tetapnya!

#### Kunci Jawaban & Jurnal Akuntansi:
| Tanggal | Kode & Nama Akun | Debit (Rp) | Kredit (Rp) |
| :---: | :--- | :---: | :---: |
| 2026-09-22 | `1211.001 - Aktiva Mesin & Peralatan - MDC` | **11.700.000,00** | - |
| | `3110.000 - Modal Disetor Pemilik / Kas - MDC` | - | **11.700.000,00** |
*(Mencatat perolehan aktiva tetap pabrik ke neraca sebagai investasi aset produktif jangka panjang)*

---

### Kasus Transaksi 8: Pengadaan Cadangan Bahan Baku Gelombang 2
**Deskripsi Kasus:**  
Untuk mengantisipasi penawaran dari *Yayasan Bina Prestasi Mandiri*, perusahaan membeli tambahan 20 lembar Papan Kayu Mahoni (`BB-001`) @ Rp 118.000 = **Rp 2.360.000,00** dari *CV Kayu Lestari Abadi* melalui Purchase Order `PUR-ORD-2026-00014` dan barang telah masuk ke Gudang Bahan Baku (`MAT-PRE-2026-00004`).

**Pertanyaan:**  
Buatlah jurnal akuntansi atas penerimaan barang tambahan tersebut!

#### Kunci Jawaban & Jurnal Akuntansi:
| Tanggal | Kode & Nama Akun | Debit (Rp) | Kredit (Rp) |
| :---: | :--- | :---: | :---: |
| 2026-09-22 | `1141.000 - Persediaan Bahan Baku - MDC` | **2.360.000,00** | - |
| | `2112.000 - Hutang Belum Ditagih (SRNB) - MDC` | - | **2.360.000,00** |
*(Menambah persediaan kayu mahoni di Gudang Bahan Baku sebanyak 20 lembar)*

---

## BAGIAN III: SOAL HITUNGAN ANALISIS LABA RUGI & NERACA

### Soal Kasus Analisis Keuangan:
Berdasarkan seluruh transaksi di atas, hitunglah:
1. **Harga Pokok Penjualan (HPP) per unit produk `MB-001`!**
2. **Laba Kotor (*Gross Profit*) dan Laba Bersih (*Net Profit*) Perusahaan!**
3. **Persentase Marjin Laba Bersih (*Net Profit Margin*)!**
4. **Total Nilai Saldo Akhir Persediaan Barang di Gudang!**

#### Jawaban Lengkap & Pembahasan:

**1. Perhitungan HPP per Unit Meja Belajar:**
$$\begin{aligned}
\text{Biaya Kayu Mahoni (1 lbr)} &= \text{Rp } 120.000,00 \\
\text{Biaya Kaki Besi Hollow (4 btg @ 45rb)} &= \text{Rp } 180.000,00 \\
\text{Biaya Baut \& Sekrup (16 pcs @ 1.500)} &= \text{Rp } 24.000,00 \\
\text{Biaya Cat Vernis (0.5 L @ 49rb)} &= \text{Rp } 24.500,00 \\
\hline
\mathbf{\text{Total HPP Standar per Unit}} &= \mathbf{\text{Rp } 348.500,00}
\end{aligned}$$

**2. Perhitungan Laba Kotor dan Laba Bersih:**
* **Total Penjualan:** 5 unit x Rp 550.000,00 = **Rp 2.750.000,00**
* **Total HPP Penjualan:** 5 unit x Rp 348.500,00 = **Rp 1.742.500,00**
* **Laba Kotor (*Gross Profit*):**
  $$\text{Laba Kotor} = \text{Rp } 2.750.000,00 - \text{Rp } 1.742.500,00 = \mathbf{\text{Rp } 1.007.500,00}$$
* Karena belum ada beban operasional lain (listrik/gaji), maka:
  $$\mathbf{\text{Laba Bersih (Net Profit)}} = \mathbf{\text{Rp } 1.007.500,00}$$

**3. Perhitungan Net Profit Margin (NPM):**
$$\text{Net Profit Margin} = \left( \frac{\text{Rp } 1.007.500,00}{\text{Rp } 2.750.000,00} \right) \times 100\% = \mathbf{36,63\%}$$
*Interpretasi:* Setiap Rp 100 penjualan menghasilkan keuntungan bersih sebesar Rp 36,63 bagi perusahaan.

**4. Rekapitulasi Saldo Persediaan Akhir Gudang:**
* Gudang Bahan Baku: 20 lembar Kayu Mahoni x Rp 118.000 = **Rp 2.360.000,00**
* Gudang Barang Jadi: 5 unit Meja Belajar x Rp 348.500 = **Rp 1.742.500,00**
* Gudang Work In Progress (WIP): **Rp 0,00**
* **Total Nilai Persediaan Akhir:**  
  $$\text{Total Persediaan} = \text{Rp } 2.360.000,00 + \text{Rp } 1.742.500,00 = \mathbf{\text{Rp } 4.102.500,00}$$
*(Angka ini cocok 100% dengan Laporan Stock Balance di ERPNext)*
