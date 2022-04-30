from sqlalchemy import create_engine, Column
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.types import String

Base = declarative_base()


class School(Base):
    __tablename__ = 'schools'
    school_id = Column(String(30), primary_key=True)
    fullname = Column(String(50))
    city = Column(String(50))
    state = Column(String(15))
    country = Column(String(50))


db = create_engine('sqlite:///course_data.db', echo=True)
Session = sessionmaker(bind=db, autocommit=True)

with Session.begin() as session:
    firstSchool = session.query(School).first()
    print(firstSchool.fullname, firstSchool.country)
    firstSchool.country = 'U.S.'                        # changed the country attribute


with Session() as session:
    school = session.query(School).first()
    print(school.fullname, school.country)


with Session.begin() as session:
    firstSchool = session.query(School).first()
    firstSchool.country = 'USA'
    print(firstSchool.fullname, firstSchool.country)
