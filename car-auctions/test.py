from car import Car
from user import User

furka = Car("Czerwony kabriolet!", "tanio, przystępnie", 1200, 2000, 2500,
                 "audi", "a3", 1999, "hatchback", "zielony", 190_000, "manualna", "diesel", "Warszawa", 190)
furka2 = Car("Czerwony kabriolet!", "tanio, przystępnie", 1200, 2000, 2500,
                 "audi", "a3", 1999, "hatchback", "zielony", 190_000, "manualna", "diesel", "Warszawa", 190)

print(furka.print_car())
print(furka2.print_car())


user = User("i@wp.pl", "pass", "Grzegorz", "Brzęczyszczykiewicz", "Warszawka warszawka", "700800900")

print(user.print_user())
