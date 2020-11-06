"""
3. Znalezienie najmniejszego i najwiekszego z podanych elementów
- Od użytkownika należy pobierać liczby do momentu aż nie wpisze znaku "-".
- Do zmiennych pomocniczych min i max należy przypisywać odpowiednio największą i najmniejszą wartość wprowadzaną.
- Wyniki należy zaprezentować użytkownikowi
"""


def is_real_decimal(n):
    try:
        int(n)
    except ValueError:
        return False
    return True


result_list = []

n = int(input("Podaj liczbę:"))
min = n
max = n

while True:
    n = input("Podaj liczbę:")

    if not is_real_decimal(n):
        break

    if int(n) < min:
        min = int(n)

    if int(n) > max:
        max = int(n)

print("Min: {}, Max: {}".format(min, max))
