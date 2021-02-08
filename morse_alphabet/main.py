# from json import dumps
#
#
# class A:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def __str__(self):
#         return dumps(self.__dict__)
#
#
# print(A("abc", "def"))


def srednia(elements=()):
    wynik = 0
    for element in elements:
        wynik += element
    return wynik / len(elements)


print(srednia((1, 2, 3, 4, 5, 6, 7)))
