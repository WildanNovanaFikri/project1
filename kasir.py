print("===============RESTORAN PAK MBUD===============")
pembeli = input("Nama Pembeli : ")
print('Nama Pembeli : ')

def makanan():
    global totalmakanan
    global porsi
    global makan
    print("\n===============MENU MAKANAN===============\n")
    print("1. Nasi Ayam Goreng - Rp.20000")
    print("2. Nasi Goreng - Rp.13000")
    print("3. Bakso - Rp.15000")
    print("4. Mie Ayam - Rp.10000")
    print("5. Nasi Pecel - Rp.10000")
    
    nomor = int(input("Masukan Pilihan 1/2/3/4/5 : "))
    porsi = int(input("Berapa Porsi : "))

    if nomor == 1:
        totalmakanan = porsi * 20000
        print(porsi,' Nasi Ayam Goreng = Rp.' ,totalmakanan)
        makan=("Nasi Ayam Goreng")
    elif nomor == 2:
        totalmakanan = porsi * 13000
        print(porsi,' Nasi Goreng = Rp.' ,totalmakanan)
        makan=("Nasi Goreng")
    elif nomor == 3:
        totalmakanan = porsi * 15000
        print(porsi,' Bakso = Rp.' ,totalmakanan)
        makan=("Bakso")
    elif nomor == 4:
        totalmakanan = porsi * 10000
        print(porsi,' Mie Ayam = Rp.' ,totalmakanan)
        makan=("Mie Ayam")
    elif nomor == 5:
        totalmakanan = porsi * 10000
        print(porsi,' Nasi Pecel = Rp.' ,totalmakanan)
        makan=("Nasi Pecel")
    else:
        print("Pilihan tidak ada di daftar menu\nSilahkan pilih kembali !")
        makanan()
                															
def minuman():
    global totalminuman
    global gelas
    global minum
    print("\n===============MENU MINUMAN===============\n")
    print("1. Air Mineral - Rp.3000")
    print("2. Es Jeruk - Rp.7000")
    print("3. Es Teh Manis - Rp.5000")
    print("4. Es Campur - Rp.10000")
    print("5. Es Teh Lemon - Rp.6000")
    
    nomor = int(input("Masukan Pilihan 1/2/3/4/5 : "))
    gelas = int(input("Berapa Gelas : "))

    if nomor == 1:
        totalminuman = gelas * 3000
        print=(gelas,' Air Mineral = Rp.' ,totalminuman)
        Minum=("Air Mineral")
    elif nomor == 2:
        totalminuman = gelas * 7000
        print=(gelas,' Es Jeruk = Rp.' ,totalminuman)
        Minum=("Es jeruk")
    elif nomor == 3:
        totalminuman = gelas * 5000
        print=(gelas,' Es Teh Manis = Rp.' ,totalminuman)
        minum=("Es Teh Manis")
    elif nomor == 4:
        totalminuman = gelas * 10000
        print(gelas,' Es Campur = Rp.' ,totalminuman)
        minum=("Es Campur")
    elif nomor == 5:
        totalminuman = gelas * 6000
        print(gelas,' Es Teh Lemon = Rp.' ,totalminuman)
        minum=("Es Teh Lemon")
    else:
        print("Pilihan tidak ada di daftar menu\nSilahkan pilih kembali !")
        minuman()  
             
makanan()
minuman()
total_semua = totalmakanan + totalminuman

print("\nTotal yang harus di bayar : ",total_semua)
uang = int(input("Uang Tunai Pembeli : Rp."))
kembalian = int(uang - total_semua)
print("kembalian :", kembalian)

print("\n===============S T R U K P E M B E L I A N===============")
print("Nama\t\t:",Pembeli)
print("Beli\t\t:",porsi,makan,"(Rp.",totalmakanan,")")
print("Beli\t\t:",gelas,minum,"(Rp.",totalminuman,")")
print("Tagihan\t\t:",total_semua)
print("Dibayar\t\t:",uang)
print("Kembalian\t:",kembalian) 

print("===============")
print("===============")










        









