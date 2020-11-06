"""
1. Generowanie "n" elementów ciągu fibbonacciego https://pl.wikipedia.org/wiki/Ci%C4%85g_Fibonacciego
- Należy pobrać od użytkownika liczbę n
- Należy wygenerować "n" elementów ciągu fibbonacciego
- Należy zaprezentować wygenerowane elementy użytkownikowi
"""

n = int(input("Podaj wartosc n: "))
x, y = 0, 1
for i in range(1, n):
    x, y = y, x + y
    print(x)
