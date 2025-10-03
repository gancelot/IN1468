"""

        task4_1_sqlalchemy_version (completed using SQLAlchemy)

"""
import sys

from sqlalchemy import create_engine, Column, select, String
from sqlalchemy.orm import Session, declarative_base
from sqlalchemy.exc import SQLAlchemyError


Base = declarative_base()


class School(Base):
    __tablename__ = 'schools'
    school_id = Column(String(30), primary_key=True)
    fullname = Column(String(50))
    city = Column(String(50))
    state = Column(String(15))
    country = Column(String(50))


try:
    engine = create_engine('sqlite:///course_data.db', echo=True)
except SQLAlchemyError as err:
    print(f'Error connecting to database.  Error: {err}', file=sys.stderr)
    sys.exit()


def get_location(school_name: str) -> list[School]:
    query_results = []
    try:
        with Session(engine) as session:
            stmt = select(School).filter(School.fullname.like(f'%{school_name}%'))
            query_results = session.scalars(stmt).all()
    except SQLAlchemyError as err:
        print(f'Error working with db.  Error: {err}', file=sys.stderr)
    return query_results


results = get_location('Loyola')

for school in results:
    print(f'{school.fullname:<40}{school.city:<20}{school.state:<4}')
