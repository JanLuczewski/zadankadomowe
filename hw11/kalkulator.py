# HW11:
# Napisać kalkulator który dodaje i odejmuje i podpiąć do niego loggera
# W przypadku gdy podamy wartość string wyrzuci błąd i zapisze go do loggera (poziom WARN lub ERROR)
# Jeśli podane dane były poprawne to zapisze dane wejściowe i wynik do loggera (poziom INFO)
import logging

for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)
logging.basicConfig(
    level=logging.INFO,
    filename="example.log")


class Kalkulator():
    @staticmethod
    def dodawanie(a, b):
        if type(a) == int and type(b) == int:
            logging.info("dane poprawne, wynik osiagniety")
            return a + b
        else:
            komunikat = "podane dane są niepoprawne"
            logging.error(komunikat)
            raise TypeError(komunikat)

    @staticmethod
    def odejmowanie(a, b):
        return a - b


if __name__ == "__main__":
    wynik = Kalkulator.dodawanie("5", 4)
    print(wynik)

