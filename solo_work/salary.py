class Pracownik:
    def __init__(self, imie, nazwisko, pensja_brutto):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pensja_brutto = pensja_brutto

    def __str__(self):
        return f"Pracownik: {self.imie} {self.nazwisko}"

    def oblicz_netto(self):
        skladka_emerytalna = 0.0976 * self.pensja_brutto
        skladka_rentowa = 0.015 * self.pensja_brutto
        skladka_chorobowa = 0.0245 * self.pensja_brutto
        skladka_zdrowotna = 0.09 * (self.pensja_brutto - skladka_emerytalna - skladka_rentowa - skladka_chorobowa)
        skladka_zdrowotna = round(skladka_zdrowotna, 2)
        skladki_calosciowe = skladka_emerytalna + skladka_rentowa + skladka_chorobowa + skladka_zdrowotna
        podstawa_opodatkowania = self.pensja_brutto - skladki_calosciowe
        podatek = 0.17 * podstawa_opodatkowania
        kwota_netto = self.pensja_brutto - skladki_calosciowe - podatek
        return round(kwota_netto, 2)

    def oblicz_koszty_pracodawcy(self):
        skladka_emerytalna = 0.0976 * self.pensja_brutto
        skladka_rentowa = 0.065 * self.pensja_brutto
        skladka_wypadkowa = 0.0167 * self.pensja_brutto
        skladka_fgsp = 0.0245 * self.pensja_brutto
        skladka_zdrowotna = 0.09 * self.pensja_brutto
        koszty_pracodawcy = self.pensja_brutto + skladka_emerytalna + skladka_rentowa + skladka_wypadkowa + skladka_fgsp + skladka_zdrowotna
        return koszty_pracodawcy

    def wygeneruj_raport(self):
        skladka_emerytalna = 0.0976 * self.pensja_brutto
        skladka_rentowa = 0.065 * self.pensja_brutto
        skladka_wypadkowa = 0.0167 * self.pensja_brutto
        skladka_fgsp = 0.0245 * self.pensja_brutto
        skladka_zdrowotna = 0.09 * self.pensja_brutto
        print(f"Koszty pracodawcy za pracownika {self.imie} {self.nazwisko}:")
        print(f"Skladka emerytalna: {skladka_emerytalna:.2f} zł")
        print(f"Skladka rentowa: {skladka_rentowa:.2f} zł")
        print(f"Skladka wypadkowa: {skladka_wypadkowa:.2f} zł")
        print(f"Skladka FGŚP: {skladka_fgsp:.2f} zł")
        print(f"Skladka zdrowotna: {skladka_zdrowotna:.2f} zł")
        print("--------------")
        print(f"Suma kosztów pracodawcy: {self.oblicz_koszty_pracodawcy():.2f} zł")


# Przykład użycia klasy Pracownik
pracownik1 = Pracownik("Jan", "Kowalski", 5000)
print(pracownik1)
pracownik1.wygeneruj_raport()

pracownik2 = Pracownik("Anna","Nowacka",3000)
print(pracownik2)
pracownik2.wygeneruj_raport()

pracownik3 = Pracownik("Barbara","Wrona",8000)
print(pracownik3)
pracownik3.wygeneruj_raport()
