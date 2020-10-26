# Linia poniżej służy do importowania klasy PeselValidator z modułu pesel_validator
from pesel_validator import PeselValidator

"""
Linia poniżej wyświetla użytkownikowi wiadomość o treści "Podaj pesel: ", pobiera od niego wartość po wciśnięciu
klawisza enter, a następnie przypisuje tą wartość do zmiennej o nazwie "global_pesel"
"""
global_pesel = input("Podaj pesel: ")

# Linia poniżej tworzy instancję klasy "PeselValidator" a następnie przypisuje ją do zmiennej o nazwie "validator"
validator = PeselValidator()

"""
Linia poniżej wypisuje wynik wywołania metody "validate_pesel", z instancji klasy "PeselValidator".
Do metody przekazywana jest wartość ze zmiennej "global_pesel"
"""
print(validator.validate_pesel(global_pesel))
