def fibonacci_search(arr, x):
    fib2 = 0  # First Fibonacci (F(n-2))
    fib1 = 1  # Second Fibonacci (F(n-1))
    fib = fib2 + fib1  # Third Fibonacci (F(n))

    # Find The biggest value from Third Fibonacci (F(n)). Then lower or same value
    while fib < len(arr):
        fib2 = fib1
        fib1 = fib
        fib = fib2 + fib1
        print('')
        print(f'Fib2 : {fib2}\nFib1 : {fib1}\nFib : {fib}\nArray length : {len(arr)}, Index till {len(arr)-1}')

        if fib >= len(arr):
            print('')
            print('='*15, 'INFO','='*16)
            print(f'Fib2 : {fib2}\nFib1 : {fib1}\nFib : {fib}\nArray length : {len(arr)}, Index till {len(arr)-1}\n')

    offset = -1  # Index offset

    # Searching by compare with offsett
    print('='*15, 'INFO','='*16)
    while fib > 1:
        # Get index
        i = min(offset + fib2, len(arr) - 1)
        print(f'Offset : {offset}')
        print(f'Fib2 : {fib2}')
        print(f'Fib1 : {fib1}')
        print(f'Fib : {fib}')
        print(f'Formula : (Offset + Fib2, Array length - 1)')
        print(f'Result : {offset + fib2, len(arr) - 1}')
        print(f'Index : {i}\n')

        # If we got bigger element
        if arr[i] < x:
            fib = fib1
            fib1 = fib2
            fib2 = fib - fib1
            offset = i

        # If we got smaller element
        elif arr[i] > x:
            print(f'{fib2}')
            fib = fib2
            print(f'{fib1} - {fib2}')
            fib1 = fib1 - fib2
            print(f'{fib} - {fib1}')
            fib2 = fib - fib1

        # If we find the element
        else:
            return i

    # Checking last element with x
    if fib1 and arr[offset + 1] == x:
        return offset + 1

    # If we cannot find the element
    return -1

# Example, you can change the value in the list <variable arr>
arr = [2, 4, 7, 10, 13, 17, 21, 25]
x = 10
result = fibonacci_search(arr, x)
if result != -1:
    print('='*16, 'RESULT','='*16)
    print(f"{x} Find in index", result, '\n')
else:
    print('='*16, 'RESULTR','='*16)
    print(f"{x} Cannot find\n")