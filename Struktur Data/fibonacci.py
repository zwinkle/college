def fibonacci_search(arr, x):
    fib2 = 0  # Fibonacci awal (F(n-2))
    fib1 = 1  # Fibonacci kedua (F(n-1))
    fib = fib2 + fib1  # Fibonacci saat ini (F(n))

    # Mencari bilangan Fibonacci saat ini (F(n)) yang paling besar. Kemudian yang lebih kecil atau sama dengan panjang array
    while fib < len(arr):
        fib2 = fib1
        fib1 = fib
        fib = fib2 + fib1
        print('')
        print(f'Fib2 : {fib2}\nFib1 : {fib1}\nFib : {fib}\nPanjang array : {len(arr)}, index sampai {len(arr)-1}')

        if fib >= len(arr):
            print('')
            print('='*15, 'DIKETAHUI','='*16)
            print(f'Fib2 : {fib2}\nFib1 : {fib1}\nFib : {fib}\nPanjang array : {len(arr)}, index sampai {len(arr)-1}\n')

    offset = -1  # Indeks offset dari awal array

    # Melakukan pencarian dengan membandingkan elemen di posisi fibonacci yang dikurangi dengan offset dengan elemen yang dicari
    print('='*15, 'DIKETAHUI','='*16)
    while fib > 1:
        # Mendapatkan indeks yang valid
        i = min(offset + fib2, len(arr) - 1)
        print(f'Offset : {offset}')
        print(f'Fib2 : {fib2}')
        print(f'Fib1 : {fib1}')
        print(f'Fib : {fib}')
        print(f'Rumus : (Offset + Fib2, Panjang array - 1)')
        print(f'Hasil : {offset + fib2, len(arr) - 1}')
        print(f'Index : {i}\n')

        # Jika elemen yang dicari lebih besar, maka fib menjadi fib2 dan fib2 menjadi fib1 untuk mencari di sebelah kanan
        if arr[i] < x:
            fib = fib1
            fib1 = fib2
            fib2 = fib - fib1
            offset = i

        # Jika elemen yang dicari lebih kecil, maka fib menjadi fib1 dan fib2 menjadi fib2 - fib1 untuk mencari di sebelah kiri
        elif arr[i] > x:
            print(f'{fib2}')
            fib = fib2
            print(f'{fib1} - {fib2}')
            fib1 = fib1 - fib2
            print(f'{fib} - {fib1}')
            fib2 = fib - fib1

        # Jika elemen yang dicari ditemukan
        else:
            return i

    # Memeriksa elemen terakhir dengan x
    if fib1 and arr[offset + 1] == x:
        return offset + 1

    # Jika elemen tidak ditemukan
    return -1

# Contoh
arr = [2, 4, 7, 10, 13, 17, 21, 25]
x = 10
result = fibonacci_search(arr, x)
if result != -1:
    print('='*16, 'HASILNYA','='*16)
    print(f"{x} ditemukan pada indeks", result, '\n')
else:
    print('='*16, 'HASILNYA','='*16)
    print(f"{x} tidak ditemukan\n")