# import itertools
#
# from bid import Bid
# from datetime import datetime, timedelta
#
#
# def sort_key(bid):
#     return bid.money_offer
#
#
# class Auction:
#     id_counter = itertools.count()
#
#     def __init__(self, auction_duration, item, starting_price, minimal_price, buy_now_price, title):
#         self.id = next(self.id_counter)
#         self.auction_duration = auction_duration
#         self.current_bid = None
#         self.bid_history = []
#         self.item = item
#         self.starting_price = starting_price
#         self.minimal_price = minimal_price
#         self.buy_now_price = buy_now_price
#         self.title = title
#         self.auction_end = datetime.now() + timedelta(days=int(auction_duration))
#         self.created_at = datetime.now()
#
#     def add_bid(self, offer, user):
#         max_offer = self.bid_history.sort(key=sort_key)[0]
#         #todo sprawdzenie czy przed czasem
#         if offer > max_offer:
#             new_bid = Bid(offer, user)
#             self.bid_history.append(new_bid)
#             self.current_bid = new_bid
#         else:
#             print("Za mała kwota")
#     # todo wyjatek rzucany gdy oferta jest mniejsza niz najwyzsza obecne


