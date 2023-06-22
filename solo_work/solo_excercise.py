class student:
    def __init__(self, imie, nazwisko,numer_indeksu):
        self.imie_studenta = imie
        self.nazwisko = nazwisko
        self.numer_indeksu = numer_indeksu
        self.indeks = []
    def __str__(self):
        return self.imie_studenta + ' ' +self.nazwisko + ' ' + str(self.numer_indeksu)

    def dodaj_ocene(self,ocena):
        self.indeks.append(ocena)

    def oblicz_srednia(self):
        if len(self.indeks) ==0:
            return 0
        else:
            return sum(self.indeks)/len(self.indeks)



student_karolina=student("Karolina", "Karaśkiewicz", "122001")
student_karolina.dodaj_ocene(5.0)
student_karolina.dodaj_ocene(4.0)
student_karolina.dodaj_ocene(3.0)
student_karolina.dodaj_ocene(2.0)
print(student_karolina.indeks)
print(student_karolina.oblicz_srednia())






