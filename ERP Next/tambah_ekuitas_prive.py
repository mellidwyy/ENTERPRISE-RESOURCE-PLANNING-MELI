import frappe
from frappe.utils import nowdate

def run():
    frappe.init('frontend', sites_path='/home/frappe/frappe-bench/sites')
    frappe.connect()
    frappe.set_user('Administrator')

    company = 'Meli Dwi Company'
    today = nowdate()

    acc_kas = '1111.002 - Kas Besar - MDC'
    acc_modal = '3110.000 - Modal di Setor - MDC'
    acc_prive = '3120.000 - Prive P.Saham - MDC'

    print("=== PENCATATAN TRANSAKSI EKUITAS & PRIVE ===", flush=True)

    # 1. Transaksi Setoran Modal Awal Pemilik (Rp 30.000.000)
    existing_modal = frappe.db.get_value("Journal Entry", {
        "company": company,
        "docstatus": 1,
        "user_remark": ["like", "%Setoran modal awal%"]
    }, "name")

    if not existing_modal:
        je_modal = frappe.get_doc({
            "doctype": "Journal Entry",
            "company": company,
            "posting_date": today,
            "voucher_type": "Journal Entry",
            "user_remark": "Setoran modal awal pendirian perusahaan oleh Meli Dwi A",
            "accounts": [
                {
                    "account": acc_kas,
                    "debit_in_account_currency": 30000000.0,
                    "credit_in_account_currency": 0.0
                },
                {
                    "account": acc_modal,
                    "debit_in_account_currency": 0.0,
                    "credit_in_account_currency": 30000000.0
                }
            ]
        })
        je_modal.insert(ignore_permissions=True)
        je_modal.submit()
        frappe.db.commit()
        print(f"[OK] Jurnal Setoran Modal Disubmit: {je_modal.name} (Rp 30.000.000,00)", flush=True)
    else:
        print(f"[EXISTS] Jurnal Setoran Modal sudah ada: {existing_modal}", flush=True)

    # 2. Transaksi Penarikan Prive Pemilik (Rp 2.000.000)
    existing_prive = frappe.db.get_value("Journal Entry", {
        "company": company,
        "docstatus": 1,
        "user_remark": ["like", "%Penarikan prive%"]
    }, "name")

    if not existing_prive:
        je_prive = frappe.get_doc({
            "doctype": "Journal Entry",
            "company": company,
            "posting_date": today,
            "voucher_type": "Journal Entry",
            "user_remark": "Penarikan prive pemilik oleh Meli Dwi A",
            "accounts": [
                {
                    "account": acc_prive,
                    "debit_in_account_currency": 2000000.0,
                    "credit_in_account_currency": 0.0
                },
                {
                    "account": acc_kas,
                    "debit_in_account_currency": 0.0,
                    "credit_in_account_currency": 2000000.0
                }
            ]
        })
        je_prive.insert(ignore_permissions=True)
        je_prive.submit()
        frappe.db.commit()
        print(f"[OK] Jurnal Penarikan Prive Disubmit: {je_prive.name} (Rp 2.000.000,00)", flush=True)
    else:
        print(f"[EXISTS] Jurnal Penarikan Prive sudah ada: {existing_prive}", flush=True)

    # 3. Tampilkan Posisi Neraca Ekuitas Terkini
    print("\n=== POSISI EKUITAS & KAS SETELAH TRANSAKSI ===", flush=True)
    gl_entries = frappe.db.sql("""
        select gle.account, sum(gle.debit - gle.credit) as debit_bal, sum(gle.credit - gle.debit) as credit_bal
        from `tabGL Entry` gle
        join `tabAccount` acc on acc.name = gle.account
        where gle.company=%s and gle.is_cancelled=0 and gle.account in (%s, %s, %s)
        group by gle.account
    """, (company, acc_kas, acc_modal, acc_prive), as_dict=True)

    for g in gl_entries:
        if g.account == acc_kas:
            print(f" * Kas Besar: Rp {g.debit_bal:,.2f} (Debit)")
        elif g.account == acc_modal:
            print(f" * Modal di Setor: Rp {g.credit_bal:,.2f} (Kredit)")
        elif g.account == acc_prive:
            print(f" * Prive Pemilik: Rp {g.debit_bal:,.2f} (Debit / Pengurang Ekuitas)")

    print("\n=== PROSES PENAMBAHAN EKUITAS & PRIVE BERHASIL 100%! ===", flush=True)

if __name__ == "__main__":
    run()
