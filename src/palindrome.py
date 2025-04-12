def is_palindrome(word: str) -> bool:
    if word[0::] == word[::-1]:
        return True 
    else:
        return False

palabra = input("ingrese una palabra palindroma")
palin = is_palindrome(palabra)
print(palin)