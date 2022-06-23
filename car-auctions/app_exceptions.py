class WrongMenuChoice(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"{self.value} jest nieprawidłowa wartościa. Nie ma takiej w menu."


class OfferedPriceLessThanCurrentPrice(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"{self.value} nie jest większa od aktualnej ceny samochodu"


class IsVacant(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"{self.value} pole nie może być puste"


class InvalidArgumentException(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"{self.value}"


class AuctionTerminated(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Aukcja o ID {self.value} dobiegła końca"