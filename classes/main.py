def generator(start_value=0):
    while start_value < 1_000_000_000_000:
        start_value += 2
        yield start_value


def funkcja(start_value=0):
    lista = []
    while start_value < 1_000_000_000_000:
        start_value += 2
        lista.append(start_value)
    return lista


for x in generator():
    print(f"Uzycie generatora:{x}")

# for x in funkcja():
#     print(f"Uzycie funkcji: {x}")


for x in generator():
    print(f"Uzycie generatora:{x}")

# for x in funkcja():
#     print(f"Uzycie funkcji: {x}")
