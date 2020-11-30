import os
from time import sleep

from morse import Morse

"""
Należy napisać program, który będzie pobierał od użytkownika
 jakąkolwiek treść i tłumaczył ją na alfabet morse'a.
 Następnie ma zasymulować przesłanie tego sygnału przez telegraf
 (w odpowiednich interwałach wypisywać słowa "Kropka", "Kreska").
"""

unit = 1 / 3

user_input = input("Wiadomość: ")

encoded = Morse.encode(user_input)

for word in encoded.split("  "):
    for letter in word.split(" "):
        for symbol in letter:
            if symbol == ".":
                print("Kropka")
                sleep(unit)
                print("Koniec kropki")
            elif symbol == "-":
                print("Kreska")
                sleep(unit * 3)
                print("Koniec kreski")
        sleep(unit * 3)
    sleep(unit * 4)
