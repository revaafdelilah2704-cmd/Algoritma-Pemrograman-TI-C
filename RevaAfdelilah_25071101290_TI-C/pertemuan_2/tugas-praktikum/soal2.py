def bilangan_prima(n):
    prima_list = []

    for angka in range(2, n + 1):
        is_prima = True

        for i in range(2, angka):
            if angka % i == 0:
                is_prima = False
                break

        if is_prima:
            prima_list.append(angka)

    return prima_list

# Memanggil fungsi
hasil_prima = bilangan_prima(50)

# Menampilkan hasil
print("Bilangan prima 1 sampai 50:", hasil_prima)