from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, Base, Item, User

engine = create_engine('sqlite:///itemcatalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create dummy user
User1 = User(name="Robo Barista", email="tinnyTim@udacity.com")
session.add(User1)
session.commit()


# Menu for UrbanBurger
category1 = Category(name="Dogs")

session.add(category1)
session.commit()


item1 = Item(user_id=1, name="Shiba Inu",
             description="They are adorable",
             category=category1)

session.add(item1)
session.commit()

item2 = Item(user_id=1, name="Labrador",
             description="They are also really cute",
             category=category1)

session.add(item2)
session.commit()

item3 = Item(user_id=1, name="Wolf",
             description="Unquestionably the best",
             category=category1)

session.add(item3)
session.commit()


# Menu for Super Stir Fry
category2 = Category(name="Cats")

session.add(category2)
session.commit()


item1 = Item(user_id=1, name="Persian",
             description="Absolutely fluffy",
             category=category2)

session.add(item1)
session.commit()

item2 = Item(user_id=1, name="Abyssinian",
             description="Adorable little buggers",
             category=category2)

session.add(item2)
session.commit()

item3 = Item(user_id=1, name="Tiger",
             description="Built for hugs",
             category=category2)

session.add(item3)
session.commit()


# Menu for Panda Garden
category1 = Category(name="Rats")

session.add(category1)
session.commit()


item1 = Item(user_id=1, name="100 Dirty Rats",
             description="This is trouble.",
             category=category1)

session.add(item1)
session.commit()

item2 = Item(user_id=1, name="1000 Filthy Rats",
             description="This is getting out of hand...",
             category=category1)

session.add(item2)
session.commit()

item3 = Item(user_id=1, name="100000000 Plagued Rats",
             description="HELP!!!",
             category=category1)

session.add(item3)
session.commit()


print("added items!")