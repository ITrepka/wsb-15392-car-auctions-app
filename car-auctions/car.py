from item import Item


class Car(Item):

    def __init__(self, name, description, starting_price, minimal_price, buy_now_price,
                 brand, model, year, body_style, colour, milleage_reading, transmission, fuel, located_in, horse_power):
        super().__init__(name, description, starting_price, minimal_price, buy_now_price)
        self.brand = brand
        self.model = model
        self.year = year
        self.body_style = body_style
        self.colour = colour
        self.milleage_reading = milleage_reading
        self.transmission = transmission
        self.fuel = fuel
        self.located_in = located_in
        self.horse_power = horse_power

    def print_car(self):
        print(
            f"dane samochodu nr {self.id}, nazwa: {self.name}, opis: {self.description}, cena wywoławcza: {self.starting_price}"
            f", cena minimalna: {self.minimal_price}, cena kup teraz: {self.buy_now_price}, marka: {self.brand}"
            f", model: {self.model}, rok produkcji: {self.year}, rodzaj nadwozaia: {self.body_style}, kolor: {self.colour}"
            f", przebieg: {self.milleage_reading}, skrzynia biegów: {self.transmission}, paliwo: {self.fuel}"
            f", lokalizacja: {self.located_in}, ilość koni mechanicznych: {self.horse_power}")
