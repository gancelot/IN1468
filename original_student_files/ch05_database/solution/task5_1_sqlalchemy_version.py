"""

        task5_1_sqlalchemy_version (completed using SQLAlchemy)

"""
from sqlalchemy import create_engine, Column
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.types import String
from sqlalchemy.exc import SQLAlchemyError
import sys


Base = declarative_base()


class School(Base):
    __tablename__ = 'schools'
    school_id = Column(String(30), primary_key=True)
    fullname = Column(String(50))
    city = Column(String(50))
    state = Column(String(15))
    country = Column(String(50))


try:
    db = create_engine('sqlite:///course_data.db', echo=True)
    Session = sessionmaker(bind=db, autocommit=True)
except SQLAlchemyError as err:
    print(f'Error connecting to database.  Error: {err}', file=sys.stderr)
    sys.exit()


def get_location(school_name):
    session = None
    query_results = []
    try:
        with Session() as session:
            query_results = session.query(School).filter(School.fullname.like('%'+school_name+'%')).all()
    except SQLAlchemyError as err:
        print(f'Error working with db.  Error: {err}', file=sys.stderr)
    return query_results


results = get_location('Loyola')

for school in results:
    print(f'{school.fullname:<40}{school.city:<20}{school.state:<4}')
