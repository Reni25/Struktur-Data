# Data Awal Mahasiswa
data_mahasiswa = [
    ["Ahmad", 85],
    ["Budi", 78],
    ["Citra", 90]
]
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

    pilih = input("Pilih menu 1-8: ")
    # 1. Tampilkan Data
    if pilih == '1':
        print("\n--- Daftar Mahasiswa ---")
        for m in data_mahasiswa:
            print(f"Nama: {m[0]}, Nilai: {m[1]}")
    # 2. Tambah Data
    elif pilih == '2':
        nama = input("Masukkan nama: ")
        nilai = int(input("Masukkan nilai: "))
        data_mahasiswa.append([nama, nilai])
        print(" Data berhasil ditambahkan!")
    # 3. Ubah Data
    elif pilih == '3':
        cari = input("Nama yang diubah: ")
        for m in data_mahasiswa:
            if m[0] == cari:
                m[0] = input("Nama baru: ")
                m[1] = int(input("Nilai baru: "))
                print(" Data berhasil diubah!")
                break
        else:
            print(" Data tidak ditemukan.")
    # 4. Hapus Data
    elif pilih == '4':
        cari = input("Nama yang dihapus: ")
        for m in data_mahasiswa:
            if m[0] == cari:
                data_mahasiswa.remove(m)
                print(" Data berhasil dihapus!")
                break
        else:
            print(" Data tidak ditemukan.")
    # 5. Cari Data
    elif pilih == '5':
        cari = input("Nama yang dicari: ")
        for m in data_mahasiswa:
            if m[0] == cari:
                print(f" Ditemukan: {m[0]} (Nilai: {m[1]})")
                break
        else:
            print(" Data tidak ditemukan.")
    # 6. Urutkan Data (Hasil Langsung Muncul)
    elif pilih == '6':
        data_mahasiswa.sort(key=lambda x: x[1], reverse=True)
        print("\n Hasil Pengurutan (Tertinggi ke Terendah):")
        for m in data_mahasiswa:
            print(f"Nama: {m[0]}, Nilai: {m[1]}")
    # 7. Hitung Rata-rata (Hasil Langsung Muncul)
    elif pilih == '7':
        if data_mahasiswa:
            total = sum(m[1] for m in data_mahasiswa)
            rata = total / len(data_mahasiswa)
            print(f"\n Rata-rata Nilai: {rata:.2f}")
        else:
            print("\n Data masih kosong.")
    # 8. Keluar
    elif pilih == '8':
        print("\n Keluar dari program. Terima kasih!")
        break

    else:
        print("\n Pilihan tidak valid!")