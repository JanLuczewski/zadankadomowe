# Wydrukuje menu z następującymi opcjami: “Oblicz średnią arytmetyczną“, “Podnieś do potęgi” oraz “Porównaj liczby”
# Użytkownik może wybrać dowolną opcję, a te powinny:
# Oblicz średnią arytmetyczną: przyjmij dwie liczby od użytkownika, następnie oblicz ich średnią arytmetyczną oraz wydrukuj ją na ekranie
# Podnieś do potęgi: przyjmij dwie liczby od użytkownika, podnieś pierwszą podaną liczbę do potęgi podanej jako druga liczba (przykładowo, jeśli podałem liczby 2 oraz 3, to wynik powinien wynosić 8. Przydatnym operatorem arytmetycznym będzie tu **)
# Porównaj liczby: przyjmij dwie liczby od użytkownika, a następnie wydrukuj na ekranie tę, która jest większa
# Po zakończeniu którejkolwiek operacji, program powinien zacząć egzekucję od początku ( przydatna będzie tutaj pętla while )
def menu():
    print("1.Oblicz średnią arytmetyczną")
    print("2.Podnieś do potęgi")
    print("3.Porównaj liczby")

    dec = int(input("Wybierz opcję "))
    liczba1 = int(input("podaj liczbe 1 :..."))
    liczba2 = int(input("podaj liczbe 2 :..."))


    if dec == 1:
        print("średnia")
        wynik = (liczba1 + liczba2)/2
        print(wynik)
    if dec == 2:
        print("potęga")
        wynik = (liczba1 ** liczba2)
        print(wynik)
    if dec == 3:
        print("porównanie")
        if liczba1 == liczba2:
            print("są równe")
        if liczba1 > liczba2:
            print("liczba 1 jest większa")
        if liczba1 < liczba2:
            print("liczba1 jest mniejsza")


while True :
    menu()

