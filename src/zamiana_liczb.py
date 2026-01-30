
liczba = int(input("Podaj liczbę dziesiętną: "))

system_docelowy = int(input("Podaj podstawę systemu (2-36): "))

znaki = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

if liczba == 0:
    print("Wynik:", 0)
else:
    wynik = ""

    while liczba > 0:
        reszta = liczba % system_docelowy
        znak = znaki[reszta]
        wynik = znak + wynik
        liczba = liczba // system_docelowy

    print("Wynik:", wynik)

#Po przeczytaniu pięknego pliku Ściąga python:

liczba_v2 = int(input("Podaj liczbę dziesiętną: "))
system_docelowy_v2 = int(input("Podaj podstawę systemu (2-36): "))

if liczba_v2 == 0:
    print("Wynik: 0")
else:
    wynik_v2 = ""

    while liczba_v2 > 0:
        reszta_v2 = liczba_v2 % system_docelowy_v2

        if reszta < 10:
            znak_v2 = chr(ord('0') + reszta_v2)
        else:
            znak_v2 = chr(ord('A') + reszta_v2 - 10)

        wynik_v2 = znak_v2 + wynik_v2
        liczba_v2 = liczba_v2 // system_docelowy_v2

    print("Wynik:", wynik_v2)