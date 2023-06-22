#zadanie 1.1
hello = "Hello"
student = "Karolina"

komunikat = "{} {}".format(hello, student)
print(komunikat)

#zadanie 1.2
student = input("Podaj imię: ")
przywitanie = "Hello " + student
print(przywitanie)

#zadanie 1.3
studenci = ["Ania", "Kuba", "Piotr", "Jan"]

liczba_studentow = len(studenci)

print("Liczba studentów wynosi: {}".format(liczba_studentow))

#zadanie 1.4

studenci = ["Ania", "Kasia", "Piotr", "Tomek"]

for student in studenci:
    print("Cześć", student)

#zadanie 1.5

liczba = 3
potega = 4

wynik = liczba ** potega

print(wynik)
