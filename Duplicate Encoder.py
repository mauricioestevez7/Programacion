def duplicate_encode(word):
    resultado = ""

    for letra in word.lower():
        if word.lower().count(letra) == 1:
            resultado += "("
        else:
            resultado += ")"

    return resultado