morse_alphabet = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "Ą": ".-.-",
    "Ć": "-.-..",
    "Ę": "..-..",
    "Ł": ".-..-",
    "Ń": "--.--",
    "Ó": "---.",
    "Ś": "...-...",
    "Ż": "--..-.",
    "Ź": "--..-",
    " ": ""
}

inverted_morse_alphabet = {value: key for key, value in morse_alphabet.items()}


class Morse:
    @staticmethod
    def encode(text: str):
        result = ""

        for char in text:
            try:
                result += morse_alphabet[char.upper()] + " "
            except KeyError:
                pass

        return result[:-1]

    @staticmethod
    def decode(morse_text: str):
        result = ""

        for word in morse_text.split("  "):
            for letter in word.split(" "):
                try:
                    result += inverted_morse_alphabet[letter]
                except KeyError:
                    pass
            result += " "

        return result[:-1]
