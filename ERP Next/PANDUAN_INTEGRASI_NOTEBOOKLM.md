# PANDUAN INTEGRASI NOTEBOOKLM DENGAN SISTEM ERP MANUFAKTUR
## MEMANFAATKAN GOOGLE NOTEBOOKLM UNTUK PEMBELAJARAN, UJIAN & PODCAST AUDIO AI
### Studi Kasus: Meli Dwi Company (MDC) - Praktik ERPNext Semester 7

**Google NotebookLM** (https://notebooklm.google.com) adalah platform kecerdasan buatan dari Google yang dirancang khusus untuk membedah dokumen sumber (*grounded source documents*). Dengan mengunggah berkas proyek ERP Meli ke NotebookLM, Anda dapat:
1. **Membuat Audio Overview (Podcast AI Dua Pembicara):** Diskusi audio interaktif dalam bahasa Indonesia/Inggris yang membahas tuntas sistem ERP manufaktur Meli Dwi Company.
2. **Membuat Panduan Belajar & Kartu Tanya-Jawab Otomatis (*Study Guide & Flashcards*).**
3. **Melakukan Simulasi Ujian & Tanya-Jawab (*Q&A Chatbot*):** Bertanya mengenai jurnal akuntansi, alur BOM, laba rugi, dan transaksi ERP.

---

## 1. DAFTAR BERKAS SUMBER YANG SIAP DIUNGGAH KE NOTEBOOKLM

Seluruh berkas ini berada di folder komputer Anda:  
`c:\Users\melid\OneDrive\Documents\SEVENTH SEMESTER\ENTERPRISE RESOURCE PLANNING (ERP)\ERP_Meli\`

| Nama File | Format | Kegunaan di NotebookLM |
| :--- | :---: | :--- |
| **`LAPORAN_AKHIR_HASIL_PRAKTIK.docx`** | Word | Sumber utama profil perusahaan, hasil laba rugi Rp 1.007.500, dan neraca. |
| **`SOAL_DAN_JAWABAN_JURNAL_ERP.docx`** | Word | Sumber utama bank soal ujian, kasus perakitan meja, dan jurnal debit/kredit. |
| **`BUKU_PETUNJUK_PENGGUNAAN_ERPNEXT.docx`** | Word | Sumber teknis navigasi aplikasi web, modul Docker, dan alur tombol ERPNext. |
| **`FLOWCHART_PROSES_MANUFAKTUR.docx`** | Word | Sumber penjelasan alur diagram proses bisnis manufaktur. |
| **`SKENARIO_PRAKTIK_MANUFAKTUR.docx`** | Word | Sumber tahapan praktikum per modul dari awal hingga akhir. |

---

## 2. LANGKAH-LANGKAH INTEGRASI KE NOTEBOOKLM (HANYA 3 MENIT)

1. **Buka NotebookLM:**
   * Di browser (Google Chrome / Edge), kunjungi: **[https://notebooklm.google.com](https://notebooklm.google.com)**
   * Masuk (*Sign in*) menggunakan akun Google Anda.
2. **Buat Notebook Baru:**
   * Klik tombol **`+ New Notebook`** (Notebook Baru).
   * Beri judul notebook: **`Praktik ERP Manufaktur - Meli Dwi Company`**.
3. **Unggah Dokumen Sumber (Sources):**
   * Di panel kiri (*Add sources*), pilih opsi **Upload Files** (atau drag-and-drop).
   * Masuk ke folder:  
     `c:\Users\melid\OneDrive\Documents\SEVENTH SEMESTER\ENTERPRISE RESOURCE PLANNING (ERP)\ERP_Meli\`
   * Pilih berkas-berkas di atas (terutama **`LAPORAN_AKHIR_HASIL_PRAKTIK.docx`** dan **`SOAL_DAN_JAWABAN_JURNAL_ERP.docx`**).
   * Klik **Open** / Tunggu beberapa detik hingga proses upload selesai.

---

## 3. FITUR KUNCI YANG BISA ANDA GUNAKAN DI NOTEBOOKLM

### A. Fitur Audio Overview (Podcast Diskusi AI)
* Di panel kanan atas NotebookLM, terdapat tombol **Generate** pada bagian **Audio Overview (Deep Dive conversation)**.
* Klik **Generate**. AI akan secara otomatis memproses seluruh dokumen dan menghasilkan rekaman podcast 2 orang pembicara yang menjelaskan:
  * Apa itu Meli Dwi Company dan produk Meja Belajar `MB-001`.
  * Bagaimana resep BOM (Kayu, Kaki Besi, Baut, Cat) dihitung hingga menghasilkan HPP Rp 348.500.
  * Bagaimana penjualan 5 unit menghasilkan laba bersih Rp 1.007.500.
  * Penjelasan jurnal akuntansi saat barang diterima, dirakit, dan dijual.
* Anda bisa mendengarkan audio ini di HP/laptop sebagai media persiapan presentasi atau ujian!

### B. Prompt Rekomendasi untuk Ditanyakan ke NotebookLM
Ketikkan pertanyaan-pertanyaan berikut di kolom chat NotebookLM untuk menguji pemahaman atau mempersiapkan ujian:

1. *"Jelaskan secara ringkas bagaimana siklus manufaktur Meja Belajar MB-001 dari pengadaan bahan sampai barang jadi siap jual!"*
2. *"Sebutkan jurnal akuntansi debit dan kredit saat barang dikirim menggunakan Delivery Note dan saat pembayaran diterima via Payment Entry!"*
3. *"Berapa laba bersih yang diperoleh Meli Dwi Company dan bagaimana rincian perhitungan HPP-nya?"*
4. *"Buatkan 5 soal latihan ujian pilihan ganda beserta pembahasannya mengenai integrasi persediaan perpetual ERP!"*
5. *"Mengapa akun Modal Pemilik baru muncul setelah ada transaksi setoran modal awal?"*

### C. Membuat Ringkasan Cepat (*Briefing Doc* & *Study Guide*)
* Di menu Notebook guide di sebelah kanan, klik **Study Guide** untuk membuat panduan belajar otomatis.
* Klik **FAQ** untuk menghasilkan daftar pertanyaan umum beserta jawabannya.
