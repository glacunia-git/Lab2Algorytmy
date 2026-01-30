def czy_palindrom(slowo):
    lewy = 0
    prawy = len(slowo) - 1

    while lewy < prawy:
        if slowo[lewy] != slowo[prawy]:
            return False
        lewy += 1
        prawy -= 1

    return True

with open("../data/palindromy.txt", "r") as plik:
    for wiersz in plik:
        tekst = wiersz.strip()

        if tekst == "":
            continue

        if czy_palindrom(tekst):
            print(f"{tekst} -> PALINDROM")
        else:
            print(f"{tekst} -> NIE palindrom")