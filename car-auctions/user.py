import itertools


class User:
    id_counter = itertools.count()

    def __init__(self, e_mail, password, first_name, surname, address, phone):
        self.id = next(self.id_counter)
        self.e_mail = e_mail
        #todo
        self.password = password
        self.first_name = first_name
        self.surname = surname
        self.address = address
        self.phone = phone
        self.auctions = []
        self.bids = []

    def print_user(self):
        print(
            f"dane uzytkownika nr {self.id}, e-mail: {self.e_mail}, imie: {self.first_name}, nazwisko: {self.surname}"
            f", adres: {self.address}, telefon: {self.phone}")


