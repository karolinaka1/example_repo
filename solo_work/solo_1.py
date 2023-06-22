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

#zadanie 1.6

ciag_znakow = "edbw(hdakqas(skqskahb))adwndwb(wgwidn()dsqwhjdw)"
liczba_nawiasow = ciag_znakow.count("(")
print("Liczba nawiasów otwierających:", liczba_nawiasow)

#zadanie 1.7

studenci = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]

studenci.sort(key=lambda x: x[0])
print("Alfabetyczna lista studentow wynosi: ")
for student in studenci:
    print(student)

#zadanie 1.8

studenci = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]

studenci.sort(key=lambda x: x.split()[1])
print("Alfabetyczna lista studentow wynosi: ")
for student in studenci:
    print(student)

#zadanie 1.9

studenci = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]
liczba_n = 0
for student in studenci:
    if student.split()[1].startswith("N"):
        liczba_n += 1
print("Liczba studentow na N wynosi:", liczba_n)
