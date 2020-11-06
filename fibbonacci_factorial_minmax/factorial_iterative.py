"""
2. Obliczanie silni z "n" https://pl.wikipedia.org/wiki/Silnia
- Należy pobrać od użytkownika liczbę "n"
- Z pobranej liczby "n" należy wyliczyć silnię
- Wynik należy zaprezentować użytkownikowi
UWAGA! Należy zwrócić i odwzorować wszystkie założenia silni
"""

n = int(input("Podaj wartosc n: "))
result = 1

for x in range(1, n + 1):
    result *= x

print(result)
