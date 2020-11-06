"""
3. Znalezienie najmniejszego i najwiekszego z podanych elementów
- Od użytkownika należy pobierać liczby do momentu aż nie wpisze znaku "-" i dodawać je do listy.
- W liście należy znaleźć największą oraz najmniejsza liczbę.
- Wyniki należy zaprezentować użytkownikowi
"""


def is_real_decimal(n):
    try:
        int(n)
    except ValueError:
        return False
    return True


result_list = []

while True:
    number = input("Podaj liczbę: ")

    if not is_real_decimal(number):
        break

    result_list.append(number)

print("Najmniejsza wartość: %s".format(min(result_list)))

print("Najmniejsza wartość: ", min(result_list))
print("Największa wartość: ", max(result_list))
