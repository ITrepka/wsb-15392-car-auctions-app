from user import User


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class App(metaclass=Singleton):
    def __init__(self):
        self.logged_in_user = None
        self.users = {User("i@wp.pl", "pass", "Grzegorz", "Brzęczyszczykiewicz", "Warszawka warszawka", "700800900")}
