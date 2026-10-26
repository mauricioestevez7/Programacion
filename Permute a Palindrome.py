def permute_a_palindrome(entrada): 
    impares = 0
    
    for char in set(entrada):
        contador = entrada.count(char)        
        
        if contador % 2 != 0:
            impares += 1
    if impares <= 1:        
        return True
    else:
        return False