from app import App
from auction import Auction
from car import Car
from user import User


def show_auctions():
    app = App()
    print(app.auctions)


def my_auctions():
    pass


def create_auction():
    app = App()
    print("Tworzenie aukcji:\n")
    title = input("Tytuł Aukcji:\n")
    auction_duration = input("Ilość dni, które aukcja ma być aktywna:\n")
    starting_price = input("Cena startowa:\n")
    minimal_price = input("Cena minimalna:\n")
    buy_now_price = input("Cena kup teraz:\n")
    print("Przedmiot aukcji\n")
    brand = input("Marka:\n")
    model = input("Model:\n")
    year = input("Rok produkcji:\n")
    body_style = input("Typ Nadwozia:\n")
    colour = input("Kolor:\n")
    milleage_reading = input("Odczyt z licznika:\n")
    transmission = input("Skrzynia biegów:\n")
    fuel = input("Paliwo:\n")
    located_in = input("Lokalizacja:\n")
    horse_power = input("Ilość koni mechanicznych:\n")
    details = input("Inne szczegóły:\n")
    
    car = Car(details, brand, model, year, body_style, colour, milleage_reading, transmission, fuel, located_in, horse_power)
    auction = Auction(auction_duration, car, starting_price, minimal_price, buy_now_price, title)
    app.auctions.append(auction)
    my_auctions()
    
class Service:
    def create_account(self):
        app = App()
        print("Tworzenie konta:\n")
        e_mail = input("Adres E-mail:\n")
        password = input("Hasło:\n")
        repeated_password = input("Powtórz hasło:\n")
        first_name = input("Imię:\n")
        surname = input("Nazwisko:\n")
        address = input("Adres:\n")
        phone = input("Telefon kontaktowy:\n")

        if password == repeated_password and len(e_mail) > 0 and len(password) > 0:
            print("Twoje konto zostało utworzone :)")
            user = User(e_mail, password, first_name, surname, address, phone)
            app.users.add(user)
            self.login()
        else:
            # todo
            choice = input("Logowanie nieudane\n1-Spróbuj jeszcze raz\n2-Powrót\n")
            if choice == "1":
                self.create_account()
            elif choice == "2":
                self.menu()
            else:
                # todo
                print("Wprowadź poprawną liczbę!")

    def display_home(self):
        print("Ekran startowy użytkownika:")

    def check_credentials(self, e_mail, password):
        app = App()
        for x in app.users:
            if x.e_mail == e_mail and x.password == password:
                return x
        return None

    def login(self):
        app = App()
        correct_credentials = 0
        print("LOGOWANIE:\n")
        e_mail = input("E-mail: \n")
        password = input("Hasło: \n")
        user = self.check_credentials(e_mail, password)

        if user is not None:
            print("Logowanie udane")
            app.logged_in_user = user
            self.menu()
        else:
            choice = input("Logowanie zakończono niepowodzeniem\n1-Spróbuj jeszcze raz\n2-Powrót do menu\n")
            if choice == "1":
                self.login()
            elif choice == "2":
                self.menu()
            else:
                # todo
                print("Wprowadź poprawną liczbę!")

    def menu(self):
        app = App()
        if app.logged_in_user is None:
            menu_choice = input("-----------------------------------------------------------------------------------\n"
                                "Witamy w serwisie aukcji samochodowych!\n1-Zaloguj się\n2-Utwórz konto\n3-Zakończ\n"
                                "-----------------------------------------------------------------------------------\n")
            if menu_choice == "1":
                self.login()
            elif menu_choice == "2":
                self.create_account()
            elif menu_choice == "3":
                quit()
            else:
                # todo
                print("Wprowadź poprawną liczbę!")
        else:
            print(f"Witaj, {app.logged_in_user.first_name}\n")
            menu_choice = input("-----------------------------------------------------------------------------------\n"
                                "\n1-Pokaż listę aukcji\n2-Utwórz aukcję\n3-Wyloguj\n"
                                "-----------------------------------------------------------------------------------\n")

            if menu_choice == "1":
                show_auctions()
            elif menu_choice == "2":
                create_auction()
            elif menu_choice == "3":
                app.logged_in_user = None
                print("Wylogowany")
                self.menu()
            else:
                # todo
                print("Wprowadź poprawną liczbę!")

    def startApp(self):
        self.menu()
