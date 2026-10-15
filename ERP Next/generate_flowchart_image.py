import os
import math
from PIL import Image, ImageDraw, ImageFont

def create_flowchart():
    # Dimensions
    W, H = 2600, 1400
    img = Image.new("RGB", (W, H), "#FFFFFF")
    draw = ImageDraw.Draw(img)

    # Fonts
    font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
    font_path_reg = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

    font_title = ImageFont.truetype(font_path, 36)
    font_sub = ImageFont.truetype(font_path_reg, 20)
    font_box = ImageFont.truetype(font_path, 16)
    font_decision = ImageFont.truetype(font_path, 16)
    font_label = ImageFont.truetype(font_path, 18)

    # Colors matching reference image
    COLOR_BORDER = "#000000"
    BORDER_W = 3

    COLOR_PINK = "#FADBD8"       # Start / End Oval
    COLOR_BLUE_LIGHT = "#D4E6F1" # Parallelogram Input/Output
    COLOR_YELLOW = "#FCF3CF"     # Rectangle Process
    COLOR_ORANGE = "#FAD7A0"     # Diamond Decision
    COLOR_DOC_BLUE = "#85C1E9"   # Document shape

    # Header Title
    title_text = "FLOWCHART SISTEM MANUFAKTUR & OPERASIONAL ERPNEXT"
    sub_text = "Studi Kasus: Meli Dwi Company (MDC) - Produksi & Penjualan Meja Belajar Kayu Minimalis (MB-001)"
    draw.text((W // 2, 50), title_text, fill="#1F4E79", font=font_title, anchor="mm")
    draw.text((W // 2, 95), sub_text, fill="#555555", font=font_sub, anchor="mm")

    # Helper: Arrowhead
    def draw_arrowhead(tip_x, tip_y, direction):
        size = 12
        if direction == 'down':
            pts = [(tip_x, tip_y), (tip_x - size, tip_y - size*1.5), (tip_x + size, tip_y - size*1.5)]
        elif direction == 'up':
            pts = [(tip_x, tip_y), (tip_x - size, tip_y + size*1.5), (tip_x + size, tip_y + size*1.5)]
        elif direction == 'right':
            pts = [(tip_x, tip_y), (tip_x - size*1.5, tip_y - size), (tip_x - size*1.5, tip_y + size)]
        elif direction == 'left':
            pts = [(tip_x, tip_y), (tip_x + size*1.5, tip_y - size), (tip_x + size*1.5, tip_y + size)]
        draw.polygon(pts, fill=COLOR_BORDER)

    # Helper: Text wrap & centering
    def draw_multiline_text(cx, cy, text, font, fill="#000000"):
        lines = text.split("\n")
        line_height = font.size + 6
        total_h = len(lines) * line_height
        start_y = cy - total_h / 2 + font.size / 2
        for i, line in enumerate(lines):
            draw.text((cx, start_y + i * line_height), line, fill=fill, font=font, anchor="mm")

    # Helper: Shapes
    def draw_oval(cx, cy, w, h, fill, text):
        x0, y0, x1, y1 = cx - w//2, cy - h//2, cx + w//2, cy + h//2
        draw.ellipse([x0, y0, x1, y1], fill=fill, outline=COLOR_BORDER, width=BORDER_W)
        draw_multiline_text(cx, cy, text, font_box)

    def draw_rect(cx, cy, w, h, fill, text):
        x0, y0, x1, y1 = cx - w//2, cy - h//2, cx + w//2, cy + h//2
        draw.rectangle([x0, y0, x1, y1], fill=fill, outline=COLOR_BORDER, width=BORDER_W)
        draw_multiline_text(cx, cy, text, font_box)

    def draw_parallelogram(cx, cy, w, h, fill, text, skew=25):
        x0, y0, x1, y1 = cx - w//2, cy - h//2, cx + w//2, cy + h//2
        pts = [
            (x0 + skew, y0),
            (x1, y0),
            (x1 - skew, y1),
            (x0, y1)
        ]
        draw.polygon(pts, fill=fill, outline=COLOR_BORDER, width=BORDER_W)
        draw_multiline_text(cx, cy, text, font_box)

    def draw_diamond(cx, cy, w, h, fill, text):
        pts = [
            (cx, cy - h//2),
            (cx + w//2, cy),
            (cx, cy + h//2),
            (cx - w//2, cy)
        ]
        draw.polygon(pts, fill=fill, outline=COLOR_BORDER, width=BORDER_W)
        draw_multiline_text(cx, cy, text, font_decision)

    def draw_document(cx, cy, w, h, fill, text):
        x0, y0, x1, y1 = cx - w//2, cy - h//2, cx + w//2, cy + h//2
        wave_pts = []
        steps = 40
        for i in range(steps + 1):
            t = i / steps
            wx = x1 - t * w
            wy = y1 + math.sin(t * math.pi * 2) * 9
            wave_pts.append((wx, wy))
        
        pts = [(x0, y0), (x1, y0)] + wave_pts + [(x0, y1)]
        draw.polygon(pts, fill=fill, outline=COLOR_BORDER, width=BORDER_W)
        draw_multiline_text(cx, cy - 5, text, font_box)

    def draw_connector(cx, cy, r=22):
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill="#FFFFFF", outline=COLOR_BORDER, width=BORDER_W)
        offset = int(r * 0.7)
        draw.line([cx - offset, cy - offset, cx + offset, cy + offset], fill=COLOR_BORDER, width=2)
        draw.line([cx - offset, cy + offset, cx + offset, cy - offset], fill=COLOR_BORDER, width=2)

    # -------------------------------------------------------------
    # LAYOUT COORDINATES & SIZES
    # -------------------------------------------------------------
    col1_x = 420
    col2_x = 1220
    col3_x = 2050

    w_std = 250
    h_std = 85

    # ---------------- COLUMN 1 (PENGADAAN & RESEP) ----------------
    # 1. Start Oval
    draw_oval(col1_x, 175, 170, 65, COLOR_PINK, "Start")

    # Arrow to Rencana Produksi
    draw.line([col1_x, 207, col1_x, 245], fill=COLOR_BORDER, width=BORDER_W)
    draw_arrowhead(col1_x, 245, 'down')

    # 2. Parallelogram: Rencana Produksi
    draw_parallelogram(col1_x, 288, w_std, h_std, COLOR_BLUE_LIGHT, "Rencana Produksi\nMeja (MB-001)")

    # Arrow to Cek Resep
    draw.line([col1_x, 331, col1_x, 370], fill=COLOR_BORDER, width=BORDER_W)
    draw_arrowhead(col1_x, 370, 'down')

    # 3. Rectangle: Cek Resep BOM
    draw_rect(col1_x, 412, w_std, h_std, COLOR_YELLOW, "Cek Resep BOM\n(BOM-MB-001-001)")

    # Arrow to Hitung Kebutuhan
    draw.line([col1_x, 455, col1_x, 495], fill=COLOR_BORDER, width=BORDER_W)
    draw_arrowhead(col1_x, 495, 'down')

    # 4. Rectangle: Hitung Kebutuhan Bahan
    draw_rect(col1_x, 537, w_std, h_std, COLOR_YELLOW, "Hitung Kebutuhan\nBahan Baku")

    # Arrow to Terbitkan PO
    draw.line([col1_x, 580, col1_x, 620], fill=COLOR_BORDER, width=BORDER_W)
    draw_arrowhead(col1_x, 620, 'down')

    # 5. Rectangle: Terbitkan PO
    draw_rect(col1_x, 662, w_std, h_std, COLOR_YELLOW, "Terbitkan Purchase Order\n(PUR-ORD)")

    # Arrow right to Document: Penerimaan Barang
    doc_x = 760
    draw.line([col1_x + w_std//2, 662, doc_x - 105, 662], fill=COLOR_BORDER, width=BORDER_W)
    draw_arrowhead(doc_x - 105, 662, 'right')
    draw_document(doc_x, 662, 210, 85, COLOR_DOC_BLUE, "Penerimaan Barang\n(Purchase Receipt)")

    # Arrow down from PO to Rilis Work Order
    draw.line([col1_x, 705, col1_x, 755], fill=COLOR_BORDER, width=BORDER_W)
    draw_arrowhead(col1_x, 755, 'down')

    # 6. Parallelogram: Rilis Work Order
    draw_parallelogram(col1_x, 798, w_std, h_std, COLOR_BLUE_LIGHT, "Rilis Work Order\n(MFG-WO-2026-00001)")

    # Arrow from Work Order -> up and right to Connector ⊗
    conn_x = 1000
    conn_y = 230
    draw.line([col1_x + w_std//2 - 10, 798, 920, 798], fill=COLOR_BORDER, width=BORDER_W)
    draw.line([920, 798, 920, conn_y], fill=COLOR_BORDER, width=BORDER_W)
    draw.line([920, conn_y, conn_x - 22, conn_y], fill=COLOR_BORDER, width=BORDER_W)
    draw_arrowhead(conn_x - 22, conn_y, 'right')

    # ---------------- COLUMN 2 (LANTAI PRODUKSI) ----------------
    # 7. Connector
    draw_connector(conn_x, conn_y)

    # Arrow from Connector to Transfer ke WIP
    draw.line([conn_x + 22, conn_y, col2_x - w_std//2, conn_y], fill=COLOR_BORDER, width=BORDER_W)
    draw_arrowhead(col2_x - w_std//2, conn_y, 'right')

    # 8. Rectangle: Transfer ke WIP & Perakitan Meja
    draw_rect(col2_x, conn_y, w_std, h_std, COLOR_YELLOW, "Transfer Bahan ke WIP\n& Perakitan Meja")

    # Arrow down to Diamond 1: Selesai Dirakit?
    dia_y = 405
    draw.line([col2_x, conn_y + h_std//2, col2_x, dia_y - 60], fill=COLOR_BORDER, width=BORDER_W)
    draw_arrowhead(col2_x, dia_y - 60, 'down')

    # 9. Diamond 1: Selesai Dirakit?
    draw_diamond(col2_x, dia_y, 220, 120, COLOR_ORANGE, "Perakitan\nSelesai?")

    # 10. Diamond 2: Ada Cacat Produksi?
    dia2_x = 1630
    draw_diamond(dia2_x, dia_y, 220, 120, COLOR_ORANGE, "Ada Cacat\nProduksi?")

    # 11. Diamond 3: Pesanan Masuk?
    dia3_x = col3_x
    draw_diamond(dia3_x, dia_y, 220, 120, COLOR_ORANGE, "Pesanan Sales\nOrder Masuk?")

    # Horizontal connection: Diamond 1 -> Diamond 2 ("No")
    draw.line([col2_x + 110, dia_y, dia2_x - 110, dia_y], fill=COLOR_BORDER, width=BORDER_W)
    draw_arrowhead(dia2_x - 110, dia_y, 'right')
    draw.text((col2_x + 150, dia_y - 28), "No", fill=COLOR_BORDER, font=font_label)

    # Horizontal connection: Diamond 2 -> Diamond 3 ("No")
    draw.line([dia2_x + 110, dia_y, dia3_x - 110, dia_y], fill=COLOR_BORDER, width=BORDER_W)
    draw_arrowhead(dia3_x - 110, dia_y, 'right')
    draw.text((dia2_x + 150, dia_y - 28), "No", fill=COLOR_BORDER, font=font_label)

    # Diamond 1 -> Down to Stock Entry Manufacture ("Yes")
    box_vac_y = 590
    draw.line([col2_x, dia_y + 60, col2_x, box_vac_y - h_std//2], fill=COLOR_BORDER, width=BORDER_W)
    draw_arrowhead(col2_x, box_vac_y - h_std//2, 'down')
    draw.text((col2_x + 18, dia_y + 70), "Yes", fill=COLOR_BORDER, font=font_label)

    # Diamond 2 -> Down and left to Stock Entry Manufacture ("Yes")
    draw.line([dia2_x, dia_y + 60, dia2_x, box_vac_y], fill=COLOR_BORDER, width=BORDER_W)
    draw.line([dia2_x, box_vac_y, col2_x + w_std//2, box_vac_y], fill=COLOR_BORDER, width=BORDER_W)
    draw_arrowhead(col2_x + w_std//2, box_vac_y, 'left')
    draw.text((dia2_x + 18, dia_y + 70), "Yes", fill=COLOR_BORDER, font=font_label)

    # 12. Parallelogram: Stock Entry Manufacture
    draw_parallelogram(col2_x, box_vac_y, w_std + 20, h_std, COLOR_BLUE_LIGHT, "Stock Entry Manufacture\n(10 Unit Meja Jadi)")

    # Arrow down to Simpan ke Gudang Barang Jadi
    ret_y = 760
    draw.line([col2_x, box_vac_y + h_std//2, col2_x, ret_y - h_std//2], fill=COLOR_BORDER, width=BORDER_W)
    draw_arrowhead(col2_x, ret_y - h_std//2, 'down')

    # 13. Rectangle: Simpan ke Gudang Barang Jadi
    draw_rect(col2_x, ret_y, w_std, h_std, COLOR_YELLOW, "Simpan ke Gudang\nBarang Jadi (FG)")

    # Arrow down to Produk Siap Kirim
    pwr_y = 930
    draw.line([col2_x, ret_y + h_std//2, col2_x, pwr_y - h_std//2], fill=COLOR_BORDER, width=BORDER_W)
    draw_arrowhead(col2_x, pwr_y - h_std//2, 'down')

    # 14. Parallelogram: Produk Siap Kirim
    draw_parallelogram(col2_x, pwr_y, w_std, h_std, COLOR_BLUE_LIGHT, "Produk Siap Kirim\n& Saldo FG Aktif")

    # Arrow down to End
    end_y = 1090
    draw.line([col2_x, pwr_y + h_std//2, col2_x, end_y - 32], fill=COLOR_BORDER, width=BORDER_W)
    draw_arrowhead(col2_x, end_y - 32, 'down')

    # 15. Oval: End
    draw_oval(col2_x, end_y, 170, 65, COLOR_PINK, "End")

    # ---------------- COLUMN 3 (PENJUALAN & KEUANGAN) ----------------
    # Diamond 3 "No" branch -> Loops UP and LEFT back to Transfer ke WIP
    loop_top_y = 135
    draw.line([dia3_x, dia_y - 60, dia3_x, loop_top_y], fill=COLOR_BORDER, width=BORDER_W)
    draw.line([dia3_x, loop_top_y, col2_x, loop_top_y], fill=COLOR_BORDER, width=BORDER_W)
    draw.line([col2_x, loop_top_y, col2_x, conn_y - h_std//2], fill=COLOR_BORDER, width=BORDER_W)
    draw_arrowhead(col2_x, conn_y - h_std//2, 'down')
    draw.text((dia3_x + 18, dia_y - 90), "No", fill=COLOR_BORDER, font=font_label)

    # Diamond 3 "Yes" branch -> Down to Delivery Note
    draw.line([dia3_x, dia_y + 60, dia3_x, box_vac_y - h_std//2], fill=COLOR_BORDER, width=BORDER_W)
    draw_arrowhead(dia3_x, box_vac_y - h_std//2, 'down')
    draw.text((dia3_x + 18, dia_y + 70), "Yes", fill=COLOR_BORDER, font=font_label)

    # 16. Parallelogram: Kirim 5 Meja via Delivery Note
    draw_parallelogram(col3_x, box_vac_y, w_std, h_std, COLOR_BLUE_LIGHT, "Kirim 5 Meja via\nDelivery Note (DN)")

    # Arrow down to Sales Invoice
    draw.line([col3_x, box_vac_y + h_std//2, col3_x, ret_y - h_std//2], fill=COLOR_BORDER, width=BORDER_W)
    draw_arrowhead(col3_x, ret_y - h_std//2, 'down')

    # 17. Rectangle: Faktur Penjualan Sales Invoice
    draw_rect(col3_x, ret_y, w_std, h_std, COLOR_YELLOW, "Terbitkan Faktur\nSales Invoice (Tagihan)")

    # Arrow down to Payment Entry
    draw.line([col3_x, ret_y + h_std//2, col3_x, pwr_y - h_std//2], fill=COLOR_BORDER, width=BORDER_W)
    draw_arrowhead(col3_x, pwr_y - h_std//2, 'down')

    # 18. Parallelogram: Kas Masuk Payment Entry
    draw_parallelogram(col3_x, pwr_y, w_std, h_std, COLOR_BLUE_LIGHT, "Kas Masuk Rp 2.75M\n(Payment Entry)")

    # Arrow from Payment Entry LEFT to Produk Siap Kirim
    draw.line([col3_x - w_std//2, pwr_y, col2_x + w_std//2, pwr_y], fill=COLOR_BORDER, width=BORDER_W)
    draw_arrowhead(col2_x + w_std//2, pwr_y, 'left')

    # Save PNG
    out_png = "/home/frappe/frappe-bench/sites/FLOWCHART_MANUFAKTUR_ERPNEXT.png"
    img.save(out_png, "PNG", dpi=(300, 300))
    print(f"[OK] Refined Flowchart PNG berhasil dibuat: {out_png}", flush=True)

    # ALSO CREATE THE WORD DOCX EMBEDDING THE FLOWCHART
    try:
        from docx import Document
        from docx.shared import Inches, Pt, RGBColor
        from docx.enum.text import WD_ALIGN_PARAGRAPH
        from docx.enum.section import WD_SECTION, WD_ORIENT
        from docx.enum.table import WD_TABLE_ALIGNMENT
        from docx.oxml import OxmlElement
        from docx.oxml.ns import qn

        doc = Document()
        # Set landscape orientation
        section = doc.sections[0]
        section.orientation = WD_ORIENT.LANDSCAPE
        section.page_width = Inches(11.69)   # A4 Landscape width
        section.page_height = Inches(8.27)  # A4 Landscape height
        section.top_margin = Inches(0.6)
        section.bottom_margin = Inches(0.6)
        section.left_margin = Inches(0.8)
        section.right_margin = Inches(0.8)

        # Title
        p_title = doc.add_paragraph()
        p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r1 = p_title.add_run("DIAGRAM ALIR SISTEM MANUFAKTUR & OPERASIONAL ERPNEXT\n")
        r1.bold = True
        r1.font.size = Pt(16)
        r1.font.color.rgb = RGBColor(31, 78, 121)

        r2 = p_title.add_run("Studi Kasus: Meli Dwi Company (MDC) - Produksi Meja Belajar Kayu Minimalis (MB-001)\n")
        r2.italic = True
        r2.font.size = Pt(11)
        r2.font.color.rgb = RGBColor(80, 80, 80)

        # Add image
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.add_run().add_picture(out_png, width=Inches(10.0))

        # Add Legend & Explanation Table
        p_desc = doc.add_paragraph()
        p_desc.add_run("Keterangan Simbol & Alur Proses Bisnis:").bold = True
        
        tbl = doc.add_table(rows=1, cols=4)
        tbl.style = 'Table Grid'
        tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        hdr = tbl.rows[0].cells
        hdr[0].text = "Bentuk / Simbol"
        hdr[1].text = "Warna"
        hdr[2].text = "Arti Standar ISO"
        hdr[3].text = "Penerapan pada Sistem ERPNext MDC"
        for c in hdr:
            for p in c.paragraphs:
                for r in p.runs:
                    r.bold = True

        symbols = [
            ("Oval (Terminator)", "Merah Muda (Pink)", "Titik Awal & Akhir Proses", "Start: Perencanaan Awal | End: Transaksi Tuntas"),
            ("Jajaran Genjang (Parallelogram)", "Biru Muda (Light Blue)", "Input / Output Operasional", "Input Rencana, Dokumen PO, Work Order, DN, Kas Masuk"),
            ("Persegi Panjang (Process)", "Kuning (Yellow)", "Aktivitas / Proses Pengolahan", "Cek Resep BOM, Perakitan Meja di WIP, Terbitkan Faktur"),
            ("Belah Ketupat (Diamond)", "Jingga (Orange)", "Pengambilan Keputusan (Decision)", "Perakitan Selesai?, Ada Cacat QC?, Pesanan Masuk?"),
            ("Bentuk Dokumen (Document)", "Biru Medium", "Pencatatan Dokumen Fisik / Cetak", "Bukti Penerimaan Barang (Purchase Receipt)"),
            ("Lingkaran Silang (Connector ⊗)", "Putih", "Penghubung Antar Alur Kerja", "Integrasi Pengadaan ke Antrean Lantai Pabrik"),
        ]
        for shape, col, mean, impl in symbols:
            row = tbl.add_row().cells
            row[0].text = shape
            row[1].text = col
            row[2].text = mean
            row[3].text = impl

        out_docx = "/home/frappe/frappe-bench/sites/FLOWCHART_PROSES_MANUFAKTUR.docx"
        doc.save(out_docx)
        print(f"[OK] Flowchart DOCX berhasil dibuat: {out_docx}", flush=True)

    except Exception as e:
        print(f"[ERR] Gagal membuat docx: {e}", flush=True)

if __name__ == "__main__":
    create_flowchart()
