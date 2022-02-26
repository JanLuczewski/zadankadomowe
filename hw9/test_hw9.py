# HW9:
# Stwórz funkcję:
# przyjmującą na wejściu długości boków trójkąta prostokątnego
# sprawdzającą czy dane są typu int - w przeciwnym wypadku niech rzuci błędem
# oblicza długość trzeciego, najdłuższego boku
# Dopisać testy w PyTest:
# sprawdzający czy jeśli podam na wejściu stringa to zostanie wyrzucony błąd
# czy jeśli podam prawidłowe wartości to dostanie poprawną długość trzeciego boku - dwa testy dla różnych wartości
import pytest
import math
from triangle import oblicz_bok

def test_oblicz_bok():
    result = oblicz_bok(2,2)
    assert result == 5
def test_czy_int():
    with pytest.raises(TypeError) as excinfo:
        oblicz_bok("6",2)
