from app import App
# from auction import Auction
# from car import Car
# from user import User
from db_service import *
import hashlib


def show_auctions():
    app = App()
    print(app.auctions)


def print_auction_short(a):
    if a.bid is None:
        money_offer = "Brak ofert"
    else:
        bid_id = a.bid.id
        session = get_session()
        bid = get_bid_by_id(session, bid_id)
        money_offer = bid.money_offer

    print(f"<Aukcja(ID = {a.id}, tytuł = {a.title}, data zakończenia = {a.auction_end},"
          f" najwyższa oferta = {money_offer})>\n")


def my_auctions():
    app = App()
    session = get_session()
    user_id = app.logged_in_user.id
    auctions = get_auctions_by_user_id(session, user_id)

    for a in auctions:
        print_auction_short(a)


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

    current_timestamp = datetime.now()
    auction_end = current_timestamp + timedelta(days=int(auction_duration))

    car = Car(brand=brand, model=model, year=year, body_style=body_style, colour=colour,
              milleage_reading=milleage_reading, transmission=transmission, fuel=fuel, located_in=located_in,
              horse_power=horse_power, details=details, created_at=current_timestamp)
    session = get_session()
    car_id = save_car(session, car)
    print(car_id)
    auction = Auction(auction_duration=auction_duration, highest_bid_id=None, car_id=car_id,
                      starting_price=starting_price, minimal_price=minimal_price, buy_now_price=buy_now_price,
                      title=title,
                      auction_end=auction_end, created_at=current_timestamp, updated_at=current_timestamp,
                      owner_id=app.logged_in_user.id)
    save_auction(session, auction)
    session.commit()

    my_auctions()


def create_account():
    print("Tworzenie konta:\n")
    e_mail = input("Adres E-mail:\n")
    password = input("Hasło:\n")
    repeated_password = input("Powtórz hasło:\n")
    first_name = input("Imię:\n")
    surname = input("Nazwisko:\n")
    address = input("Adres:\n")
    phone = input("Telefon kontaktowy:\n")
    created_at = datetime.now()
    updated_at = datetime.now()
    if password == repeated_password and len(e_mail) > 0 and len(password) > 0:
        user = User(e_mail=e_mail, password=hashlib.md5(password.encode('utf-8')).hexdigest(), first_name=first_name,
                    surname=surname, address=address,
                    phone=phone, created_at=created_at, updated_at=updated_at)
        session = get_session()
        save_user(session, user)
        session.commit()
        print("Twoje konto zostało utworzone :)\n")
        login()
    else:
        # todo
        choice = input("Nieudane tworzenie konta\n1-Spróbuj jeszcze raz\n2-Powrót\n")
        if choice == "1":
            create_account()
        elif choice == "2":
            menu()
        else:
            # todo
            print("Wprowadź poprawną liczbę!")


def display_home():
    print("Ekran startowy użytkownika:")


def check_credentials(e_mail, password):
    session = get_session()
    user = get_user_by_email(session, e_mail)
    session.commit()
    if user is None:
        return None

    if hashlib.md5(password.encode('utf-8')).hexdigest() == user.password:
        return user
    else:
        return None


def login():
    app = App()
    print("LOGOWANIE:\n")
    e_mail = input("E-mail: \n")
    password = input("Hasło: \n")
    user = check_credentials(e_mail, password)

    if user is not None:
        print("Logowanie udane")
        app.logged_in_user = user
        menu()
    else:
        choice = input("Logowanie zakończono niepowodzeniem\n1-Spróbuj jeszcze raz\n2-Powrót do menu\n")
        if choice == "1":
            login()
        elif choice == "2":
            menu()
        else:
            # todo
            print("Wprowadź poprawną liczbę!")


def auctioned_by_me():
    pass


def my_auctions_menu():
    menu_choice = input("-----------------------------------------------------------------------------------\n"
                        "\n1-Pokaż aukcje stworzone przeze mnie\n2-Aukcje, w których biorę udział\n3-Powrót\n"
                        "-----------------------------------------------------------------------------------\n")

    if menu_choice == "1":
        my_auctions()
    elif menu_choice == "2":
        auctioned_by_me()
    elif menu_choice == "3":
        menu()
    else:
        # todo
        print("Wprowadź poprawną liczbę!")


def menu():
    app = App()
    if app.logged_in_user is None:
        menu_choice = input("-----------------------------------------------------------------------------------\n"
                            "Witamy w serwisie aukcji samochodowych!\n1-Zaloguj się\n2-Utwórz konto\n3-Zakończ\n"
                            "-----------------------------------------------------------------------------------\n")
        if menu_choice == "1":
            login()
        elif menu_choice == "2":
            create_account()
        elif menu_choice == "3":
            quit()
        else:
            # todo
            print("Wprowadź poprawną liczbę!")
    else:
        print(f"Witaj, {app.logged_in_user.first_name}\n")
        menu_choice = input("-----------------------------------------------------------------------------------\n"
                            "\n1-Pokaż listę wszystkich aukcji\n2-Pokaż moje aukcje\n3-Utwórz aukcję\n4-Wyloguj\n"
                            "-----------------------------------------------------------------------------------\n")

        if menu_choice == "1":
            show_auctions()
        elif menu_choice == "2":
            my_auctions_menu()
        elif menu_choice == "3":
            create_auction()
        elif menu_choice == "4":
            app.logged_in_user = None
            print("Wylogowany")
            menu()
        else:
            # todo
            print("Wprowadź poprawną liczbę!")


def startApp():
    menu()
