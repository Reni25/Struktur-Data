# Inisialisasi data awal sesuai contoh
data_mahasiswa = [
    ["Ahmad", 85],
    ["Budi", 78],
    ["Citra", 90]
]

def tampilkan_data():
    print("\n--- Daftar Data Mahasiswa ---")
    if not data_mahasiswa:
        print("Data masih kosong.")
    else:
        print(f"{'No':<3} | {'Nama':<15} | {'Nilai'}")
        print("-" * 30)
        for i, mhs in enumerate(data_mahasiswa, start=1):
            print(f"{i:<3} | {mhs[0]:<15} | {mhs[1]}")
    print("-" * 30)

def tambah_data():
    print("\n--- Tambah Data Mahasiswa ---")
    nama = input("Masukkan nama mahasiswa: ").strip().title()
    try:
        nilai = float(input("Masukkan nilai mahasiswa: "))
        data_mahasiswa.append([nama, nilai])
        print(f" Data {nama} berhasil ditambahkan!")
    except ValueError:
        print(" Error: Nilai harus berupa angka!")

def ubah_data():
    print("\n--- Ubah Data Mahasiswa ---")
    nama_cari = input("Masukkan nama mahasiswa yang ingin diubah: ").strip().title()
    
    for mhs in data_mahasiswa:
        if mhs[0] == nama_cari:
            print(f"Ditemukan: {mhs[0]} dengan nilai {mhs[1]}")
            nama_baru = input("Masukkan nama baru (kosongkan jika tidak diubah): ").strip().title()
            nilai_baru_str = input("Masukkan nilai baru (kosongkan jika tidak diubah): ").strip()
            
            if nama_baru:
                mhs[0] = nama_baru
            if nilai_baru_str:
                try:
                    mhs[1] = float(nilai_baru_str)
                except ValueError:
                    print(" Error: Nilai baru harus berupa angka! Perubahan nilai dibatalkan.")
            
            print(" Data berhasil diubah!")
            return
            
    print(" Data mahasiswa tidak ditemukan.")

def hapus_data():
    print("\n--- Hapus Data Mahasiswa ---")
    nama_cari = input("Masukkan nama mahasiswa yang ingin dihapus: ").strip().title()
    
    for mhs in data_mahasiswa:
        if mhs[0] == nama_cari:
            data_mahasiswa.remove(mhs)
            print(f"Data {nama_cari} berhasil dihapus!")
            return
            
    print(" Data mahasiswa tidak ditemukan.")

def cari_data():
    print("\n--- Cari Data Mahasiswa ---")
    nama_cari = input("Masukkan nama mahasiswa yang dicari: ").strip().title()
    ditemukan = False
    
    for mhs in data_mahasiswa:
        if mhs[0] == nama_cari:
            print(f" Ditemukan: Nama = {mhs[0]}, Nilai = {mhs[1]}")
            ditemukan = True
            
    if not ditemukan:
        print(" Data mahasiswa tidak ditemukan.")

def urutkan_data():
    print("\n--- Urutkan Data Berdasarkan Nilai Tertinggi ---")
    # Mengurutkan list berdasarkan elemen indeks ke-1 (Nilai), secara descending (tertinggi ke terendah)
    data_mahasiswa.sort(key=lambda x: x[1], reverse=True)
    print(" Data berhasil diurutkan!")
    tampilkan_data() # Panggil fungsi tampilkan_data agar user langsung melihat hasilnya

def hitung_rata_rata():
    print("\n--- Hitung Rata-rata Nilai ---")
    if not data_mahasiswa:
        print("Tidak ada data untuk dihitung.")
        return
    
    total_nilai = sum(mhs[1] for mhs in data_mahasiswa)
    rata_rata = total_nilai / len(data_mahasiswa)
    print(f"Total Mahasiswa: {len(data_mahasiswa)}")
    print(f"Rata-rata Nilai: {rata_rata:.2f}")

def main():
    while True:
        print("\n====================================")
        print(" APLIKASI MANAJEMEN NILAI MAHASISWA")
        print("====================================")
        print("1. Tampilkan Data")
        print("2. Tambah Data")
        print("3. Ubah Data")
        print("4. Hapus Data")
        print("5. Cari Data")
        print("6. Urutkan Data Berdasarkan Nilai")
        print("7. Hitung Rata-rata Nilai")
        print("8. Keluar")
        
        pilihan = input("Pilih menu 1-8: ").strip()
        
        if pilihan == '1':
            tampilkan_data()
        elif pilihan == '2':
            tambah_data()
        elif pilihan == '3':
            ubah_data()
        elif pilihan == '4':
            hapus_data()
        elif pilihan == '5':
            cari_data()
        elif pilihan == '6':
            urutkan_data()
        elif pilihan == '7':
            hitung_rata_rata()
        elif pilihan == '8':
            print("\n Terima kasih telah menggunakan Aplikasi Manajemen Nilai. Sampai jumpa!")
            break
        else:
            print("\n Pilihan tidak valid! Silakan pilih angka 1-8.")

# Menjalankan program utama
if __name__ == "__main__":
    main()