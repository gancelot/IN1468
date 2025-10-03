from sqlalchemy import create_engine, Column, select, String
from sqlalchemy.orm import Session, declarative_base


Base = declarative_base()


class School(Base):
    __tablename__ = 'schools'
    school_id = Column(String(30), primary_key=True)
    fullname = Column(String(50))
    city = Column(String(50))
    state = Column(String(15))
    country = Column(String(50))


engine = create_engine('sqlite:///course_data.db', echo=True)


with Session(engine) as session:
    stmt = select(School)
    firstSchool = session.scalars(stmt).first()             # returns the first record or none if nont found
    print(firstSchool.fullname, firstSchool.country)
    firstSchool.country = 'U.S.'                                    # changed the country attribute

with Session(engine) as session:
    stmt = select(School)
    school = session.scalars(stmt).first()
    print(school.fullname, school.country)


with Session(engine) as session:
    stmt = select(School)
    firstSchool = session.scalars(stmt).first()
    firstSchool.country = 'USA'
    print(firstSchool.fullname, firstSchool.country)
