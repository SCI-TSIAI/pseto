# Linia poniżej jest deklaracją klasy "PeselValidator".
class PeselValidator:
    # Linia poniżej definiuje stałą z wagami. Mnożenie przez 3 powiela listę 3-krotnie.
    weight = [9, 7, 3, 1] * 3

    # Linia poniżej definiuje metodę o nazwie "validate_pesel" która przyjmuje parametr typu string o nazwie "pesel".
    def validate_pesel(self, pesel: str):
        # Linia poniżej definiuje zmienną, która przechowywać będzie rezultat wykonania algorytmu
        result = 0

        # Linia poniżej sprawdza czy długość peselu jest równa 11 i czy zawiera on same cyfry.
        if len(pesel) != 11 or not pesel.isnumeric():
            # Jeżeli poniższy warunek nie jest spełniony, zwróc fałsz.
            return False

        """
         Poniższa linia mówi że, dla przedziału od 0-9(czyli nasz range(10)) wykonaj tyle iteracji ile jest elementów
         w danym range. W każdej iteracji przypisz aktualną wartość do zmiennej i.
        """
        for i in range(10):
            """
             Poniższa linia wykonuje mnożenie na i-tym elemencie peselu oraz wagi. 
             Następnie dodaje wynik mnożenia do zmiennej result.
            """
            result += int(pesel[i]) * self.weight[i]

        # Poniższa linia wykonuje dzielenie modulo przez dziesieć na zmiennej result a następnie przypisuje wynik do niej.
        result = result % 10

        # Poniższa linia porównuje ostatni znak numer pesel, z wynikiem działania algorytmu i zwraca wynik z metody.
        return pesel[-1] == str(result)
