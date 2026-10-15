import os
import sys

try:
    import docx
    from docx import Document
    from docx.shared import Inches, Pt, RGBColor
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    from docx.enum.table import WD_TABLE_ALIGNMENT
    from docx.oxml import OxmlElement
    from docx.oxml.ns import qn
except ImportError:
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "python-docx"])
    import docx
    from docx import Document
    from docx.shared import Inches, Pt, RGBColor
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    from docx.enum.table import WD_TABLE_ALIGNMENT
    from docx.oxml import OxmlElement
    from docx.oxml.ns import qn

def set_cell_background(cell, fill_hex):
    tcPr = cell._element.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), fill_hex)
    tcPr.append(shd)

def create_manual_docx():
    doc = Document()
    for section in doc.sections:
        section.top_margin = Inches(1)
        section.bottom_margin = Inches(1)
        section.left_margin = Inches(1)
        section.right_margin = Inches(1)

    # Title Page / Header
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r1 = p_title.add_run("BUKU PETUNJUK PENGGUNAAN SISTEM ERPNEXT\n")
    r1.bold = True
    r1.font.size = Pt(20)
    r1.font.color.rgb = RGBColor(31, 78, 121)

    r2 = p_title.add_run("PANDUAN OPERASIONAL LENGKAP LOCALHOST & MODUL MANUFAKTUR\n")
    r2.bold = True
    r2.font.size = Pt(13)
    r2.font.color.rgb = RGBColor(68, 114, 196)

    r3 = p_title.add_run("Studi Kasus: Meli Dwi Company (MDC) - Produksi Meja Belajar Kayu Minimalis\n\n")
    r3.italic = True
    r3.font.size = Pt(11)

    p_meta = doc.add_paragraph()
    p_meta.add_run("Penyusun: ").bold = True
    p_meta.add_run("Meli Dwi A (melidwyy@gmail.com)\n")
    p_meta.add_run("Mata Kuliah: ").bold = True
    p_meta.add_run("Enterprise Resource Planning (ERP) - Semester 7\n")
    p_meta.add_run("Platform: ").bold = True
    p_meta.add_run("ERPNext v16 on Docker Desktop (Windows / WSL2)\n")
    p_meta.add_run("URL Akses: ").bold = True
    p_meta.add_run("http://localhost:8080 (Port 8080)\n")
    p_meta.add_run("Status Sistem: ").bold = True
    p_meta.add_run("Berjalan Aktif & Tervalidasi 100% (Termasuk Ekuitas & Prive)\n")

    doc.add_heading("BAB I: PENGANTAR SISTEM & ARSITEKTUR LOCALHOST", level=1)
    doc.add_paragraph(
        "Sistem ERPNext pada proyek ini diinstalasi menggunakan kontainerisasi Docker modern yang berjalan "
        "di atas sistem operasi Windows dengan subsistem WSL2. Arsitektur ini terdiri dari 9 layanan: "
        "frontend (Nginx Reverse Proxy port 8080), backend (Gunicorn ERPNext v16), db (MariaDB 11.8), "
        "redis-cache, redis-queue, worker queue-short, queue-long, scheduler, dan websocket server."
    )

    doc.add_heading("Perintah Penting Pengelolaan Server di PowerShell:", level=2)
    tbl_cmd = doc.add_table(rows=1, cols=2)
    tbl_cmd.style = 'Table Grid'
    tbl_cmd.alignment = WD_TABLE_ALIGNMENT.CENTER
    h = tbl_cmd.rows[0].cells
    h[0].text = "Perintah PowerShell"
    h[1].text = "Fungsi & Kegunaan"
    set_cell_background(h[0], "D9E1F2")
    set_cell_background(h[1], "D9E1F2")
    for cell in h:
        for p in cell.paragraphs:
            for r in p.runs:
                r.bold = True

    commands = [
        ("docker compose up -d", "Menyalakan seluruh server ERPNext di background"),
        ("docker compose ps", "Mengecek status kesehatan kontainer (pastikan semua Up)"),
        ("docker compose down", "Mematikan server secara aman (data tetap tersimpan aman)"),
        ("docker compose restart backend frontend", "Me-restart layanan web jika ada perubahan konfigurasi"),
    ]
    for cmd, desc in commands:
        row = tbl_cmd.add_row().cells
        row[0].text = cmd
        row[1].text = desc

    doc.add_heading("BAB II: NAVIGASI ANTARMUKA PENGGUNA (DESK NAVIGATION)", level=1)
    doc.add_paragraph(
        "1. Awesome Bar (Search Bar Utama): Terletak di bagian atas tengah. Pengguna cukup mengetikkan "
        "nama dokumen atau laporan (contoh: 'Stock Balance', 'Sales Order', 'Work Order', 'Journal Entry') untuk berpindah halaman seketika.\n"
        "2. Sidebar Kiri: Menyediakan akses ke ruang kerja terstruktur (Stock, Buying, Manufacturing, Selling, Accounts, Assets).\n"
        "3. Status Dokumen: Setiap dokumen melalui tahapan Draft (bisa diedit), Submitted (sah & mempengaruhi stok/jurnal), "
        "dan Cancelled (dibatalkan dengan jurnal pembalik)."
    )

    doc.add_heading("BAB III: PANDUAN PENGOPERASIAN PER MODUL", level=1)
    
    doc.add_heading("3.1 Modul Pengadaan (Buying)", level=2)
    doc.add_paragraph(
        "Alur pengadaan dimulai dari Material Request (MAT-MR-2026-00001) untuk kebutuhan bahan baku, "
        "dilanjutkan dengan meminta Supplier Quotation (PUR-SQTN-2026-00001), kemudian menerbitkan "
        "Purchase Order resmi (PUR-ORD-2026-00011 s/d 00014). Saat bahan tiba, staff gudang membuat Purchase Receipt "
        "(MAT-PRE-2026-00001 s/d 00004) sehingga saldo fisik bertambah seketika."
    )

    doc.add_heading("3.2 Modul Manufaktur (Manufacturing)", level=2)
    doc.add_paragraph(
        "Modul manufaktur berpijak pada Bill of Materials (BOM-MB-001-001). Satu unit Meja Belajar Kayu Minimalis "
        "membutuhkan 1 lembar papan mahoni, 4 kaki besi hollow, 16 baut baja, dan 0.5 liter cat vernis "
        "dengan HPP standar Rp 348.500,00 per meja. Eksekusi perakitan dilakukan melalui Work Order (MFG-WO-2026-00001) "
        "yang memicu perpindahan bahan ke WIP (MAT-STE-2026-00001) dan penyelesaian 10 meja jadi (MAT-STE-2026-00002)."
    )

    doc.add_heading("3.3 Modul Penjualan & Distribusi (Selling)", level=2)
    doc.add_paragraph(
        "Penawaran harga dikirim ke pelanggan via Quotation (SAL-QTN-2026-00001). Setelah disepakati, dibuat Sales Order "
        "(SAL-ORD-2026-00006). Pengiriman 5 meja dilakukan via Delivery Note (MAT-DN-2026-00001), penagihan via Sales Invoice "
        "(ACC-SINV-2026-00006), dan pembayaran kas masuk Rp 2.750.000 via Payment Entry (ACC-PAY-2026-00006)."
    )

    doc.add_heading("3.4 Modul Manajemen Aset Tetap (Assets)", level=2)
    doc.add_paragraph(
        "Didaftarkan 2 unit aset produktif pabrik pada Kategori 'Mesin & Peralatan Pabrik':\n"
        "- ACC-ASS-2026-00001: Mesin Pemotong Kayu (Table Saw) = Rp 8.500.000,00\n"
        "- ACC-ASS-2026-00002: Kompresor & Spray Gun Finishing = Rp 3.200.000,00\n"
        "Total nilai aset tetap Rp 11.700.000,00 tercatat sah menambah kekayaan neraca perusahaan."
    )

    doc.add_heading("3.5 Modul Akuntansi: Ekuitas Modal & Penarikan Prive (Accounts)", level=2)
    doc.add_paragraph(
        "Pencatatan pos ekuitas dan modal dilakukan melalui dokumen Journal Entry:\n"
        "1. ACC-JV-2026-00001: Setoran Modal Awal Pemilik Ibu Meli Dwi A sebesar Rp 30.000.000,00 (Debit Kas Besar, Kredit Modal di Setor).\n"
        "2. ACC-JV-2026-00002: Penarikan Prive Pemilik sebesar Rp 2.000.000,00 (Debit Prive Pemilik, Kredit Kas Besar).\n"
        "Transaksi ini membuat kelompok Ekuitas di Neraca memiliki saldo modal bersih Rp 28.000.000 dan saldo Kas Besar bertambah menjadi Rp 30.750.000,00."
    )

    doc.add_heading("BAB IV: CARA MENARIK LAPORAN KEUANGAN & OPERASIONAL", level=1)
    doc.add_paragraph(
        "1. Laporan Stok (Stock Balance): Ketik 'Stock Balance' di search bar -> Pilih Company 'Meli Dwi Company'. "
        "Menampilkan sisa 20 papan kayu di Gudang Bahan Baku dan 5 unit meja belajar di Gudang Barang Jadi.\n"
        "2. Laporan Laba Rugi (Profit & Loss): Ketik 'Profit and Loss Statement'. Menampilkan Pendapatan Rp 2.750.000, "
        "HPP Rp 1.742.500, dan Laba Bersih Rp 1.007.500.\n"
        "3. Laporan Neraca (Balance Sheet): Ketik 'Balance Sheet'. Menampilkan Kas Rp 30.750.000, Persediaan Rp 4.102.500, "
        "Aset Tetap Rp 11.700.000 (Total Aset Rp 46.552.500), serta Modal di Setor Rp 30.000.000 dikurangi Prive Rp 2.000.000 dan Laba Bersih Rp 1.007.500 "
        "(Total Ekuitas Rp 29.007.500).\n"
        "4. Ekspor Data: Klik menu titik tiga (...) atau 'Actions' di kanan atas layar laporan untuk mengunduh versi Excel atau PDF."
    )

    out_path = "/home/frappe/frappe-bench/sites/BUKU_PETUNJUK_PENGGUNAAN_ERPNEXT.docx"
    doc.save(out_path)
    print(f"[OK] {out_path} berhasil dibuat!", flush=True)

def create_soal_jurnal_docx():
    doc = Document()
    for section in doc.sections:
        section.top_margin = Inches(1)
        section.bottom_margin = Inches(1)
        section.left_margin = Inches(1)
        section.right_margin = Inches(1)

    # Title
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r1 = p_title.add_run("KUMPULAN SOAL UJIAN & KUNCI JAWABAN JURNAL AKUNTANSI ERP\n")
    r1.bold = True
    r1.font.size = Pt(18)
    r1.font.color.rgb = RGBColor(31, 78, 121)

    r2 = p_title.add_run("PRAKTIK TRANSAKSI MANUFAKTUR & BUKU BESAR ERPNEXT\n")
    r2.bold = True
    r2.font.size = Pt(13)
    r2.font.color.rgb = RGBColor(68, 114, 196)

    r3 = p_title.add_run("Studi Kasus Lengkap: Meli Dwi Company (MDC) - Produksi Meja Belajar Kayu Minimalis\n\n")
    r3.italic = True
    r3.font.size = Pt(11)

    p_info = doc.add_paragraph()
    p_info.add_run("Mata Kuliah: ").bold = True
    p_info.add_run("Enterprise Resource Planning (ERP) - Semester 7\n")
    p_info.add_run("Penyusun: ").bold = True
    p_info.add_run("Meli Dwi A (melidwyy@gmail.com)\n")
    p_info.add_run("Cakupan Materi: ").bold = True
    p_info.add_run("Pengadaan, BOM, Produksi, Penjualan, Ekuitas & Prive, Jurnal Perpetual & Laporan Keuangan\n")

    doc.add_heading("BAGIAN I: SOAL KASUS TRANSAKSI & KUNCI JURNAL AKUNTANSI (DEBIT / KREDIT)", level=1)
    doc.add_paragraph(
        "Berikut disajikan 10 kasus transaksi nyata yang terjadi pada Meli Dwi Company selama simulasi siklus manufaktur. "
        "Setiap kasus dilengkapi dengan analisis transaksi dan tabel jurnal akuntansi perpetual resmi."
    )

    transactions = [
        {
            "no": "1",
            "title": "Setoran Modal Awal Pendirian Perusahaan (Ekuitas Pemilik)",
            "desc": "Ibu Meli Dwi A menyetorkan uang tunai sebesar Rp 30.000.000,00 ke rekening kas perusahaan sebagai modal awal pendirian usaha via Journal Entry ACC-JV-2026-00001.",
            "journals": [
                ("Saat Penyetoran Modal Awal:", [
                    ("1111.002 - Kas Besar - MDC", "30.000.000,00", "-"),
                    ("3110.000 - Modal di Setor - MDC", "-", "30.000.000,00")
                ])
            ]
        },
        {
            "no": "2",
            "title": "Pengadaan Bahan Baku Awal (Batch 1)",
            "desc": "Perusahaan menerima bahan baku dari 3 supplier: 10 Kayu Mahoni (Rp 1.200.000), 40 Kaki Besi & 160 Baut (Rp 2.040.000), dan 5L Cat Vernis (Rp 245.000) dengan total nilai Rp 3.485.000,00 via Bukti Penerimaan Barang (MAT-PRE-2026-00001 s/d 00003) dan Faktur Pembelian (ACC-PINV-2026-00007 s/d 00009).",
            "journals": [
                ("Saat Penerimaan Barang (Purchase Receipt):", [
                    ("1141.000 - Persediaan Bahan Baku - MDC", "3.485.000,00", "-"),
                    ("2112.000 - Hutang Belum Ditagih (SRNB) - MDC", "-", "3.485.000,00")
                ]),
                ("Saat Penerbitan Faktur Pembelian (Purchase Invoice):", [
                    ("2112.000 - Hutang Belum Ditagih (SRNB) - MDC", "3.485.000,00", "-"),
                    ("2111.000 - Hutang Usaha / Supplier - MDC", "-", "3.485.000,00")
                ])
            ]
        },
        {
            "no": "3",
            "title": "Pengalihan Bahan Baku ke Proses Perakitan (WIP)",
            "desc": "Divisi produksi merilis Work Order (MFG-WO-2026-00001) untuk merakit 10 Meja Belajar. Seluruh bahan mentah senilai Rp 3.485.000 dipindahkan dari Gudang Bahan Baku ke Gudang Work In Progress via Stock Entry MAT-STE-2026-00001.",
            "journals": [
                ("Saat Pengalihan Bahan Baku ke Pabrik:", [
                    ("1142.000 - Persediaan Barang Dalam Proses (WIP) - MDC", "3.485.000,00", "-"),
                    ("1141.000 - Persediaan Bahan Baku - MDC", "-", "3.485.000,00")
                ])
            ]
        },
        {
            "no": "4",
            "title": "Penyelesaian Manufaktur 10 Unit Meja Belajar Jadi",
            "desc": "Proses perakitan dan finishing 10 unit Meja Belajar selesai 100%. Barang jadi dipindahkan ke Gudang Barang Jadi via Stock Entry MAT-STE-2026-00002 dengan total akumulasi biaya Rp 3.485.000,00 (Rp 348.500/unit).",
            "journals": [
                ("Saat Penerimaan Meja Jadi di Gudang Barang Jadi:", [
                    ("1143.000 - Persediaan Barang Jadi (Finished Goods) - MDC", "3.485.000,00", "-"),
                    ("1142.000 - Persediaan Barang Dalam Proses (WIP) - MDC", "-", "3.485.000,00")
                ])
            ]
        },
        {
            "no": "5",
            "title": "Pengiriman 5 Unit Meja Belajar ke Pembeli (Delivery Note)",
            "desc": "Perusahaan mengirimkan 5 unit Meja Belajar kepada PT Graha Furniture Nusantara menggunakan Surat Jalan MAT-DN-2026-00001. Harga pokok penjualan 5 meja adalah Rp 1.742.500,00 (5 x Rp 348.500).",
            "journals": [
                ("Saat Pengiriman Fisik Meja ke Pembeli:", [
                    ("4210.000 - Harga Pokok Penjualan (HPP) - MDC", "1.742.500,00", "-"),
                    ("1143.000 - Persediaan Barang Jadi - MDC", "-", "1.742.500,00")
                ])
            ]
        },
        {
            "no": "6",
            "title": "Penerbitan Faktur Penjualan (Sales Invoice)",
            "desc": "Diterbitkan Faktur Penjualan ACC-SINV-2026-00006 kepada PT Graha Furniture Nusantara atas penjualan 5 unit meja @ Rp 550.000 = Rp 2.750.000,00.",
            "journals": [
                ("Saat Pengakuan Piutang & Pendapatan:", [
                    ("1131.000 - Piutang Usaha (Debtors) - MDC", "2.750.000,00", "-"),
                    ("4110.000 - Pendapatan Penjualan - MDC", "-", "2.750.000,00")
                ])
            ]
        },
        {
            "no": "7",
            "title": "Penerimaan Kas Pelunasan Piutang dari Pelanggan",
            "desc": "PT Graha Furniture Nusantara melunasi seluruh kewajibannya sebesar Rp 2.750.000,00 ke rekening kas perusahaan via Payment Entry ACC-PAY-2026-00006.",
            "journals": [
                ("Saat Kas Diterima di Akun Kas Besar:", [
                    ("1111.002 - Kas Besar - MDC", "2.750.000,00", "-"),
                    ("1131.000 - Piutang Usaha (Debtors) - MDC", "-", "2.750.000,00")
                ])
            ]
        },
        {
            "no": "8",
            "title": "Pencatatan Perolehan Aset Tetap Pabrik",
            "desc": "Perusahaan mendaftarkan Mesin Table Saw (ACC-ASS-2026-00001, Rp 8.500.000) dan Kompresor Cat (ACC-ASS-2026-00002, Rp 3.200.000) dengan total nilai aktiva tetap Rp 11.700.000,00.",
            "journals": [
                ("Saat Pendaftaran Aktiva Tetap Pabrik:", [
                    ("1211.001 - Aktiva Mesin & Peralatan - MDC", "11.700.000,00", "-"),
                    ("3110.000 - Modal Disetor Pemilik / Kas - MDC", "-", "11.700.000,00")
                ])
            ]
        },
        {
            "no": "9",
            "title": "Pengadaan Cadangan Bahan Baku Kayu Mahoni (Batch 2)",
            "desc": "Perusahaan membeli tambahan 20 lembar Kayu Mahoni @ Rp 118.000 = Rp 2.360.000 dari CV Kayu Lestari Abadi via PO PUR-ORD-2026-00014 dan barang diterima di gudang (MAT-PRE-2026-00004).",
            "journals": [
                ("Saat Penerimaan Bahan Baku Tambahan:", [
                    ("1141.000 - Persediaan Bahan Baku - MDC", "2.360.000,00", "-"),
                    ("2112.000 - Hutang Belum Ditagih (SRNB) - MDC", "-", "2.360.000,00")
                ])
            ]
        },
        {
            "no": "10",
            "title": "Penarikan Dana untuk Keperluan Pribadi Pemilik (Prive)",
            "desc": "Ibu Meli Dwi A melakukan penarikan uang tunai dari kas perusahaan untuk keperluan pribadi sebesar Rp 2.000.000,00 via Journal Entry ACC-JV-2026-00002.",
            "journals": [
                ("Saat Penarikan Prive Pemilik:", [
                    ("3120.000 - Prive P.Saham - MDC", "2.000.000,00", "-"),
                    ("1111.002 - Kas Besar - MDC", "-", "2.000.000,00")
                ])
            ]
        }
    ]

    for t in transactions:
        doc.add_heading(f"Kasus {t['no']}: {t['title']}", level=2)
        doc.add_paragraph(t['desc'])
        for j_title, entries in t['journals']:
            p_j = doc.add_paragraph()
            p_j.add_run(j_title).bold = True
            
            tbl = doc.add_table(rows=1, cols=3)
            tbl.style = 'Table Grid'
            tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
            hdr = tbl.rows[0].cells
            hdr[0].text = "Kode & Nama Rekening / Akun"
            hdr[1].text = "Debit (Rp)"
            hdr[2].text = "Kredit (Rp)"
            set_cell_background(hdr[0], "D9E1F2")
            set_cell_background(hdr[1], "D9E1F2")
            set_cell_background(hdr[2], "D9E1F2")
            for c in hdr:
                for p in c.paragraphs:
                    for r in p.runs:
                        r.bold = True

            for acc, deb, kre in entries:
                row = tbl.add_row().cells
                row[0].text = acc
                row[1].text = deb
                row[2].text = kre
            doc.add_paragraph()

    doc.add_heading("BAGIAN II: SOAL HITUNGAN KEUANGAN & PEMBAHASAN", level=1)
    doc.add_paragraph(
        "Soal Analisis Laba Rugi & Neraca:\n"
        "1. Hitung Harga Pokok Penjualan (HPP) per unit produk Meja Belajar (MB-001) berdasarkan BOM!\n"
        "Jawaban: Rp 120.000 (kayu) + Rp 180.000 (kaki besi) + Rp 24.000 (baut) + Rp 24.500 (cat) = Rp 348.500,00 per unit.\n\n"
        "2. Hitung Laba Kotor dan Laba Bersih dari penjualan 5 unit meja belajar!\n"
        "Jawaban: Penjualan = 5 x Rp 550.000 = Rp 2.750.000,00.\n"
        "HPP Penjualan = 5 x Rp 348.500 = Rp 1.742.500,00.\n"
        "Laba Bersih Operasional = Rp 2.750.000 - Rp 1.742.500 = Rp 1.007.500,00.\n"
        "Net Profit Margin = (Rp 1.007.500 / Rp 2.750.000) x 100% = 36,63%.\n\n"
        "3. Berapakah posisi saldo akhir Kas Besar dan total Ekuitas Pemilik di Neraca?\n"
        "Jawaban:\n"
        "- Saldo Kas Besar = Rp 2.750.000 (hasil penjualan) + Rp 30.000.000 (setoran modal) - Rp 2.000.000 (prive) = Rp 30.750.000,00.\n"
        "- Modal di Setor = Rp 30.000.000,00\n"
        "- Prive Pemilik = (Rp 2.000.000,00)\n"
        "- Laba Bersih Tahun Berjalan = Rp 1.007.500,00\n"
        "- Total Ekuitas Perusahaan = Rp 30.000.000 - Rp 2.000.000 + Rp 1.007.500 = Rp 29.007.500,00."
    )

    doc.add_heading("BAGIAN III: SOAL PILIHAN GANDA KONSEPTUAL & ANALITIS ERP", level=1)
    mc_questions = [
        ("1. Dokumen yang menjadi dasar formula kebutuhan bahan baku dan biaya produksi per unit di ERPNext adalah...",
         "A. Purchase Order | B. Bill of Materials (BOM) | C. Work Order | D. Delivery Note",
         "Kunci: B (Bill of Materials)"),
        ("2. Pada metode pencatatan persediaan perpetual, saat barang diterima fisik via Purchase Receipt, akun yang dikredit adalah...",
         "A. Kas Besar | B. Hutang Dagang Definitif | C. Hutang Belum Ditagih (SRNB) | D. Pendapatan",
         "Kunci: C (Hutang Belum Ditagih / Stock Received But Not Billed)"),
        ("3. Pengakuan beban pokok penjualan (HPP) atas barang jadi yang dikirim ke pelanggan terjadi pada saat submit dokumen...",
         "A. Customer Quotation | B. Sales Order | C. Delivery Note | D. Bank Deposit",
         "Kunci: C (Delivery Note / Surat Jalan Pengiriman Fisik)"),
        ("4. Transaksi penarikan uang tunai oleh pemilik untuk keperluan pribadi (Prive) di ERPNext dijurnal sebagai...",
         "A. Debit: Kas Besar | Kredit: Prive\nB. Debit: Prive Pemilik | Kredit: Kas Besar\nC. Debit: Beban Operasional | Kredit: Kas\nD. Debit: Hutang Dagang | Kredit: Kas",
         "Kunci: B (Debit: Prive Pemilik | Kredit: Kas Besar)")
    ]
    for q, opt, ans in mc_questions:
        p_q = doc.add_paragraph()
        p_q.add_run(f"{q}\n").bold = True
        p_q.add_run(f"{opt}\n")
        p_ans = p_q.add_run(f"{ans}\n")
        p_ans.bold = True
        p_ans.font.color.rgb = RGBColor(0, 128, 0)

    out_path = "/home/frappe/frappe-bench/sites/SOAL_DAN_JAWABAN_JURNAL_ERP.docx"
    doc.save(out_path)
    print(f"[OK] {out_path} berhasil dibuat!", flush=True)

if __name__ == "__main__":
    create_manual_docx()
    create_soal_jurnal_docx()
