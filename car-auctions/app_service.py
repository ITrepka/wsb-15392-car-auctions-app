from app import App
# from auction import Auction
# from car import Car
# from user import User
from db_service import *
import hashlib


def print_car(car):
    print(f"Marka: {car.brand}, Model: {car.model}, Rok produkcji: {car.year}, Typ nadwozia: {car.body_style}"
          f"Kolor: {car.colour}, Przebieg: {car.milleage_reading}, Skrzynia biegów: {car.transmission}"
          f"Paliwo: {car.fuel}, Lokalizacja: {car.located_in}, Liczba koni mechanicznych: {car.horse_power}\n"
          f"Inne informacje: {car.details}")


def show_auction_details(auction):
    session = get_session()
    if auction.highest_bid_id is not None:
        bid = get_bid_by_id(session, auction.highest_bid_id)
        current_price = bid.money_offer
    else:
        current_price = auction.starting_price

    car = get_car_by_id(session, auction.car_id)
    print(f"Aukcja: {auction.id}\nTytuł: {auction.title}\nAktualna cena: {current_price}\n"
          f"Kup Teraz: {auction.buy_now_price}\nData Zakończenia Aukcji: {auction.auction_end}\n"
          f"\nPrzedmiot aukcji:\n{print_car(car)}")


def add_bid(auction):
    app = App()
    user_id = app.logged_in_user.id
    money_offer = input("Podaj kwotę:\n")
    session = get_session()
    current_timestamp = datetime.now()
    bid = Bid(money_offer=money_offer, user_id=user_id, created_at=current_timestamp, auction_id=auction.id)
    bid_id = save_bid(session, bid)


def buy_now(auction):
    app = App()
    user_id = app.logged_in_user.id
    session = get_session()
    current_timestamp = datetime.now()
    bid = Bid(money_offer=auction.buy_now_price, user_id=user_id, created_at=current_timestamp, auction_id=auction.id)
    bid_id = save_bid(session, bid)
    # todo edit auction
    update_auction(session, auction, user_id, bid_id)


def take_part_auction():
    auction_id = input("Podaj ID aukcji:\n")
    session = get_session()
    auction = get_auction_by_id(session, auction_id)
    show_auction_details(auction)
    menu_choice = input("-----------------------------------------------------------------------------------\n"
                        "1-Licytuj\n2-Kup teraz\n3-Powrót\n4-Menu Główne\n"
                        "-----------------------------------------------------------------------------------\n")

    if menu_choice == "1":
        add_bid(auction)
    elif menu_choice == "2":
        buy_now(auction)
    elif menu_choice == "3":
        show_auctions(None)
    elif menu_choice == "4":
        menu()


def filter_auctions(auctions):
    menu_choice = input("-----------------------------------------------------------------------------------\n"
                        "1-Cena Max\n2-Lokalizacja\n3-Model\n4-Usuń Filtry\n5-Powrót\n"
                        "-----------------------------------------------------------------------------------\n")
    filtered = []

    # auctions = get_all_auctions(session)
    if menu_choice == "1":
        max_price = input("Podaj cenę maksymalną: \n")
        session = get_session()
        for a in auctions:
            if a.highest_bid_id is not None:
                bid = get_bid_by_id(session, a.highest_bid_id)
                if bid.money_offer <= int(max_price):
                    filtered.append(a)
            else:
                if a.starting_price <= int(max_price):
                    filtered.append(a)

        show_auctions(filtered)
    elif menu_choice == "2":
        localization = input("Podaj nazwę miasta: \n")
        for a in auctions:
            session = get_session()
            print(a.id)
            print(a.car_id)
            car = get_car_by_id(session, a.car_id)
            print(car.id)
            if car.located_in.lower() == localization.lower():
                filtered.append(a)
        show_auctions(filtered)
    elif menu_choice == "3":
        model = input("Podaj model samochodu: \n")
        for a in auctions:
            session = get_session()
            car = get_car_by_id(session, a.car_id)
            if car.model.lower() == model.lower():
                filtered.append(a)
        show_auctions(filtered)
    elif menu_choice == "4":
        show_auctions(None)
    elif menu_choice == "5":
        show_auctions(auctions)


def partition(array, start, end, compare_func):
    pivot = array[start]
    low = start + 1
    high = end

    while True:
        while low <= high and compare_func(array[high], pivot):
            high = high - 1

        while low <= high and not compare_func(array[low], pivot):
            low = low + 1

        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break

    array[start], array[high] = array[high], array[start]

    return high


def quick_sort(array, start, end, compare_func):
    if start >= end:
        return

    p = partition(array, start, end, compare_func)
    quick_sort(array, start, p - 1, compare_func)
    quick_sort(array, p + 1, end, compare_func)


def sort_auctions(auctions):
    menu_choice = input("-----------------------------------------------------------------------------------\n"
                        "1-Cena rosnąco\n2-Cena malejąco\n3-Data zakończenia rosnąco\n"
                        "4-Data zakończenia rosnąco\n5-Powrót do Menu\n"
                        "-----------------------------------------------------------------------------------\n")
    if menu_choice == "1":
        session = get_session()
        offers = {}
        sorted_auctions = []
        for a in auctions:
            if a.highest_bid_id is not None:
                bid = get_bid_by_id(session, a.highest_bid_id)
                offers[a.id] = bid.money_offer
            else:
                offers[a.id] = a.starting_price
        offers = sorted(offers.items(), key=lambda x: x[1])
        print(offers)
        for auction_id in offers:
            sorted_auctions.append(get_auction_by_id(session, auction_id[0]))
        show_auctions(sorted_auctions)
    elif menu_choice == "2":
        session = get_session()
        offers = {}
        sorted_auctions = []
        for a in auctions:
            if a.highest_bid_id is not None:
                bid = get_bid_by_id(session, a.highest_bid_id)
                offers[a.id] = bid.money_offer
            else:
                offers[a.id] = a.starting_price
        offers = sorted(offers.items(), key=lambda x: x[1], reverse=True)
        print(offers)
        for auction_id in offers:
            sorted_auctions.append(get_auction_by_id(session, auction_id[0]))
        show_auctions(sorted_auctions)
    elif menu_choice == "3":
        sorted_auctions = auctions
        quick_sort(auctions, 0, len(auctions) - 1, lambda x, y: x.auction_end > y.auction_end)
        show_auctions(sorted_auctions)
    elif menu_choice == "4":
        sorted_auctions = auctions
        quick_sort(auctions, 0, len(auctions) - 1, lambda x, y: x.auction_end < y.auction_end)
        show_auctions(sorted_auctions)
    elif menu_choice == "5":
        menu()
    else:
        # todo
        print("Wprowadź poprawną liczbę!")
        sort_auctions(auctions)


def show_auctions(auctions):
    print("-----------------------------------------------------------------------------------\n"
          "Aukcje!\n"
          "-----------------------------------------------------------------------------------\n")
    session = get_session()
    if auctions is None:
        auctions = get_all_auctions(session)

    for a in auctions:
        print_auction_short(a)

    menu_choice = input("1-Filtry\n2-Sortuj\n3-Licytuj\n4-Powrót do Menu\n")

    if menu_choice == "1":
        filter_auctions(auctions)
    elif menu_choice == "2":
        sort_auctions(auctions)
    elif menu_choice == "3":
        take_part_auction()
    elif menu_choice == "4":
        menu()
    else:
        # todo
        print("Wprowadź poprawną liczbę!")
        show_auctions(auctions)


def print_auction_short(a):
    if a.highest_bid_id is None:
        money_offer = 0
    else:
        bid_id = a.highest_bid_id
        session = get_session()
        bid = get_bid_by_id(session, bid_id)
        money_offer = bid.money_offer

    print(f"<Aukcja(ID = {a.id}, tytuł = {a.title}, data zakończenia = {a.auction_end},"
          f"aktualna_cena = {max(money_offer, a.starting_price)})>\n")


def my_auctions():
    print("-----------------------------------------------------------------------------------\n"
          "Moje Aukcje!"
          "-----------------------------------------------------------------------------------\n")
    app = App()
    session = get_session()
    user_id = app.logged_in_user.id
    auctions = get_auctions_by_user_id(session, user_id)

    for a in auctions:
        print_auction_short(a)

    menu_choice = input("-----------------------------------------------------------------------------------\n"
                        "1-Pokaż szczegóły wybranej aukcji\n2-Licytuj\n3-Powrót do Menu\n"
                        "-----------------------------------------------------------------------------------\n")
    if menu_choice == "1":
        session = get_session()
        auction_id = input("Podaj ID aukcji:\n")
        auction = get_auction_by_id(session, auction_id)
        show_auction_details(auction)
    elif menu_choice == "2":
        take_part_auction()
    elif menu_choice == "3":
        menu()
    else:
        # todo
        print("Wprowadź poprawną liczbę!")
        my_auctions()


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
    milleage_reading = input("Liczba przejechanych kilometrów na liczniku:\n")
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
            login()


def auctioned_by_me():
    app = App()
    session = get_session()
    user_id = app.logged_in_user.id
    bids = get_bids_by_user_id(session, user_id)
    for b in bids:
        # todo distinct
        auction = get_auction_by_id(session, b.auction_id)
        print_auction_short(auction)


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
            show_auctions(None)
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
