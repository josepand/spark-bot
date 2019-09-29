from sqlalchemy import Column, Sequence, Integer, String, DateTime, Numeric, Boolean, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
'''

        state = json.dumps(
            {
                'orders': self.orders,
                # convert money to regular dict
                'money': dict(self.money),
                'defaults': self.default_orders,
                'menu': self.menu,
            },
            separators=(',', ':')
        )

                    {
                'meal': meal_name,
                'spicy': spicy,
                'wings': wings,
                'drink': drink,
                'notes': comment,
                'price': price,
            }

'''

Base = declarative_base()

class Orders(Base):
    __tablename__ = 'orders'
    person_id = Column(String(120), primary_key=True)
    meal = Column(String(80))
    spicy = Column(Boolean())
    drink = Column(String(200))
    wings = Column(Integer())
    notes = Column(String(200))
    price = Column(Float(asdecimal=True))

    def __repr__(self):
        return f"<Orders('{self.id}', '{self.person_id}', '{self.meal}', '{self.spicy}', '{self.wings}', '{self.notes}', '{self.price}')>"

class Users(Base):
    __tablename__ = 'users'
    person_id = Column(String(120), primary_key=True)
    # user_balance = relationship("Money", backref="user")
    display_name = Column(String(300))
    collections = Column(Integer())
    default_order = Column(String(300))

    def __repr__(self):
        return f"<user('{self.person_id}', '{self.display_name}')>"

class Money(Base):
    __tablename__ = 'money'
    person_id = Column(String(120), primary_key = True)
    balance = Column(Float(asdecimal=True))

    def __repr__(self):
        return f"<Money('{self.person_id}', '{self.balance}')>"


class Menu(Base):
    __tablename__ = 'menu'
    key_id = Column(String(80), primary_key=True)
    name = Column(String(180))
    price = Column(Float(asdecimal=True))
    spicy = Column(Boolean())

    def __repr__(self):
        return f"<menu('{self.key_id}', '{self.name}', '{self.price}', '{self.spicy}')>"

