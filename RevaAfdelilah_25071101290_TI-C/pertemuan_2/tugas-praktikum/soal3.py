def input_data():
    while True:
        try:
            n = int(input("Masukkan jumlah elemen: "))
            if n <= 0:
                print("Jumlah harus lebih dari 0!")
                continue
            break
        except:
            print("Input harus angka!")

    data = []
    for i in range(n):
        while True:
            try:
                angka = int(input(f"Masukkan elemen ke-{i+1}: "))
                if angka < 0:
                    print("Harus bilangan non-negatif!")
                    continue
                data.append(angka)
                break
            except:
                print("Input tidak valid!")

    return data
