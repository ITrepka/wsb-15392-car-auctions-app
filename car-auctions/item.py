import itertools


class Item:
    id_counter = itertools.count()

    def __init__(self, name, description, starting_price, minimal_price, buy_now_price):
        self.id = next(self.id_counter)
        self.name = name
        self.description = description
        self.starting_price = starting_price
        self.minimal_price = minimal_price
        self.buy_now_price = buy_now_price
