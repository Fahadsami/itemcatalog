from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


from database_setup import Category, CategoryItem, User, Base

engine = create_engine('postgresql://catalog:PASSWORD@localhost/catalog')


Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

# Create dummy user
user1 = User(name="Fahad", email="alhamdanfahad2@gmail.com",
             picture='https://i.etsystatic.com/14449774/r/il/da71b3/1173059942/il_570xN.1173059942_hpl6.jpg')
session.add(user1)
session.commit()

# Items for Shooting games
category1 = Category(name="SHOOTER", user_id=1)

session.add(category1)
session.commit()

item1 = CategoryItem(name="Call of duty", user_id=1, description="Call of Duty is a first-person shooter video game franchise. The series began on Microsoft Windows, and expanded to consoles and handhelds. Several spin-off games have been released. The earlier games in the series are set primarily in World War II, but later games have typically been set in modern times or in futuristic settings. The most recent game.", category=category1)

session.add(item1)
session.commit()

item2 = CategoryItem(name="Battlefield", user_id=1,  description="Battlefield is a series of first-person shooter video games that started out on Microsoft Windows and OS X with Battlefield 1942, which was released in 2002. The series is developed by Swedish company EA DICE and is published by American company Electronic Arts. The series features a particular focus on large maps, teamwork and vehicle warfare.", category=category1)

session.add(item2)
session.commit()


# Items for MMO
category2 = Category(name="MMO", user_id=1)

session.add(category2)
session.commit()

item1 = CategoryItem(name="Tera", user_id=1, description="TERA (short for The Exiled Realm of Arborea) is a massively multiplayer online role-playing game (MMORPG) developed by KRAFTON. The game was released in South Korea on 25 January 2011, in North America on 1 May 2012, and in Europe on 3 May 2012, with closed and open beta testings taking place before the launch dates. NHN Corporation, NHN Japan Corporation, En Masse Entertainment and Gameforge publishes the game in these regions, respectively. In February 2013 the game was renamed to TERA: Rising concurrently with the game's launch to the free-to-play model.", category=category2)

session.add(item1)
session.commit()

item2 = CategoryItem(name="WOW", user_id=1,  description="World of Warcraft (WoW) is a massively multiplayer online role-playing game (MMORPG) released in 2004 by Blizzard Entertainment. It is the fourth released game set in the Warcraft fantasy universe.[3] World of Warcraft takes place within the Warcraft world of Azeroth, approximately four years after the events at the conclusion of Blizzard's previous Warcraft release, Warcraft III: The Frozen Throne.[4] The game was announced in 2001, and was released for the 10th anniversary of the Warcraft franchise on November 23, 2004. Since launch, World of Warcraft has had seven major expansion packs released for it: The Burning Crusade, Wrath of the Lich King, Cataclysm, Mists of Pandaria, Warlords of Draenor, Legion, and Battle for Azeroth.", category=category2)

session.add(item2)
session.commit()


# Items for RPG
category3 = Category(name="RPG", user_id=1)

session.add(category3)
session.commit()

item1 = CategoryItem(name="The wicher", user_id=1, description="The Witcher,by Polish writer Andrzej Sapkowski, is a fantasy series of short stories and novels about the witcher Geralt of Rivia. In Sapkowski's books,wichers are monster hunters who (with training and body modification) develop supernatural abilities at a young age to battle deadly beasts. The books have been adapted into a film, a television series, video games, and a graphic novel series. The series of novels is known as the Witcher Saga. The short stories and novels have been translated into numerous languages, including English..", category=category3)

session.add(item1)
session.commit()

item2 = CategoryItem(name="Dark souls", user_id=1, description="Dark Souls received critical acclaim upon its release and is considered to be one of the best video games ever made, with critics praising the depth of its combat, intricate level design, and world lore. However, the game's difficulty received mixed reviews. While some praised the challenge it provides, others criticized it for being unnecessarily unforgiving. The Windows version of the game was less well received, with criticism directed at numerous technical issues.", category=category3)

session.add(item2)
session.commit()



categories = session.query(Category).all()
for category in categories:
    print "Category: " + category.name
