
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model import Base, Orders, Money , Menu, Users


class DB:

    def __init__(self, db_url):
        engine = create_engine(db_url, echo=True)
        Base.metadata.create_all(engine)
        self.session = sessionmaker(bind=engine)()

    def set_users(self, users):
        for person_id, display_name in users.items():
            self.session.merge(Users(person_id=person_id, display_name=display_name, collections=0))
        self.session.commit()

    def get_users(self, users):
        users = session.query(Users).all()
        result = {}
        for user in users:
            result[user.person_id] = user.display_name
        return result

    def set_menu(self, menu):
        for tag, menu_item in menu.items():
            self.session.merge(Menu(
                key_id=tag, name=menu_item[0], price=menu_item[1], spicy=menu_item[2]))
        self.session.commit()

    def get_menu(self):
        menus = self.session.query(Menu).all()
        result = {}
        for menu in menus:
            result[menu.key_id] = [menu.name, float(menu.price), menu.spicy]
        return result

    def set_money(self, money):
        print('setting money ', money)
        for person_id, balance in money.items():
            print(person_id, balance)
            self.session.merge(Money(person_id=person_id, balance=balance))
        self.session.commit()

    def get_money(self):
        bank = self.session.query(Money).all()
        result = {}
        for entry in bank:
            result[entry.person_id] = float(entry.balance)
        return result

    def set_usuals(self, defaults):
        users = self.session.query(Users).all()
        result = {}
        for person_id, entry in defaults.items():
            for user in users:
                if user.person_id == person_id:
                    user.default_order = entry
                    break
        self.session.commit()

    def get_usuals(self):
        users = self.session.query(Users).all()
        result = {}
        for entry in users:
            result[entry.person_id] = entry.default_order
        return result

    def get_orders(self):
        orders = self.session.query(Orders).all()
        result = []
        for entry in orders:
            notes = [] if entry.notes == "{}" else [entry.notes]
            result.append([entry.person_id, {
                'meal': entry.meal,
                'spicy': entry.spicy,
                'wings': entry.wings,
                'drink': entry.drink,
                'notes': notes,
                'price': float(entry.price),
            }])
        return result

    def set_orders(self, orders):
        for person_id, order in orders:
            self.session.merge(Orders(person_id=person_id, **order))
        self.session.commit()