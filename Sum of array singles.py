def repeats(arr):
    suma = 0

    for numero in arr:
        if arr.count(numero) == 1:
            suma += numero

    return suma