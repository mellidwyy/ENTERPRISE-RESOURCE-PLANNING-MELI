import os
import sys

try:
    import docx
    from docx import Document
    from docx.shared import Inches, Pt, RGBColor
    from docx.enum.text import WD_ALIGN_PARAGRAPH
except ImportError:
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "python-docx"])
    import docx
    from docx import Document
    from docx.shared import Inches, Pt, RGBColor
    from docx.enum.text import WD_ALIGN_PARAGRAPH

def create_report_docx():
    doc = Document()

    # Page Margins
    for section in doc.sections:
        section.top_margin = Inches(1)
        section.bottom_margin = Inches(1)
        section.left_margin = Inches(1)
        section.right_margin = Inches(1)

    # Title
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run_t1 = p_title.add_run("LAPORAN AKHIR PRAKTIK ERP\n")
    run_t1.bold = True
    run_t1.font.size = Pt(18)
    run_t1.font.color.rgb = RGBColor(31, 78, 121)

    run_t2 = p_title.add_run("IMPLEMENTASI SISTEM ERPNEXT INDUSTRI MANUFAKTUR\n")
    run_t2.bold = True
    run_t2.font.size = Pt(14)
    run_t2.font.color.rgb = RGBColor(46, 117, 182)

    run_t3 = p_title.add_run("Studi Kasus: Produksi & Penjualan Meja Belajar Kayu Minimalis (MB-001)\n\n")
    run_t3.font.size = Pt(12)
    run_t3.font.italic = True

    # Info Box
    p_info = doc.add_paragraph()
    p_info.add_run("Perusahaan: ").bold = True
    p_info.add_run("Meli Dwi Company (MDC)\n")
    p_info.add_run("Administrator: ").bold = True
    p_info.add_run("Meli Dwi A (melidwyy@gmail.com)\n")
    p_info.add_run("Aplikasi / Versi: ").bold = True
    p_info.add_run("ERPNext v16 (Frappe Docker Stack)\n")
    p_info.add_run("URL Server: ").bold = True
    p_info.add_run("http://localhost:8080\n")
    p_info.add_run("Status Proyek: ").bold = True
    p_info.add_run("Selesai 100% (Tahap 1 s/d Tahap 6 + Ekuitas & Prive)\n")

    doc.add_heading("1. Ringkasan Hasil Eksekusi Siklus Manufaktur & Keuangan", level=1)
    
    table_summary = doc.add_table(rows=1, cols=4)
    table_summary.style = 'Table Grid'
    hdr = table_summary.rows[0].cells
    hdr[0].text = "Tahap"
    hdr[1].text = "Modul / Aktivitas"
    hdr[2].text = "Dokumen Kunci"
    hdr[3].text = "Status"
    for cell in hdr:
        for p in cell.paragraphs:
            for r in p.runs:
                r.bold = True

    data_summary = [
        ("Tahap 1", "Master Data", "3 Gudang, 5 Item, 3 Pemasok, 2 Pelanggan", "Selesai"),
        ("Tahap 2", "Pengadaan Bahan Awal", "PUR-ORD-00011-13, MAT-PRE-00001-3", "Selesai"),
        ("Tahap 3", "Formula Resep (BOM)", "BOM-MB-001-001 (Rp 348.500/unit)", "Selesai"),
        ("Tahap 4", "Produksi Manufaktur", "MFG-WO-00001 (10 Unit Meja Jadi)", "Selesai"),
        ("Tahap 5", "Penjualan Produk", "SAL-ORD-00006, DN-00001, PINV, Kas Masuk", "Selesai"),
        ("Tahap 5B", "Operasional & Aset", "MR-00001, Penawaran, Aset Tetap Pabrik", "Selesai"),
        ("Tahap 5C", "Ekuitas & Prive Pemilik", "ACC-JV-00001 (Modal 30M), ACC-JV-00002 (Prive 2M)", "Selesai"),
        ("Tahap 6", "Laporan Keuangan", "Laba Bersih Rp 1.007.500, Posisi Stok & Neraca Lengkap", "Selesai"),
    ]
    for row_data in data_summary:
        row = table_summary.add_row().cells
        for i, val in enumerate(row_data):
            row[i].text = val

    doc.add_heading("2. Formula Resep Produksi (Bill of Materials)", level=1)
    p_bom = doc.add_paragraph("Pembuatan 1 unit Meja Belajar Kayu Minimalis (MB-001) memerlukan bahan baku:")
    
    table_bom = doc.add_table(rows=1, cols=4)
    table_bom.style = 'Table Grid'
    hdr_b = table_bom.rows[0].cells
    hdr_b[0].text = "Kode Bahan"
    hdr_b[1].text = "Nama Bahan"
    hdr_b[2].text = "Kebutuhan"
    hdr_b[3].text = "Biaya Satuan (Rp)"
    for cell in hdr_b:
        for p in cell.paragraphs:
            for r in p.runs:
                r.bold = True

    bom_data = [
        ("BB-001", "Papan Kayu Mahoni 120x60", "1 Lembar", "120.000"),
        ("BB-002", "Kaki Meja Besi Hollow", "4 Batang", "180.000 (45.000/btg)"),
        ("BB-003", "Baut & Sekrup Baja", "16 Pcs", "24.000 (1.500/pc)"),
        ("BB-004", "Cat Vernis Wood Finish", "0.5 Liter", "24.500 (49.000/L)"),
    ]
    for b in bom_data:
        r = table_bom.add_row().cells
        for i, val in enumerate(b):
            r[i].text = val

    p_tot_bom = doc.add_paragraph()
    r_tb = p_tot_bom.add_run("Total Biaya Pokok Produksi (HPP Standar) per Meja: Rp 348.500,00\n")
    r_tb.bold = True

    doc.add_heading("3. Laporan Keuangan, Laba Rugi & Neraca Ekuitas (Tahap 6)", level=1)
    
    p_fin = doc.add_paragraph()
    p_fin.add_run("A. Laporan Laba Rugi (Profit & Loss Statement):\n").bold = True
    p_fin.add_run(" * Pendapatan Penjualan (5 Meja @ Rp 550.000): ").font.size = Pt(11)
    p_fin.add_run("Rp 2.750.000,00\n").bold = True
    p_fin.add_run(" * Harga Pokok Penjualan (5 Meja @ Rp 348.500): ").font.size = Pt(11)
    p_fin.add_run("(Rp 1.742.500,00)\n").bold = True
    r_laba = p_fin.add_run(" * LABA BERSIH OPERASIONAL: Rp 1.007.500,00 (Net Margin: 36,63%)\n\n")
    r_laba.bold = True
    r_laba.font.color.rgb = RGBColor(0, 128, 0)

    p_fin.add_run("B. Saldo Persediaan Barang di Gudang (Stock Balance):\n").bold = True
    p_fin.add_run(" * Gudang Bahan Baku: 20 lembar Kayu Mahoni (Batch 2) = Rp 2.360.000,00\n")
    p_fin.add_run(" * Gudang Barang Jadi: 5 unit Meja Belajar siap jual = Rp 1.742.500,00\n")
    p_fin.add_run(" * Gudang WIP: 0 unit (seluruh material telah selesai dirakit)\n")
    p_fin.add_run(" * Total Nilai Persediaan Meli Dwi Company: Rp 4.102.500,00\n\n")

    p_fin.add_run("C. Posisi Aktiva & Ekuitas Perusahaan (Balance Sheet Highlights):\n").bold = True
    p_fin.add_run(" [AKTIVA / ASSETS]\n").bold = True
    p_fin.add_run(" * Kas Besar (1111.002): Rp 30.750.000,00 (Penjualan 2.75M + Modal 30M - Prive 2M)\n")
    p_fin.add_run(" * Persediaan Barang (1141.000): Rp 4.102.500,00\n")
    p_fin.add_run(" * Total Aktiva Lancar: Rp 34.852.500,00\n")
    p_fin.add_run(" * Aset Tetap Pabrik (Mesin Saw & Kompresor): Rp 11.700.000,00\n")
    r_tot_ast = p_fin.add_run(" * TOTAL ASET USAHA: Rp 46.552.500,00\n\n")
    r_tot_ast.bold = True

    p_fin.add_run(" [EKUITAS & MODAL PEMILIK / EQUITY]\n").bold = True
    p_fin.add_run(" * Modal di Setor (3110.000 - ACC-JV-2026-00001): Rp 30.000.000,00\n")
    p_fin.add_run(" * Penarikan Prive Pemilik (3120.000 - ACC-JV-2026-00002): (Rp 2.000.000,00)\n")
    p_fin.add_run(" * Modal Bersih Pemilik: Rp 28.000.000,00\n")
    p_fin.add_run(" * Laba Bersih Tahun Berjalan (Provisional Profit): Rp 1.007.500,00\n")
    r_tot_eq = p_fin.add_run(" * TOTAL EKUITAS PERUSAHAAN: Rp 29.007.500,00\n")
    r_tot_eq.bold = True
    r_tot_eq.font.color.rgb = RGBColor(31, 78, 121)

    doc.add_heading("4. Kesimpulan", level=1)
    p_kesimpulan = doc.add_paragraph(
        "Sistem ERPNext berhasil merepresentasikan keseluruhan rantai nilai (value chain) "
        "industri manufaktur perabot mebel secara end-to-end. Aliran informasi, pergerakan "
        "persediaan bahan baku dan barang jadi, pencatatan ekuitas modal serta penarikan prive, "
        "dan jurnal akuntansi otomatis terintegrasi dengan sempurna tanpa selisih data."
    )

    output_path = "/home/frappe/frappe-bench/sites/LAPORAN_AKHIR_HASIL_PRAKTIK.docx"
    doc.save(output_path)
    print(f"[OK] File docx berhasil dibuat di: {output_path}", flush=True)

if __name__ == "__main__":
    create_report_docx()
