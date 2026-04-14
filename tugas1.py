nama=input("MASUKKAN NAMA PENDEK ANDA :")
if nama == "Roni":
    print(f"selamat datang {nama}")
else:
    print("program selesai")
    
umur=int(input("MASUKAN UMUR ANDA :"))
#kondisi
if umur <=0:
    print("Anda belum lahir")
    print("program selesai")
elif umur>60:
    print("banyakin ibadah bentar lagi mati")
    print("program selesai")
elif umur>=18:
    print("Anda cukup umur")
    print("program selesai")
elif umur <18:
    print ("anda belum cukup umur")
    print("program selesai")
else:
    print("program selesai")