def anagrams(word, words):
    resultado = []

    for palabra in words:
        if sorted(word) == sorted(palabra):
            resultado.append(palabra)

    return resultado