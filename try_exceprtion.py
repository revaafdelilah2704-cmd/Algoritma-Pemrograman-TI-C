try:
    angka1 = int(input("memasukkan angka pertama: "))
    angka2 = int(input("masukan angka kedua: "))
    hasil = angka1 / angka2

except ValueError:
    print("terjadi kesalahan: input harus berupa angka>")

except ZeroDivisionError:
    print("terjadi kesalahan: input boleh membagi dengan nol.")

else: 
    print("hasil pembagian:", hasil)

finally:
    print("prohtam selesai.")
    
    

