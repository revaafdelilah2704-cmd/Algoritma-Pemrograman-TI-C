try:
    p = 3 / 0  
    print(p)
except:
    print("Blok 'try' mengalami error")    
try:
    print(x)    # code cause an error
except:
    print("Variabel tidak ditemukan")
else:
    print("Semua berjalan lancar")  
    print("Program berjalan")  
def floor_div(a, b):
    try:
        hasil = a // b
        print("Berhasil dieksekusi, hasil nya adalah: ", hasil)
    except:
        print("Terjadi kendala. Coba kembali")
floor_div(6, 3)     
try:
    umur = -1
    if umur < 0:
        raise Exception("Nggak ada umur di bawah 0")
except Exception as e:
    print("Error diketahui: ", e)
else:
    print("Program berjalan")