def input_data():
    while True:
        try:
            n = int(input("Jumlah elemen: "))
            if n <= 0: continue
            break
        except:
            print("Harus angka!")

    data = []
    for i in range(n):
        while True:
            try:
                x = int(input(f"elemen ke-{i+1}: "))
                if x < 0: continue
                data.append(x)
                break
            except:
                print("Invalid!")
    return data

data = input_data()

print("\nelemen awal:", data)

def insertion_sort(a):
    a = a.copy()
    for i in range(1, len(a)):
        key = a[i]; j = i-1
        while j >= 0 and a[j] > key:
            a[j+1] = a[j]; j -= 1
        a[j+1] = key
    return a

print("\nInsertion Sort")
print("Sebelum:", data)
print("Sesudah:", insertion_sort(data))


def quick_sort(a):
    if len(a) <= 1: return a
    pivot = a[0]
    kiri = [x for x in a[1:] if x <= pivot]
    kanan = [x for x in a[1:] if x > pivot]
    return quick_sort(kiri) + [pivot] + quick_sort(kanan)

print("\nQuick Sort")
print("Sebelum:", data)
print("Sesudah:", quick_sort(data))

def counting_sort(a):
    if not a: return []
    count = [0]*(max(a)+1)
    for x in a: count[x] += 1
    hasil = []
    for i in range(len(count)):
        hasil += [i]*count[i]
    return hasil

print("\nCounting Sort")
print("Sebelum:", data)
print("Sesudah:", counting_sort(data))