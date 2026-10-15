import frappe
import json

def run():
    frappe.init('frontend', sites_path='/home/frappe/frappe-bench/sites')
    frappe.connect()
    frappe.set_user('Administrator')

    company = 'Meli Dwi Company'

    print("==================================================================", flush=True)
    print(f"   LAPORAN EVALUASI & KEUANGAN LENGKAP - {company.upper()}", flush=True)
    print("==================================================================\n", flush=True)

    # 1. POSISI SALDO STOK (STOCK BALANCE)
    print("1. POSISI SALDO STOK PERSIDIAAN GUDANG (STOCK BALANCE)", flush=True)
    print("-" * 66, flush=True)
    bins = frappe.get_all("Bin",
        fields=["item_code", "warehouse", "actual_qty", "stock_value", "valuation_rate"],
        filters={"actual_qty": [">", 0]},
        order_by="warehouse, item_code"
    )
    total_inventory_value = 0.0
    for b in bins:
        item_name = frappe.db.get_value("Item", b.item_code, "item_name")
        total_inventory_value += float(b.stock_value or 0)
        wh_short = b.warehouse.replace(f" - MDC", "")
        print(f" * [{wh_short}] {b.item_code} ({item_name})", flush=True)
        print(f"   Jumlah: {b.actual_qty:,.1f} | Harga Satuan: Rp {b.valuation_rate:,.2f} | Total Nilai: Rp {b.stock_value:,.2f}", flush=True)
    print(f"\n >>> TOTAL NILAI PERSEDIAAN GUDANG: Rp {total_inventory_value:,.2f}\n", flush=True)

    # 2. LAPORAN LABA RUGI (PROFIT AND LOSS)
    print("2. LAPORAN LABA RUGI (PROFIT AND LOSS STATEMENT)", flush=True)
    print("-" * 66, flush=True)
    incomes = frappe.db.sql("""
        select gle.account, sum(gle.credit - gle.debit) as balance
        from `tabGL Entry` gle
        join `tabAccount` acc on acc.name = gle.account
        where gle.company=%s and acc.root_type='Income' and gle.is_cancelled=0
        group by gle.account
    """, (company,), as_dict=True)

    total_revenue = 0.0
    print("[PENDAPATAN / REVENUE]")
    if incomes:
        for inc in incomes:
            bal = float(inc.balance or 0)
            total_revenue += bal
            print(f" * {inc.account}: Rp {bal:,.2f}", flush=True)
    else:
        print(" * Belum ada transaksi pendapatan", flush=True)
    print(f" Total Pendapatan: Rp {total_revenue:,.2f}\n", flush=True)

    expenses = frappe.db.sql("""
        select gle.account, sum(gle.debit - gle.credit) as balance
        from `tabGL Entry` gle
        join `tabAccount` acc on acc.name = gle.account
        where gle.company=%s and acc.root_type='Expense' and gle.is_cancelled=0
        group by gle.account
    """, (company,), as_dict=True)

    total_expense = 0.0
    print("[BEBAN & HARGA POKOK PENJUALAN / COGS]")
    if expenses:
        for exp in expenses:
            bal = float(exp.balance or 0)
            total_expense += bal
            print(f" * {exp.account}: Rp {bal:,.2f}", flush=True)
    else:
        print(" * Belum ada beban/HPP", flush=True)
    print(f" Total Beban / HPP: Rp {total_expense:,.2f}\n", flush=True)

    net_profit = total_revenue - total_expense
    print(f" >>> LABA BERSIH OPERASIONAL (NET PROFIT): Rp {net_profit:,.2f}\n", flush=True)

    # 3. RINGKASAN NERACA AKTIVA & EKUITAS (BALANCE SHEET HIGHLIGHTS)
    print("3. NERACA KEUANGAN PERUSAHAAN (BALANCE SHEET HIGHLIGHTS)", flush=True)
    print("-" * 66, flush=True)
    assets = frappe.db.sql("""
        select gle.account, acc.account_type, sum(gle.debit - gle.credit) as balance
        from `tabGL Entry` gle
        join `tabAccount` acc on acc.name = gle.account
        where gle.company=%s and acc.root_type='Asset' and gle.is_cancelled=0
        group by gle.account, acc.account_type
        having balance != 0
        order by acc.account_type, gle.account
    """, (company,), as_dict=True)

    total_assets = 0.0
    print("[AKTIVA / ASSETS]")
    for a in assets:
        bal = float(a.balance or 0)
        total_assets += bal
        print(f" * {a.account}: Rp {bal:,.2f}", flush=True)
    print(f" Total Aktiva: Rp {total_assets:,.2f}\n", flush=True)

    equities = frappe.db.sql("""
        select gle.account, sum(gle.credit - gle.debit) as balance
        from `tabGL Entry` gle
        join `tabAccount` acc on acc.name = gle.account
        where gle.company=%s and acc.root_type='Equity' and gle.is_cancelled=0
        group by gle.account
    """, (company,), as_dict=True)

    total_equity_direct = 0.0
    print("[EKUITAS & MODAL PEMILIK / EQUITY]")
    for eq in equities:
        bal = float(eq.balance or 0)
        total_equity_direct += bal
        print(f" * {eq.account}: Rp {bal:,.2f}", flush=True)
    
    print(f" * Laba Bersih Berjalan (Retained/Provisional Profit): Rp {net_profit:,.2f}", flush=True)
    total_net_equity = total_equity_direct + net_profit
    print(f" >>> TOTAL EKUITAS PERUSAHAAN: Rp {total_net_equity:,.2f}\n", flush=True)

    # 4. REKAPITULASI DOKUMEN SISTEM
    print("4. REKAPITULASI NOMOR DOKUMEN OPERASIONAL ERPNEXT", flush=True)
    print("-" * 66, flush=True)
    doctypes = [
        ("Purchase Order", "Pesanan Pembelian"),
        ("Purchase Receipt", "Penerimaan Barang"),
        ("Purchase Invoice", "Faktur Pembelian"),
        ("BOM", "Formula BOM Meja"),
        ("Work Order", "Perintah Kerja Produksi"),
        ("Stock Entry", "Transaksi Stok (WIP & Produksi)"),
        ("Quotation", "Penawaran Pelanggan"),
        ("Supplier Quotation", "Penawaran Pemasok"),
        ("Material Request", "Permintaan Material"),
        ("Sales Order", "Pesanan Penjualan"),
        ("Delivery Note", "Surat Jalan / Pengiriman"),
        ("Sales Invoice", "Faktur Penjualan"),
        ("Payment Entry", "Kas Masuk / Pembayaran"),
        ("Asset", "Aset Tetap Pabrik"),
        ("Journal Entry", "Jurnal Penyesuaian & Modal")
    ]
    for dt, label in doctypes:
        docs = frappe.get_all(dt, filters={"docstatus": ["in", [0, 1]]}, fields=["name", "docstatus"])
        doc_names = ", ".join([f"{d.name} ({'Draft' if d.docstatus==0 else 'Submitted'})" for d in docs])
        print(f" * {label} ({dt}): {len(docs)} Dokumen -> {doc_names}", flush=True)

    print("\n==================================================================", flush=True)
    print("   EVALUASI DENGAN EKUITAS SELESAI 100% SUKSES!", flush=True)
    print("==================================================================", flush=True)

if __name__ == "__main__":
    run()
