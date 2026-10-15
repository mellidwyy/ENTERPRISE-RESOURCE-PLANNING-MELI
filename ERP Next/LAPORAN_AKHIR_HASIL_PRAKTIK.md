# LAPORAN AKHIR PRAKTIK ENTERPRISE RESOURCE PLANNING (ERP)
## IMPLEMENTASI SISTEM ERPNEXT PADA INDUSTRI MANUFAKTUR MEBEL KAYU
### STUDI KASUS: PRODUKSI & PENJUALAN MEJA BELAJAR KAYU MINIMALIS

**Nama Perusahaan:** Meli Dwi Company (`MDC`)  
**Administrator Sistem:** Meli Dwi A (`melidwyy@gmail.com`)  
**Sistem Aplikasi:** ERPNext v16 (Frappe Framework)  
**URL Sistem Localhost:** http://localhost:8080  
**Tahun Ajaran / Semester:** Semester 7 - Enterprise Resource Planning  

---

## 1. PENDAHULUAN & PROFIL USAHA

**Meli Dwi Company (MDC)** adalah entitas manufaktur skala menengah yang bergerak di bidang pembuatan perabot rumah tangga dan kantor berbahan dasar kayu mahoni berkualitas dengan aksen kaki besi industrial. 

Untuk meningkatkan efisiensi operasional, transparansi alur barang, serta akurasi pelaporan keuangan, perusahaan mengimplementasikan sistem ERP berbasis open-source, yaitu **ERPNext v16**.

Produk unggulan yang diproduksi dan disimulasikan dalam siklus ERP ini adalah:
* **Nama Produk:** Meja Belajar Kayu Minimalis
* **Kode Item:** `MB-001`
* **Spesifikasi:** Meja belajar kayu solid mahoni finishing natural dengan rangka kaki hollow steel anti-karat.

---

## 2. STRUKTUR MASTER DATA (TAHAP 1)

Sistem telah mengonfigurasi struktur dasar organisasi dan data operasional:

### A. Lokasi Gudang (Warehouses)
1. **Gudang Bahan Baku - MDC:** Menampung papan kayu, kaki besi, baut, dan cat.
2. **Gudang Work In Progress - MDC:** Area lini produksi perakitan meja.
3. **Gudang Barang Jadi - MDC:** Tempat penyimpanan meja yang telah selesai diproduksi dan siap dikirim ke konsumen.

### B. Master Data Barang (Items)
* `MB-001` - Meja Belajar Kayu Minimalis (Barang Jadi / Finished Good)
* `BB-001` - Papan Kayu Mahoni 120x60 (Bahan Baku / Raw Material)
* `BB-002` - Kaki Meja Besi Hollow (Bahan Baku / Raw Material)
* `BB-003` - Baut & Sekrup Baja (Bahan Pendukung)
* `BB-004` - Cat Vernis Wood Finish (Bahan Pendukung)
* `AST-001` - Mesin Pemotong Kayu Serbaguna Table Saw (Aset Tetap)
* `AST-002` - Kompresor & Spray Gun Finishing (Aset Tetap)

### C. Master Mitra Usaha (Stakeholders)
* **Pemasok (Suppliers):**
  * *CV Kayu Lestari Abadi* (Kayu Mahoni)
  * *PT Logam Perkasa Indonesia* (Kaki Besi & Sekrup)
  * *Toko Cat Warna Indah* (Cat Vernis)
* **Pelanggan (Customers):**
  * *PT Graha Furniture Nusantara* (Distributor Furnitur)
  * *Yayasan Bina Prestasi Mandiri* (Lembaga Pendidikan)

---

## 3. RESEP PRODUKSI / BILL OF MATERIALS (BOM)

Formula standar produksi untuk pembuatan **1 (satu) unit** Meja Belajar Kayu Minimalis (`MB-001`) tercatat dalam dokumen **`BOM-MB-001-001`**:

| Kode Bahan | Deskripsi Bahan | Kebutuhan per Unit | Biaya Satuan | Total Biaya per Unit |
| :--- | :--- | :---: | :---: | :---: |
| `BB-001` | Papan Kayu Mahoni 120x60 | 1.0 Lembar | Rp 120.000,00 | Rp 120.000,00 |
| `BB-002` | Kaki Meja Besi Hollow | 4.0 Batang | Rp 45.000,00 | Rp 180.000,00 |
| `BB-003` | Baut & Sekrup Baja | 16.0 Pcs | Rp 1.500,00 | Rp 24.000,00 |
| `BB-004` | Cat Vernis Wood Finish | 0.5 Liter | Rp 49.000,00 | Rp 24.500,00 |
| **TOTAL HPP PRODUKSI PER UNIT** | | | | **Rp 348.500,00** |

---

## 4. ALUR SIKLUS OPERASIONAL & MANUFAKTUR (TAHAP 2 S/D 5B)

### A. Pengadaan Bahan Baku (Procurement / Buying)
* Diterbitkan Pesanan Pembelian awal: `PUR-ORD-2026-00011`, `PUR-ORD-2026-00012`, `PUR-ORD-2026-00013`.
* Penerimaan barang di gudang bahan baku tercatat pada `MAT-PRE-2026-00001` s/d `00003`.
* Pengadaan tambahan gelombang 2 (20 papan kayu) via `PUR-ORD-2026-00014` dan `MAT-PRE-2026-00004`.

### B. Proses Produksi (Manufacturing Execution)
* Diterbitkan Surat Perintah Kerja Produksi: **`MFG-WO-2026-00001`** untuk target produksi **10 unit meja**.
* Bahan baku dipindahkan dari Gudang Bahan Baku ke Gudang WIP via Stock Entry `MAT-STE-2026-00001`.
* Perakitan dan finishing selesai, menghasilkan 10 unit meja jadi ke `Gudang Barang Jadi - MDC` via Stock Entry `MAT-STE-2026-00002`.

### C. Penjualan & Distribusi (Selling & Delivery)
* Pesanan Penjualan dari *PT Graha Furniture Nusantara*: **`SAL-ORD-2026-00006`** sebanyak 5 unit @ Rp 550.000.
* Surat Jalan Pengiriman: **`MAT-DN-2026-00001`** (5 unit dikeluarkan dari Gudang Barang Jadi).
* Faktur Penjualan: **`ACC-SINV-2026-00006`** senilai **Rp 2.750.000,00**.
* Pembayaran Kas Masuk: **`ACC-PAY-2026-00006`** diterima lunas di akun `1111.002 - Kas Besar - MDC`.

### D. Dokumen Pendukung & Aset Tetap Pabrik
* Permintaan Material: `MAT-MR-2026-00001` untuk rencana produksi batch 2.
* Penawaran Pemasok: `PUR-SQTN-2026-00001` dari CV Kayu Lestari Abadi.
* Penawaran Pelanggan: `SAL-QTN-2026-00001` ke Yayasan Bina Prestasi Mandiri (15 unit @ Rp 540.000 = Rp 8.100.000,00).
* Aset Tetap Pabrik: Mesin Table Saw (`ACC-ASS-2026-00001`, Rp 8.500.000) dan Kompresor Cat (`ACC-ASS-2026-00002`, Rp 3.200.000).

---

## 5. EVALUASI LAPORAN KEUANGAN & SALDO STOK (TAHAP 6)

### A. Laporan Saldo Persediaan (Stock Balance)
* **Gudang Bahan Baku - MDC:**
  * Papan Kayu Mahoni (`BB-001`): 20.0 Unit (Nilai: Rp 2.360.000,00)
* **Gudang Work In Progress - MDC:**
  * Saldo: 0 Unit (Semua material telah tuntas dirakit)
* **Gudang Barang Jadi - MDC:**
  * Meja Belajar Kayu Minimalis (`MB-001`): 5.0 Unit (Nilai: Rp 1.742.500,00)
* **Total Nilai Persediaan Akhir:** **Rp 4.102.500,00**

### B. Laporan Laba Rugi (Profit & Loss Statement)
* **Pendapatan Penjualan (5 Meja @ Rp 550.000):** Rp 2.750.000,00
* **Harga Pokok Penjualan / HPP (5 Meja @ Rp 348.500):** (Rp 1.742.500,00)
* **Laba Bersih Operasional (Net Profit):** **Rp 1.007.500,00**  
*(Margin Laba Bersih = 36,63%)*

### C. Neraca Keuangan (Balance Sheet Summary)
* **Kas Masuk di Tangan:** Rp 2.750.000,00
* **Persediaan Barang:** Rp 4.102.500,00
* **Total Aktiva Lancar:** Rp 6.852.500,00
* **Aktiva Tetap Mesin & Alat:** Rp 11.700.000,00
* **Total Keseluruhan Aset Usaha:** **Rp 18.552.500,00**

---

## 6. KESIMPULAN

Praktik integrasi ERPNext pada industri manufaktur **Meli Dwi Company** berhasil membuktikan bahwa sistem ERP mampu:
1. Menghilangkan redundansi data operasional antar bagian (Pengadaan, Gudang, Produksi, dan Penjualan).
2. Menjaga ketertelusuran barang (*traceability*) secara *real-time* dari status bahan baku hingga barang jadi.
3. Mengotomatisasi kalkulasi Harga Pokok Penjualan (HPP) berbasis *Bill of Materials* secara akurat.
4. Memberikan kepastian posisi keuangan (Laba Bersih Rp 1.007.500,00) seketika saat barang dikirim dan dibayar.
