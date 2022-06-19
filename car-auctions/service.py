from app import App
from user import User


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
            return user
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
                print("Pokazuje aukcje")
            elif menu_choice == "2":
                print("Stwórz aukcje")
            elif menu_choice == "3":
                app.logged_in_user = None
                print("Wylogowany")
                self.menu()
            else:
                # todo
                print("Wprowadź poprawną liczbę!")

    def startApp(self):
        self.menu()
