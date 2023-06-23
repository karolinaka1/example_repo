class Mieszkanie:
    def __init__(self, nr_mieszkania, adres, miasto, powierzchnia, pietro, liczba_pokoi, cena, mieszkancy):
        self.nr_mieszkania = nr_mieszkania
        self.adres = adres
        self.miasto = miasto
        self.powierzchnia = powierzchnia
        self.pietro = pietro
        self.liczba_pokoi = liczba_pokoi
        self.cena = cena
        self.mieszkancy = mieszkancy

    def __str__(self):
        return 'Mieszkanie nr ' + str(self.nr_mieszkania) + ', ' + self.adres + ', ' + self.miasto + ', powierzchnia (m^2): ' + str(self.powierzchnia) + ', piętro: ' + str(self.pietro) + ', liczba pokoi: ' + str(self.liczba_pokoi) + ', cena: ' + str(self.cena) + ', mieszkańcy: ' + ', '.join(self.mieszkancy)

    def dodaj_mieszkanca(self, mieszkaniec):
       self.mieszkancy.append(mieszkaniec)

    def zmien_cene(self, nowa_cena):
        self.cena = nowa_cena

mieszkanie_1 = Mieszkanie(1, "ul.Kwiatowa 4/1", "Poznań", 50, 1, 3, 2000, ["Anna Kowalska"])
print(mieszkanie_1)

mieszkanie_1.zmien_cene(2700)
print(mieszkanie_1)

mieszkanie_1.dodaj_mieszkanca("Jan Kowalski")
print(mieszkanie_1.mieszkancy)
