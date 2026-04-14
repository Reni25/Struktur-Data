# ========================================
# PROGRAM TABEL PERKALIAN - RENI
# ========================================
print("SELAMAT DATANG!")
print("Program Tabel Perkalian\n")
# Cek nama
nama = input("Masukan nama anda: ").strip().lower()

if nama == "reni":
    print("\n nama benar! Lanjut ke tabel perkalian...")
    
    # Input angka
    angka = input("Masukkan angka (1-10): ")
    
    # Validasi angka
    try:
        angka = int(angka)
        if 1 <= angka <= 10:
            print(f"\nTABEL PERKALIAN {angka}:")
            print("-" * 20)
            
            # Tampilkan tabel
            for i in range(1, 11):
                hasil = angka * i
                print(f"{angka} × {i} = {hasil}")
                
            print("-" * 20)
            print("Selesai!")
            
        else:
            print("❌ Masukkan angka 1-10 saja!")
            
    except ValueError:
        print("❌ Harus angka!")
        
else:
    print("❌ silahkan coba lagi")

print("\nTerima kasih!")