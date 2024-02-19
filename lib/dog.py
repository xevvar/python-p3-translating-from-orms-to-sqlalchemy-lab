from models import Dog
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def create_table(base, engine):
    engine = create_engine('sqlite:///lib/dogs.db')
    base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    return Session()

def save(session, dog):
    session.add(dog)
    session.commit()

def get_all(session):
    query = session.query(Dog).all()
    return query

def find_by_name(session, name):
    dog = session.query(Dog).filter(Dog.name == name).first()
    return dog

def find_by_id(session, id):
    return session.query(Dog).filter(Dog.id == id).first()

def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).filter_by(name=name, breed=breed).first()

def update_breed(session, dog, breed):
    dog.breed = breed
    session.commit()