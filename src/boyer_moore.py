def zapamietaj_ostatnie_pozycje(wzorzec):
    ostatnia_pozycja = {}

    for indeks in range(len(wzorzec)):
        ostatnia_pozycja[wzorzec[indeks]] = indeks

    return ostatnia_pozycja


def znajdz_wzorzec(tekst, wzorzec):
    dlugosc_tekstu = len(tekst)
    dlugosc_wzorca = len(wzorzec)

    ostatnia_pozycja = zapamietaj_ostatnie_pozycje(wzorzec)

    przesuniecie = 0

    while przesuniecie <= dlugosc_tekstu - dlugosc_wzorca:
        indeks = dlugosc_wzorca - 1

        # porównujemy znaki od końca wzorca
        while indeks >= 0 and wzorzec[indeks] == tekst[przesuniecie + indeks]:
            indeks -= 1

        if indeks < 0:
            print(f"Wzorzec znaleziony na pozycji {przesuniecie}")

            if przesuniecie + dlugosc_wzorca < dlugosc_tekstu:
                nastepny_znak = tekst[przesuniecie + dlugosc_wzorca]
                przesuniecie += dlugosc_wzorca - ostatnia_pozycja.get(nastepny_znak, -1)
            else:
                przesuniecie += 1
        else:
            zly_znak = tekst[przesuniecie + indeks]
            ostatnie_wystapienie = ostatnia_pozycja.get(zly_znak, -1)

            przesuniecie += max(1, indeks - ostatnie_wystapienie)


def main():
    tekst = "ABAAABCD"
    wzorzec = "ABC"
    znajdz_wzorzec(tekst, wzorzec)


if __name__ == "__main__":
    main()