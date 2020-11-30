# Importujesz bibliotekę re. Służy ona do operowania na wyrażeniach regularnych. Jeżeli chcesz wiedzieć więcej wpisz w google: Regular Expressions
import re

# Importujesz bibliotekę requests. Odpowiada ona za wykonywanie żądań do serwera. Za pomocą tej biblioteki możesz np. Pobrać kod strony internetowe.
import requests

# Importujesz bibliotekę htmldom. Służy ona do operowania na kodzie html. Buduje ona drzewo DOM po którym sie poruszasz.
from htmldom import htmldom

# Definiujesz metodę która ma za zadanie wykonanie na argumencie "string" wyrażenia regularnego które pozostawia w nim tylko same liczby. Resztę usuwa i zwraca zmienioną wersję.
def format_to_only_numbers(string):
    return re.sub('[^0-9]', '', string)


# Zmienna w której przekazujesz adres url strony na której będziesz pracował
site_url = "https://pogoda.interia.pl/prognoza-szczegolowa-szczecin,cId,34668"

# Wykonujesz żądanie GET które powinno Ci zwrócić kod strony z linku wyżej.
response = requests.get(site_url)

# Deklarujesz zmienną do której przypisujesz utworzone za pomocą htmldom drzewo dom, z kodu który pobrałeś wyżej
dom = htmldom.HtmlDom().createDom(response.text)

# Zaczynając od elementu który posiada klasę o nazwie ".feelTemperature", przechodzisz do elementu dziecka(czyli takiego elementu który zawiera się w tym pierwszym) i wyciągasz jego wartość tekstową
temperature = dom.find(".feelTemperature").children(".weather-currently-details-value").text()

# Zaczynając od elementu który posiada klasę o nazwie ".pressure", przechodzisz do elementu dziecka(czyli takiego elementu który zawiera się w tym pierwszym) i wyciągasz jego wartość tekstową
pressure = dom.find(".pressure").children(".weather-currently-details-value").text()

# Zaczynając od elementu który posiada klasę o nazwie ".wind", przechodzisz do elementu dziecka(czyli takiego elementu który zawiera się w tym pierwszym) i wyciągasz jego wartość tekstową
wind = dom.find(".wind").children(".weather-currently-details-value").text()

# Wypisujesz temperature, cisnienie i wiatr
print("Temperatura: " + format_to_only_numbers(temperature) + " Cisnienie: " + format_to_only_numbers(
    pressure) + " Wiatr: " + format_to_only_numbers(wind))
