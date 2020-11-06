"""
2. Obliczanie silni z "n" https://pl.wikipedia.org/wiki/Silnia
- Należy pobrać od użytkownika liczbę "n"
- Z pobranej liczby "n" należy wyliczyć silnię
- Wynik należy zaprezentować użytkownikowi
UWAGA! Należy zwrócić i odwzorować wszystkie założenia silni
"""

def factorial(n): return 1 if n < 1 else n * factorial(n - 1)


n = int(input("Podaj wartosc n: "))
print(factorial(n))
