import frappe
from frappe.utils import nowdate, add_months
import time

def retry_op(fn, max_retries=5, delay=1.5):
    for i in range(max_retries):
        try:
            res = fn()
            frappe.db.commit()
            return res
        except Exception as e:
            print(f"Percobaan {i+1} mengalami kendala: {e}. Mengulang...", flush=True)
            try:
                frappe.db.rollback()
            except Exception:
                pass
            time.sleep(delay)
            if i == max_retries - 1:
                raise

def run():
    frappe.init('frontend', sites_path='/home/frappe/frappe-bench/sites')
    frappe.connect()
    frappe.set_user('Administrator')

    company = 'Meli Dwi Company'
    wh_raw = 'Gudang Bahan Baku - MDC'
    today = nowdate()

    print(f"=== Menjalankan Tahap 5B: Kelengkapan Operasional & Aset ({company}) ===", flush=True)

    # 1. Dokumen Permintaan Material (Material Request)
    mr_name = frappe.db.get_value("Material Request", {"company": company, "docstatus": 1}, "name")
    if not mr_name:
        def create_mr():
            mr = frappe.get_doc({
                "doctype": "Material Request",
                "company": company,
                "material_request_type": "Purchase",
                "transaction_date": today,
                "schedule_date": today,
                "items": [
                    {"item_code": "BB-001", "qty": 20, "schedule_date": today, "warehouse": wh_raw},
                    {"item_code": "BB-002", "qty": 80, "schedule_date": today, "warehouse": wh_raw},
                    {"item_code": "BB-003", "qty": 320, "schedule_date": today, "warehouse": wh_raw},
                    {"item_code": "BB-004", "qty": 10, "schedule_date": today, "warehouse": wh_raw}
                ]
            })
            mr.insert(ignore_permissions=True)
            mr.submit()
            return mr.name
        created_mr = retry_op(create_mr)
        print(f"[OK] Material Request Disubmit: {created_mr} (Rencana Produksi Gelombang 2)", flush=True)
    else:
        print(f"[EXISTS] Material Request sudah ada: {mr_name}", flush=True)

    # 2. Dokumen Penawaran dari Pemasok (Supplier Quotation)
    sq_name = frappe.db.get_value("Supplier Quotation", {"company": company, "docstatus": 1}, "name")
    if not sq_name:
        def create_sq():
            sq = frappe.get_doc({
                "doctype": "Supplier Quotation",
                "company": company,
                "supplier": "CV Kayu Lestari Abadi",
                "transaction_date": today,
                "items": [
                    {"item_code": "BB-001", "qty": 20, "rate": 118000, "warehouse": wh_raw}
                ]
            })
            sq.insert(ignore_permissions=True)
            sq.submit()
            return sq.name
        created_sq = retry_op(create_sq)
        print(f"[OK] Supplier Quotation Disubmit: {created_sq} (Dari CV Kayu Lestari Abadi)", flush=True)
    else:
        print(f"[EXISTS] Supplier Quotation sudah ada: {sq_name}", flush=True)

    # 3. Dokumen Penawaran ke Pelanggan (Customer Quotation)
    quo_name = frappe.db.get_value("Quotation", {"company": company, "docstatus": 1}, "name")
    if not quo_name:
        def create_quo():
            quo = frappe.get_doc({
                "doctype": "Quotation",
                "company": company,
                "party_name": "Yayasan Bina Prestasi Mandiri",
                "order_type": "Sales",
                "transaction_date": today,
                "valid_till": add_months(today, 1),
                "items": [
                    {"item_code": "MB-001", "qty": 15, "rate": 540000}
                ]
            })
            quo.insert(ignore_permissions=True)
            quo.submit()
            return (quo.name, quo.grand_total)
        created_quo, grand_total = retry_op(create_quo)
        print(f"[OK] Customer Quotation Disubmit: {created_quo} (Penawaran 15 Meja ke Yayasan Bina Prestasi Mandiri, Total: Rp {grand_total:,.2f})", flush=True)
    else:
        print(f"[EXISTS] Customer Quotation sudah ada: {quo_name}", flush=True)

    # 4. Modul Aset Tetap (Location, Asset Category, Items, Assets)
    if not frappe.db.exists("Location", "Pabrik Utama"):
        def create_loc():
            loc = frappe.get_doc({"doctype": "Location", "location_name": "Pabrik Utama"})
            loc.insert(ignore_permissions=True)
            return loc.name
        retry_op(create_loc)
        print("[OK] Location Dibuat: Pabrik Utama", flush=True)

    # Cari akun yang cocok untuk Fixed Asset
    fixed_asset_acc = frappe.db.get_value("Account", {"company": company, "account_type": "Fixed Asset", "is_group": 0}, "name")
    accum_depr_acc = frappe.db.get_value("Account", {"company": company, "account_type": "Accumulated Depreciation", "is_group": 0}, "name")
    depr_exp_acc = frappe.db.get_value("Account", {"company": company, "account_type": "Depreciation", "is_group": 0}, "name")

    if not fixed_asset_acc:
        fixed_asset_acc = frappe.db.get_value("Account", {"company": company, "name": ["like", "%Aktiva%"], "is_group": 0}, "name")
    if not accum_depr_acc:
        accum_depr_acc = frappe.db.get_value("Account", {"company": company, "name": ["like", "%Akumulasi%"], "is_group": 0}, "name")
    if not depr_exp_acc:
        depr_exp_acc = frappe.db.get_value("Account", {"company": company, "name": ["like", "%Peny%"], "is_group": 0}, "name")

    cat_name = "Mesin & Peralatan Pabrik"
    if not frappe.db.exists("Asset Category", cat_name):
        def create_cat():
            cat = frappe.get_doc({
                "doctype": "Asset Category",
                "asset_category_name": cat_name,
                "accounts": [
                    {
                        "company_name": company,
                        "fixed_asset_account": fixed_asset_acc,
                        "accumulated_depreciation_account": accum_depr_acc,
                        "depreciation_expense_account": depr_exp_acc
                    }
                ]
            })
            cat.insert(ignore_permissions=True)
            return cat.name
        retry_op(create_cat)
        print(f"[OK] Asset Category Dibuat: {cat_name} (Akun: {fixed_asset_acc})", flush=True)
    else:
        print(f"[EXISTS] Asset Category sudah ada: {cat_name}", flush=True)

    asset_items = [
        {"code": "AST-001", "name": "Mesin Pemotong Kayu Serbaguna (Table Saw)", "price": 8500000},
        {"code": "AST-002", "name": "Kompresor & Spray Gun Finishing Cat", "price": 3200000}
    ]
    for ai in asset_items:
        if not frappe.db.exists("Item", ai["code"]):
            def create_item():
                it = frappe.get_doc({
                    "doctype": "Item",
                    "item_code": ai["code"],
                    "item_name": ai["name"],
                    "item_group": "Products",
                    "is_stock_item": 0,
                    "is_fixed_asset": 1,
                    "asset_category": cat_name,
                    "stock_uom": "Nos"
                })
                it.insert(ignore_permissions=True)
                return it.name
            retry_op(create_item)
            print(f"[OK] Item Aset Dibuat: {ai['code']} - {ai['name']}", flush=True)

        existing_ast = frappe.db.get_value("Asset", {"item_code": ai["code"], "company": company}, "name")
        if not existing_ast:
            def create_asset():
                ast = frappe.get_doc({
                    "doctype": "Asset",
                    "asset_name": ai["name"],
                    "item_code": ai["code"],
                    "asset_category": cat_name,
                    "company": company,
                    "location": "Pabrik Utama",
                    "gross_purchase_amount": ai["price"],
                    "net_purchase_amount": ai["price"],
                    "purchase_date": today,
                    "available_for_use_date": today,
                    "calculate_depreciation": 0,
                    "asset_owner": "Company",
                    "is_existing_asset": 1
                })
                ast.insert(ignore_permissions=True)
                ast.submit()
                return ast.name
            created_ast_name = retry_op(create_asset)
            print(f"[OK] Dokumen Aset Tetap Terdaftar & Aktif: {created_ast_name} (Nilai: Rp {ai['price']:,.2f})", flush=True)
        else:
            print(f"[EXISTS] Dokumen Aset sudah ada: {existing_ast}", flush=True)

    # 5. Pengadaan Bahan Baku Gelombang 2 (Purchase Order & Receipt)
    from erpnext.buying.doctype.purchase_order.purchase_order import make_purchase_receipt
    po2_name = frappe.db.get_value("Purchase Order", {"supplier": "CV Kayu Lestari Abadi", "transaction_date": today, "docstatus": 1, "name": ["not in", ["PUR-ORD-2026-00011", "PUR-ORD-2026-00012", "PUR-ORD-2026-00013"]]}, "name")
    if not po2_name:
        def create_po_and_pr():
            po2 = frappe.get_doc({
                "doctype": "Purchase Order",
                "company": company,
                "supplier": "CV Kayu Lestari Abadi",
                "transaction_date": today,
                "schedule_date": today,
                "items": [
                    {"item_code": "BB-001", "qty": 20, "rate": 118000, "schedule_date": today, "warehouse": wh_raw}
                ]
            })
            po2.insert(ignore_permissions=True)
            po2.submit()
            frappe.db.commit()

            pr2 = make_purchase_receipt(po2.name)
            pr2.insert(ignore_permissions=True)
            pr2.submit()
            frappe.db.commit()
            return po2.name, pr2.name

        p_name, r_name = retry_op(create_po_and_pr)
        print(f"[OK] Purchase Order Gelombang 2 Disubmit: {p_name}", flush=True)
        print(f"[OK] Pengadaan Gelombang 2 Diterima: {r_name} (20 Papan Kayu Mahoni masuk ke {wh_raw})", flush=True)
    else:
        print(f"[EXISTS] Purchase Order Gelombang 2 sudah ada: {po2_name}", flush=True)

    print("=== Tahap 5B Berhasil Selesai 100%! ===", flush=True)

if __name__ == "__main__":
    run()
