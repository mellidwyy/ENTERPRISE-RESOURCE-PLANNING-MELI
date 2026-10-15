"""
Script Impor Otomatis Master Data Manufaktur ke ERPNext
Jalankan script ini di backend container jika ingin memasukkan master data secara otomatis.
"""
import frappe

def import_all():
    frappe.init('frontend', sites_path='/home/frappe/frappe-bench/sites')
    frappe.connect()
    frappe.set_user('Administrator')

    company = 'Meli Dwi Company'
    print(f"Mengimpor master data untuk: {company}")

    # 1. Buat Gudang
    warehouses = [
        {"warehouse_name": "Gudang Bahan Baku", "warehouse_type": "Transit"},
        {"warehouse_name": "Gudang Work In Progress", "warehouse_type": "Transit"},
        {"warehouse_name": "Gudang Barang Jadi", "warehouse_type": "Transit"}
    ]
    for wh in warehouses:
        name = f"{wh['warehouse_name']} - MDC"
        if not frappe.db.exists("Warehouse", name):
            doc = frappe.get_doc({
                "doctype": "Warehouse",
                "warehouse_name": wh['warehouse_name'],
                "company": company
            })
            doc.insert(ignore_permissions=True)
            print(f"Gudang dibuat: {wh['warehouse_name']}")

    # 2. Buat Pemasok (Suppliers)
    suppliers = ["CV Kayu Lestari Abadi", "PT Logam Perkasa Indonesia", "Toko Cat Warna Indah"]
    for s in suppliers:
        if not frappe.db.exists("Supplier", s):
            doc = frappe.get_doc({"doctype": "Supplier", "supplier_name": s, "supplier_group": "All Supplier Groups"})
            doc.insert(ignore_permissions=True)
            print(f"Supplier dibuat: {s}")

    # 3. Buat Pelanggan (Customers)
    customers = ["PT Graha Furniture Nusantara", "Yayasan Bina Prestasi Mandiri"]
    for c in customers:
        if not frappe.db.exists("Customer", c):
            doc = frappe.get_doc({"doctype": "Customer", "customer_name": c, "customer_group": "All Customer Groups", "territory": "All Territories"})
            doc.insert(ignore_permissions=True)
            print(f"Customer dibuat: {c}")

    # 4. Buat Barang (Items)
    items = [
        {"item_code": "MB-001", "item_name": "Meja Belajar Kayu Minimalis", "item_group": "Products", "stock_uom": "Nos", "is_sales_item": 1, "is_purchase_item": 0, "standard_rate": 550000},
        {"item_code": "BB-001", "item_name": "Papan Kayu Mahoni 120x60", "item_group": "Raw Material", "stock_uom": "Nos", "is_sales_item": 0, "is_purchase_item": 1, "standard_rate": 120000},
        {"item_code": "BB-002", "item_name": "Kaki Besi Hollow Meja", "item_group": "Raw Material", "stock_uom": "Nos", "is_sales_item": 0, "is_purchase_item": 1, "standard_rate": 45000},
        {"item_code": "BB-003", "item_name": "Baut & Sekrup Baja 5cm", "item_group": "Raw Material", "stock_uom": "Nos", "is_sales_item": 0, "is_purchase_item": 1, "standard_rate": 1000},
        {"item_code": "BB-004", "item_name": "Cat Vernis Natural Clear", "item_group": "Raw Material", "stock_uom": "Litre", "is_sales_item": 0, "is_purchase_item": 1, "standard_rate": 65000},
    ]
    for it in items:
        if not frappe.db.exists("Item", it['item_code']):
            doc = frappe.get_doc({
                "doctype": "Item",
                "item_code": it['item_code'],
                "item_name": it['item_name'],
                "item_group": it['item_group'],
                "stock_uom": it['stock_uom'],
                "is_stock_item": 1,
                "is_sales_item": it['is_sales_item'],
                "is_purchase_item": it['is_purchase_item'],
                "standard_rate": it['standard_rate']
            })
            doc.insert(ignore_permissions=True)
            print(f"Item dibuat: {it['item_code']}")

    frappe.db.commit()
    print("Seluruh master data berhasil diimpor!")

if __name__ == "__main__":
    import_all()
