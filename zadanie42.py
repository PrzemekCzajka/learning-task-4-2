#Zadanie: Palindromy


def palin(word):
    if word == word[::-1]:
        return True
    else:
        return False

palin("kajak")
palin("ziemia")