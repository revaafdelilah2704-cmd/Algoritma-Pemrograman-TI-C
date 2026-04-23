 # === BAGIAN A ===.
DAFTAR_PILIHAN = ["gunting", "batu", "kertas", "batu", "gunting", "kertas", "gunting", "batu"]
riwayat ={}

def tentukan_pemendang(pilihan_pemain, pilihan_komputer)
     menang_lawan{"gunting" :"kertas", "batu" : "gunting", "kertas" : "batu"}

if pilihan_pemain == pilihan_komputer:
return"seri"

elif (pilihan_pemain == "gunting" and pilihan_komputer == "kertas")
    return "pemain"
elif (pilihan_pemain == "batu" and pilihan_komputer == "gunting")
     return "pemain"
elif(pilihan_pemain == "kertas" and pilihan_komputer == "batu")
    return "pemain"
else:
    return "komputer"

def main_satu_giliran(nomor_giliran):
    pilihan_komputer = DAFTAR_PILIHAN{nomor_giliran % len(DAFTAR_pikihan)}
    while True:
    tebakan = input in DAFTAR_PILIHAN:
    if hasil == "gunting" or pilihan_pemain == "batu" or pilihan_pemain == "kertas":
        break
        print("hasil:",hasil)

      print("komputer:", pilihan_komputer)
      
      hasil = tentukan_pemenang(pilihan_pemain, pilihan_komputer)
      print("hasil:", hasil)

      return hasil


def main_satu_ronde(nama, nomor_ronde):
nomor_giliran = 0
menang_pilihan = 0
menang_komputer = 0
while menang_pemain < 3 and menang_komputer < 3:
    hasil = main_satu_giliran(nomor_giliran)
    nomor_giliran += 1
    if hasil == pemain:
        menang_pemain += 1
    elif hasil == "komputer":
        menang_komputer += 1



 # === BAGIAN B ===
def tampilkan_riwayat(riwayat):
    n = len(salinan)
        print("Belum ada riwayat")
        return
    
    print("No\tNama\tSkor")
    for i, data in enumerate(riwayat, 1):
    


# === BAGIAN C ===
def selection_sort_riwayat(riwayat):
    n = len(data)
    
    for i in range(n):
        max_idx = i
        for j in range(i+1, n):
            if data[j][1] > data[max_idx][1]:
                max_idx = j
        
        data[i], data[max_idx] = data[max_idx], data[i]

    return data



        






    

