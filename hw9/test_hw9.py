# HW9:
# Stwórz funkcję:
# przyjmującą na wejściu długości boków trójkąta prostokątnego
# sprawdzającą czy dane są typu int - w przeciwnym wypadku niech rzuci błędem
# oblicza długość trzeciego, najdłuższego boku
# Dopisać testy w PyTest:
# sprawdzający czy jeśli podam na wejściu stringa to zostanie wyrzucony błąd
# czy jeśli podam prawidłowe wartości to dostanie poprawną długość trzeciego boku - dwa testy dla różnych wartości
import pytest

def oblicz_bok(a,b):
    pass

def test_oblicz_bok():
    result = oblicz_bok(3,4)
    assert result == 5
