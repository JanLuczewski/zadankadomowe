# 1). Stwórz funkcję nazwaną dodajListy() która zwróci nową listę sumując ze sobą elementy na tych samych
# indeksach  . Możesz przypuścić, że jako parametry do funkcji podawane są zawsze listy zawierające tylko liczby.
#     Jeżeli listy są różnej długości, funkcja powinna wyświetlić napis ‘Podane listy muszą być tej samej długości’
#

def zbadaj_trojkat(lista1,lista2):
    if len(lista1) != len(lista2):
        print("listy muszą być równe")
    else :
        print("listy są równe")
        wynik = []
        for a,b in zip(lista1,lista2):
            wynik.append(a+b)
        print(wynik)

zbadaj_trojkat([1,2],[3,4])

# 2). Stwórz funkcję nazwaną zbadajTrojkat() która przyjmie jako argumenty długości boków trójkąta.
#     Funkcja powinna zwrócić, czy trójkąt jest prostokątny, równoramienny, równoboczny, różnoboczny
# lub nieprawidłowy

def zbadajTrojkat(bokA,bokB,bokC):
    if bokA ** 2 + bokB ** 2 == bokC ** 2:
        print("trójkąt jest prostokątny")
    if (bokA == bokB) and (bokC == (bokA)/(2 ** 0.5)):
        print("trójkąt jest równoramienny")
    if bokA == bokB == bokC:
        print("trójkąt jest równoboczny")
    if bokA != bokB != bokC:
        print("trójkąt jest różnoboczny")

zbadajTrojkat(3,4,5)
