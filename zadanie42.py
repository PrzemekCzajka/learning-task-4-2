#Zadanie: Palindromy


def palin(word):
    if word == word[::-1]:
        print(f"Wyraz {word} jest palindromem")
        return(True)
    else:
        print(f"Wyraz {word} nie jest palindromem")
        return(False)

palin("Kajak")
palin("rura")