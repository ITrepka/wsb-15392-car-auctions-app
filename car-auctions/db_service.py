import hashlib
from datetime import datetime, timedelta
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = sqlalchemy.create_engine('mysql+mysqlconnector://root:root@localhost:3306/car_auctions',
                                  echo=False)

Base = declarative_base()


def sort_key(bid):
    return bid.money_offer


class Auction(Base):
    __tablename__ = 'auctions'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    auction_duration = sqlalchemy.Column(sqlalchemy.Integer)
    highest_bid_id = sqlalchemy.Column(sqlalchemy.Integer)
    car_id = sqlalchemy.Column(sqlalchemy.Integer)
    starting_price = sqlalchemy.Column(sqlalchemy.Numeric)
    minimal_price = sqlalchemy.Column(sqlalchemy.Numeric)
    buy_now_price = sqlalchemy.Column(sqlalchemy.Numeric)
    title = sqlalchemy.Column(sqlalchemy.String(length=100))
    auction_end = sqlalchemy.Column(sqlalchemy.DateTime)
    created_at = sqlalchemy.Column(sqlalchemy.DateTime)
    updated_at = sqlalchemy.Column(sqlalchemy.DateTime)
    owner_id = sqlalchemy.Column(sqlalchemy.Integer)


class Bid(Base):
    __tablename__ = "bids"
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    money_offer = sqlalchemy.Column(sqlalchemy.Numeric)
    user_id = sqlalchemy.Column(sqlalchemy.Integer)
    created_at = sqlalchemy.Column(sqlalchemy.DateTime)
    auction_id = sqlalchemy.Column(sqlalchemy.Integer)


class User(Base):
    __tablename__ = "users"
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    e_mail = sqlalchemy.Column(sqlalchemy.String(length=50), unique=True)
    password = sqlalchemy.Column(sqlalchemy.String(length=50))
    first_name = sqlalchemy.Column(sqlalchemy.String(length=50))
    surname = sqlalchemy.Column(sqlalchemy.String(length=50))
    address = sqlalchemy.Column(sqlalchemy.String(length=100))
    phone = sqlalchemy.Column(sqlalchemy.String(length=50))
    created_at = sqlalchemy.Column(sqlalchemy.DateTime)
    updated_at = sqlalchemy.Column(sqlalchemy.DateTime)


class Car(Base):
    __tablename__ = "cars"
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    brand = sqlalchemy.Column(sqlalchemy.String(length=50))
    model = sqlalchemy.Column(sqlalchemy.String(length=50))
    year = sqlalchemy.Column(sqlalchemy.Integer)
    body_style = sqlalchemy.Column(sqlalchemy.String(length=50))
    colour = sqlalchemy.Column(sqlalchemy.String(length=50))
    milleage_reading = sqlalchemy.Column(sqlalchemy.String(length=50))
    transmission = sqlalchemy.Column(sqlalchemy.String(length=50))
    fuel = sqlalchemy.Column(sqlalchemy.String(length=50))
    located_in = sqlalchemy.Column(sqlalchemy.String(length=100))
    horse_power = sqlalchemy.Column(sqlalchemy.Integer)
    details = sqlalchemy.Column(sqlalchemy.String(length=200))
    created_at = sqlalchemy.Column(sqlalchemy.DateTime)


def update_auction(session, auction, user_id, bid_id):
    session.query(Auction).filter(Auction.id == auction.id).update({"highest_bid_id": bid_id,
                                                                    "updated_at": datetime.now()},
                                                                   synchronize_session="fetch")


def get_session():
    Session = sqlalchemy.orm.sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    return session


def init():
    create_database()
    create_tables()
    # create_init_user(session)


def create_init_user():
    session = get_session()
    user_password = hashlib.md5("pass".encode('utf-8')).hexdigest()
    user = User(e_mail="root@gmail.com", password=user_password, first_name="Ireneusz",
                surname="Trepka", address="LA 101", phone="999000111")
    session.add(user)
    session.commit()


def create_database():
    engine2 = sqlalchemy.create_engine('mysql://root:root@localhost:3306')  # connect to server
    conn = engine2.connect()
    conn.execute("create database if not exists car_auctions")
    conn.close()


def get_car_by_id(session, car_id):
    car = session.query(Car).filter(Car.id == car_id).one()
    session.commit()
    return car


def create_tables():
    Base.metadata.create_all(engine)


def get_bids_by_user_id(session, user_id):
    bid = session.query(Bid).filter(Bid.user_id == user_id)
    session.commit()
    return bid


def get_auction_by_id(session, auction_id):
    auction = session.query(Auction).filter(Auction.id == auction_id).one()
    session.commit()
    return auction


def get_bid_by_id(session, bid_id):
    bid = session.query(Bid).filter(Bid.id == bid_id).one()
    session.commit()
    return bid


def get_owner_auctions(session, owner_id):
    auctions = []
    for s in session.query(Auction).filter(Auction.owner_id == owner_id):
        auctions.append(s)

    session.commit()

    return auctions


def get_user_by_id(session, user_id):
    user = session.query(User).filter(User.id == user_id)
    session.commit()
    return user


def get_user_by_email(session, user_email):
    user = session.query(User).filter(User.e_mail == user_email)
    if user.count() > 0:
        return user[0]
    else:
        return None


def get_all_auctions(session):
    auctions = []
    for s in session.query(Auction).all():
        auctions.append(s)
    return auctions


def get_auctions_by_user_id(session, user_id):
    auctions = []
    for s in session.query(Auction).filter(Auction.owner_id == user_id):
        auctions.append(s)
    return auctions


def save_user(session, user):
    session.add(user)
    session.commit()
    return user.id


def save_auction(session, auction):
    session.add(auction)
    session.commit()
    return auction.id


def save_car(session, car):
    session.add(car)
    session.commit()
    return car.id


def save_bid(session, bid):
    session.add(bid)
    session.commit()
    return bid.id

# Session = sqlalchemy.orm.sessionmaker()
# Session.configure(bind=engine)
# session = Session()
#
# ju1 = User(name="Marcin", fullname="Marcin Albiniak", nickname="marc")
# session.query.
# session.commit()
#
# ju2 = User(name="Olga", fullname="Olga Kot", nickname="kotka")
# session.add(ju2)
# session.commit()
#
# Session = sessionmaker(bind=engine)
# session = Session()
#
# print("***** wszystkie dane *******")
#
# for s in session.query(User).all():
#     print(s.fullname)
#
# print("***** filtrowane dane *******")
#
# for s in session.query(User).filter(User.nickname == 'marc'):
#     print(s.fullname)
