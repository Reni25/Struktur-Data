nama = input("Masukkan nama: ")
print(f"\nHalo {nama}, program validasi angka siap.")

angka = None
while angka is None or angka < 0:
    try:
        angka = int(input("Masukkan angka: "))
        if angka < 0:
            print("Harus positif!")
    except ValueError:
        print("Input salah. Masukkan angka bulat.")
        angka = None

print(f"\n terima kasih {nama}, {angka} adalah angka positif.")
print("program selesai")