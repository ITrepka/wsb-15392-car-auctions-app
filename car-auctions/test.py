from car import Car
from user import User
# Timedelta function demonstration
from datetime import datetime, timedelta
from test_dto import create_tables

# Using current time
# time_for_now = datetime.now()
#
# furka = Car("perfetto","audi", "a3", 1999, "hatchback", "zielony", 190_000, "manualna", "diesel", "Warszawa", 190)
# furka2 = Car("perfetto","audi", "a3", 1999, "hatchback", "zielony", 190_000, "manualna", "diesel", "Warszawa", 190)
#
# print(furka.print_car())
# print(furka2.print_car())
#
#
# user = User("i@wp.pl", "pass", "Grzegorz", "Brzęczyszczykiewicz", "Warszawka warszawka", "700800900")
#
# print(user.print_user())
#
# print(time_for_now)
# print(time_for_now + timedelta(days=365))

create_tables()