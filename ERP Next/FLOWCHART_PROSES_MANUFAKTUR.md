# DIAGRAM ALIR PROSES BISNIS & DOKUMEN MANUFAKTUR (FLOWCHART)
## IMPLEMENTASI SISTEM ERPNEXT PADA MELI DWI COMPANY (MDC)
### Studi Kasus: Produksi Meja Belajar Kayu Minimalis (MB-001)

Dokumen ini menyajikan visualisasi menyeluruh diagram alir proses bisnis (*Business Process Flowchart*), siklus hidup dokumen ERPNext (*Document Lifecycle*), serta integrasi jurnal akuntansi otomatis (*General Ledger Accounting Flow*).

---

## 1. FLOWCHART UTAMA: SIKLUS END-TO-END INDUSTRI MANUFAKTUR

Diagram ini memetakan koordinasi antar 5 departemen utama: **Perencanaan Produksi**, **Pengadaan (Purchasing)**, **Gudang (Warehouse)**, **Penjualan (Sales)**, dan **Keuangan (Accounting)**.

```mermaid
flowchart TD
    subgraph S1["1. PERENCANAAN & PENGADAAN (BUYING)"]
        A1["Mulai: Rencana Produksi Meja MB-001"] --> A2["Terbitkan Material Request (MAT-MR-2026-00001)"]
        A2 --> A3["Minta Penawaran Supplier (PUR-SQTN-2026-00001)"]
        A3 --> A4["Terbitkan Purchase Order ke 3 Supplier (PUR-ORD)"]
        A4 --> A5["Pemasok Kirim Bahan Baku"]
    end

    subgraph S2["2. PENERIMAAN & PENYIMPANAN GUDANG (STOCK)"]
        A5 --> B1["Penerimaan Barang di Gudang Bahan Baku (Purchase Receipt)"]
        B1 --> B2["Stok Bahan Baku Bertambah (Kayu, Besi, Baut, Cat)"]
        B1 --> B3["Faktur Pembelian Dicatat (Purchase Invoice)"]
    end

    subgraph S3["3. PROSES PRODUKSI MANUFAKTUR (MFG)"]
        B2 --> C1["Master Resep Produksi: BOM-MB-001-001"]
        C1 --> C2["Rilis Work Order Produksi 10 Meja (MFG-WO-2026-00001)"]
        C2 --> C3["Transfer Bahan ke Lantai Pabrik: Stock Entry Material Transfer"]
        C3 --> C4["Bahan Masuk ke Gudang Work In Progress (WIP)"]
        C4 --> C5["Proses Pemotongan, Perakitan & Finishing Meja"]
        C5 --> C6["Penyelesaian Meja: Stock Entry Manufacture"]
        C6 --> C7["10 Unit Meja Masuk ke Gudang Barang Jadi (WIP Saldo 0)"]
    end

    subgraph S4["4. PENJUALAN & PENGIRIMAN (SELLING)"]
        C7 --> D1["Penawaran ke Customer: Quotation (SAL-QTN-2026-00001)"]
        D1 --> D2["Pesanan Penjualan Diterima: Sales Order (SAL-ORD-2026-00006)"]
        D2 --> D3["Kirim 5 Meja via Surat Jalan: Delivery Note (MAT-DN-2026-00001)"]
        D3 --> D4["Stok Gudang Barang Jadi Berkurang 5 (Sisa 5 Unit)"]
    end

    subgraph S5["5. PENAGIHAN & KEUANGAN (ACCOUNTS)"]
        D3 --> E1["Terbitkan Faktur Penjualan: Sales Invoice (ACC-SINV-2026-00006)"]
        E1 --> E2["Pelanggan Membayar: Payment Entry (ACC-PAY-2026-00006)"]
        E2 --> E3["Kas Masuk Rp 2.750.000 (1111.002 - Kas Besar - MDC)"]
        E3 --> E4["Evaluasi Laporan Laba Rugi (Laba Bersih Rp 1.007.500)"]
        E4 --> E5["Selesai: Neraca & Stok Balance Terupdate Otomatis"]
    end

    style S1 fill:#f0f4f8,stroke:#1f4e79,stroke-width:2px
    style S2 fill:#e8f8f5,stroke:#117864,stroke-width:2px
    style S3 fill:#fef9e7,stroke:#b7950b,stroke-width:2px
    style S4 fill:#fdf2e9,stroke:#ba4a00,stroke-width:2px
    style S5 fill:#eaf2f8,stroke:#2471a3,stroke-width:2px
```

---

## 2. FLOWCHART HUBUNGAN KETERKAITAN DOKUMEN TRANSAKSI ERPNEXT

Diagram ini menggambarkan relasi turunan (*document lineage*) dari setiap formulir transaksi resmi di dalam modul ERPNext.

```mermaid
flowchart LR
    subgraph Buying_Cycle["SIKLUS PEMBELIAN"]
        MR["Material Request\n(MAT-MR)"] --> SQ["Supplier Quotation\n(PUR-SQTN)"]
        SQ --> PO["Purchase Order\n(PUR-ORD)"]
        PO --> PR["Purchase Receipt\n(MAT-PRE)"]
        PR --> PI["Purchase Invoice\n(ACC-PINV)"]
    end

    subgraph Mfg_Cycle["SIKLUS PRODUKSI"]
        BOM["Bill of Materials\n(BOM-MB-001)"] --> WO["Work Order\n(MFG-WO)"]
        WO --> SE1["Stock Entry\n(Transfer to WIP)"]
        SE1 --> SE2["Stock Entry\n(Manufacture FG)"]
    end

    subgraph Selling_Cycle["SIKLUS PENJUALAN"]
        QTN["Quotation\n(SAL-QTN)"] --> SO["Sales Order\n(SAL-ORD)"]
        SO --> DN["Delivery Note\n(MAT-DN)"]
        DN --> SI["Sales Invoice\n(ACC-SINV)"]
        SI --> PE["Payment Entry\n(ACC-PAY)"]
    end

    PR -.->|Bahan Masuk| SE1
    SE2 -.->|Barang Jadi Masuk| DN

    style Buying_Cycle fill:#e8f6f3,stroke:#1abc9c,stroke-width:2px
    style Mfg_Cycle fill:#fefde8,stroke:#f39c12,stroke-width:2px
    style Selling_Cycle fill:#ebf5fb,stroke:#3498db,stroke-width:2px
```

---

## 3. FLOWCHART INTEGRASI JURNAL AKUNTANSI OTOMATIS (PERPETUAL GENERAL LEDGER)

Diagram ini memperlihatkan bagaimana mutasi fisik barang secara otomatis dijurnal ke buku besar (*General Ledger*) tanpa perlu entri jurnal manual:

```mermaid
flowchart TD
    subgraph PR_Journal["1. Saat Penerimaan Barang (Purchase Receipt)"]
        direction LR
        J1D["Debit: Persediaan Bahan Baku\n(1141.000)"] <--> J1K["Kredit: Hutang Belum Ditagih\n(2112.000)"]
    end

    subgraph PI_Journal["2. Saat Faktur Pembelian Terbit (Purchase Invoice)"]
        direction LR
        J2D["Debit: Hutang Belum Ditagih\n(2112.000)"] <--> J2K["Kredit: Hutang Usaha / Supplier\n(2111.000)"]
    end

    subgraph WIP_Journal["3. Saat Perakitan Meja Dimulai (Stock Entry Issue)"]
        direction LR
        J3D["Debit: Persediaan WIP\n(1142.000)"] <--> J3K["Kredit: Persediaan Bahan Baku\n(1141.000)"]
    end

    subgraph FG_Journal["4. Saat Perakitan Selesai Jadi Meja (Stock Entry Manufacture)"]
        direction LR
        J4D["Debit: Persediaan Barang Jadi\n(1143.000)"] <--> J4K["Kredit: Persediaan WIP\n(1142.000)"]
    end

    subgraph DN_Journal["5. Saat Barang Dikirim ke Pembeli (Delivery Note)"]
        direction LR
        J5D["Debit: Harga Pokok Penjualan - HPP\n(4210.000)"] <--> J5K["Kredit: Persediaan Barang Jadi\n(1143.000)"]
    end

    subgraph SI_Journal["6. Saat Faktur Penjualan Diterbitkan (Sales Invoice)"]
        direction LR
        J6D["Debit: Piutang Usaha\n(1131.000)"] <--> J6K["Kredit: Pendapatan Penjualan\n(4110.000)"]
    end

    subgraph PAY_Journal["7. Saat Pembayaran Diterima (Payment Entry)"]
        direction LR
        J7D["Debit: Kas Besar\n(1111.002)"] <--> J7K["Kredit: Piutang Usaha\n(1131.000)"]
    end

    PR_Journal --> PI_Journal
    PI_Journal --> WIP_Journal
    WIP_Journal --> FG_Journal
    FG_Journal --> DN_Journal
    DN_Journal --> SI_Journal
    SI_Journal --> PAY_Journal

    style PR_Journal fill:#f4f6f6,stroke:#7f8c8d
    style PI_Journal fill:#f4f6f6,stroke:#7f8c8d
    style WIP_Journal fill:#fef9e7,stroke:#f1c40f
    style FG_Journal fill:#fef9e7,stroke:#f1c40f
    style DN_Journal fill:#eaf2f8,stroke:#2980b9
    style SI_Journal fill:#eaf2f8,stroke:#2980b9
    style PAY_Journal fill:#e8f8f5,stroke:#27ae60
```

---

## 4. PENJELASAN PENGENDALIAN INTERNAL PADA ALUR DOKUMEN

Sistem alur di atas menerapkan kontrol internal manufaktur (*Internal Control System*):
1. **Three-Way Matching:** Pencocokan 3 arah antara *Purchase Order*, *Purchase Receipt*, dan *Purchase Invoice* mencegah perusahaan membayar barang yang belum diterima atau salah harga.
2. **Standard Costing vs Actual:** *Work Order* membatasi penggunaan bahan baku sesuai resep BOM sehingga pemborosan bahan langsung terdeteksi.
3. **Pemisahan Tugas (Segregation of Duties):** Bagian gudang yang menerima barang fisik (*Delivery Note / Receipt*) terpisah dari bagian akuntansi yang menerbitkan faktur (*Invoice*).
