# import itertools
# from datetime import datetime
#
#
# class Bid:
#     id_counter = itertools.count()
#
#     def __init__(self, money_offer, user):
#         self.id = next(self.id_counter)
#         self.money_offer = money_offer
#         self.user = user
#         self.created_at = datetime.now()
#         self.auction = None
