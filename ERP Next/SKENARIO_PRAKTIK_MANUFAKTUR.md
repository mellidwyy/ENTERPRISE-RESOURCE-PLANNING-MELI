# Skenario Praktik ERPNext: Industri Manufaktur
**Studi Kasus:** Industri Pembuatan Meja Belajar Kayu Minimalis  
**Nama Perusahaan:** Meli Dwi Company  
**Folder Dataset:** `ERP_Meli`

---

## Ringkasan Alur Praktik Manufaktur
Praktikum ini mensimulasikan siklus lengkap sebuah perusahaan manufaktur:
```
1. Master Data -> 2. Pengadaan Bahan Baku (Buying) -> 3. Pembuatan BOM (Resep)
      -> 4. Proses Produksi (Manufacturing) -> 5. Penjualan Produk Jadi (Selling)
            -> 6. Laporan Keuangan & Stok
```

---

## Tahap 1: Penginputan Master Data

### 1. Master Gudang (Stock > Warehouse)
Buka menu **Stock > Warehouse > Add Warehouse**:
1. **Gudang Bahan Baku** (Simpan material kayu, besi, cat, baut)
2. **Gudang Work In Progress (WIP)** (Area lantai pabrik perakitan meja)
3. **Gudang Barang Jadi** (Simpan meja yang sudah selesai diproduksi)

### 2. Master Item / Barang (Stock > Item)
Buka menu **Stock > Item > Add Item**:

* **Bahan Baku (Raw Material):**
  1. `BB-001` - Papan Kayu Mahoni 120x60 (Satuan: *Nos*, Harga Beli: Rp 120.000)
  2. `BB-002` - Kaki Besi Hollow Meja (Satuan: *Nos*, Harga Beli: Rp 45.000)
  3. `BB-003` - Baut & Sekrup Baja 5cm (Satuan: *Nos*, Harga Beli: Rp 1.000)
  4. `BB-004` - Cat Vernis Natural Clear (Satuan: *Litre*, Harga Beli: Rp 65.000)
  *(Centang "Maintain Stock" dan "Is Purchase Item", Jangan centang "Is Sales Item")*

* **Barang Jadi (Finished Good):**
  1. `MB-001` - Meja Belajar Kayu Minimalis (Satuan: *Nos*, Harga Jual: Rp 550.000)
  *(Centang "Maintain Stock" dan "Is Sales Item")*

### 3. Master Pemasok (Buying > Supplier)
1. **CV Kayu Lestari Abadi** (Pemasok Kayu Mahoni)
2. **PT Logam Perkasa Indonesia** (Pemasok Kaki Besi & Baut)
3. **Toko Cat Warna Indah** (Pemasok Cat Vernis)

### 4. Master Pelanggan (Selling > Customer)
1. **PT Graha Furniture Nusantara** (Toko Retail Mebel)
2. **Yayasan Bina Prestasi Mandiri** (Institusi Sekolah)

---

## Tahap 2: Pengadaan Bahan Baku (Buying Cycle)
Untuk memproduksi **10 unit** meja belajar, kita memesan bahan baku ke supplier:

1. **Purchase Order (PO):**
   * Masuk ke **Buying > Purchase Order > Add Purchase Order**.
   * Buat PO ke **CV Kayu Lestari Abadi**: 10 unit `BB-001` (Rp 1.200.000).
   * Buat PO ke **PT Logam Perkasa Indonesia**: 40 unit `BB-002` (Rp 1.800.000) & 160 unit `BB-003` (Rp 160.000).
   * Buat PO ke **Toko Cat Warna Indah**: 5 Liter `BB-004` (Rp 325.000).
   * Klik **Save** lalu **Submit**.

2. **Purchase Receipt (Penerimaan Barang):**
   * Di tiap PO, klik tombol **Create > Receipt**.
   * Set target gudang penerimaan ke: **Gudang Bahan Baku**.
   * Klik **Submit** (Stok bahan baku sekarang otomatis bertambah).

3. **Purchase Invoice & Pembayaran:**
   * Di dokumen Receipt/PO, klik **Create > Invoice**.
   * Masukkan faktur lalu klik **Create > Payment** untuk pelunasan pembayaran kas/bank.

---

## Tahap 3: Pembuatan Bill of Materials (BOM)
BOM adalah resep formula produksi.

1. Buka menu **Manufacturing > Bill of Materials (BOM) > Add BOM**.
2. **Item:** Pilih `MB-001` (Meja Belajar Kayu Minimalis).
3. **Quantity:** `1`
4. Di tabel **Materials (Bahan yang dibutuhkan)**, masukkan:
   * `BB-001` : 1 Nos
   * `BB-002` : 4 Nos
   * `BB-003` : 16 Nos
   * `BB-004` : 0.5 Litre
5. Biaya bahan baku otomatis dihitung: **Rp 348.500 / unit**.
6. Klik **Save** lalu **Submit**.

---

## Tahap 4: Proses Produksi (Manufacturing Cycle)
Target: Memproduksi **10 unit** Meja Belajar.

1. **Work Order (Perintah Kerja):**
   * Buka **Manufacturing > Work Order > Add Work Order**.
   * Item To Produce: `MB-001`.
   * Qty To Manufacture: `10`.
   * Source Warehouse: `Gudang Bahan Baku`.
   * WIP Warehouse: `Gudang Work In Progress (WIP)`.
   * Target Warehouse: `Gudang Barang Jadi`.
   * Klik **Save** lalu **Submit**.

2. **Transfer Bahan Baku ke Lantai Produksi:**
   * Di dalam Work Order, klik **Start** (atau Create > Stock Entry: Material Transfer for Manufacture).
   * Klik **Submit** (Bahan baku keluar dari Gudang Bahan Baku dan berpindah ke Gudang WIP).

3. **Selesai Produksi (Manufacture):**
   * Di dalam Work Order yang sama, klik **Finish** (Create > Stock Entry: Manufacture).
   * Klik **Submit**.
   * *Hasil:* Stok bahan di Gudang WIP berkurang, dan **10 unit Meja Belajar (`MB-001`) resmi masuk ke Gudang Barang Jadi**.

---

## Tahap 5: Penjualan Produk Jadi (Selling Cycle)
PT Graha Furniture Nusantara memesan **5 unit Meja Belajar**:

1. **Sales Order (SO):**
   * Masuk ke **Selling > Sales Order > Add Sales Order**.
   * Customer: `PT Graha Furniture Nusantara`.
   * Item: `MB-001`, Qty: `5`, Harga Satuan: `Rp 550.000` (Total: Rp 2.750.000).
   * Klik **Save** lalu **Submit**.

2. **Delivery Note (Surat Jalan / Pengiriman Barang):**
   * Di Sales Order, klik **Create > Delivery**.
   * Source Warehouse: `Gudang Barang Jadi`.
   * Klik **Submit** (Stok meja di gudang barang jadi berkurang 5 unit).

3. **Sales Invoice (Faktur Penjualan):**
   * Di Sales Order, klik **Create > Invoice**.
   * Klik **Submit**.

4. **Penerimaan Pembayaran (Payment Entry):**
   * Di Sales Invoice, klik **Create > Payment**.
   * Masukkan akun Kas/Bank, klik **Submit**. Pendapatan penjualan resmi tercatat!

---

## Tahap 6: Evaluasi & Laporan Praktikum
Buka menu laporan untuk melihat hasil keseluruhan:
* **Stock Balance (Laporan Posisi Stok):**
  Buka `Stock > Stock Balance`. Anda akan melihat sisa bahan baku dan sisa 5 unit meja belajar.
* **Profit and Loss Statement (Laba Rugi):**
  Buka `Accounting > Profit and Loss Statement`. Anda dapat menganalisis pendapatan penjualan vs Harga Pokok Penjualan (HPP/COGS).
