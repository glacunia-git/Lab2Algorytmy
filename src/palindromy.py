def czy_palindrom(slowo):
    lewy = 0
    prawy = len(slowo) - 1

    while lewy < prawy:
        if slowo[lewy] != slowo[prawy]:
            return False
        lewy += 1
        prawy -= 1

    return True

tekst = input("Podaj słowo: ")

if czy_palindrom(tekst):
    print("To jest palindrom")
else:
    print("To nie jest palindrom")