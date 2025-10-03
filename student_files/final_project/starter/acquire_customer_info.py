from pathlib import Path
from typing import Sequence

import pandas as pd
from sqlalchemy import create_engine, Column, String, Integer, DateTime, Boolean, select
from sqlalchemy.orm import Session, declarative_base

Base = declarative_base()

db_location = Path(__file__).parents[1] / 'resources/customers.db'
print(f'Using database at location: {str(db_location)}')

engine = create_engine('sqlite:///' + str(db_location), echo=False)


class Customer(Base):
    __tablename__ = 'customers'
    customer_id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    email = Column(String(30))
    phone_number = Column(String(30))
    sign_up_date = Column(DateTime)
    address = Column(String(100))
    city = Column(String(50))
    state = Column(String(50))
    zip_code = Column(String(20))

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.customer_id})'

    __repr__ = __str__


class CustomerPreferences(Base):
    __tablename__ = 'customer_preferences'
    preference_id = Column(Integer, primary_key=True)
    customer_id = Column(Integer)
    preferred_contact_method = Column(String(30))
    marketing_opt_in = Column(Boolean)

    def __str__(self):
        return f'Preferred contact method: {self.preferred_contact_method}, marketing opt-in: {self.customer_id}'

    __repr__ = __str__


class CustomerOrders(Base):
    __tablename__ = 'customer_orders'
    order_id = Column(Integer, primary_key=True)
    customer_id = Column(Integer)
    order_date = Column(DateTime)
    total_amount = Column(Integer)
    order_status = Column(String(30))

    def __str__(self):
        return f'Order date: {self.order_date}, total amount: ${self.total_amount}, status: {self.order_status}'

    __repr__ = __str__

# Step 8. To save a little time, the SQLAlchemy models for the customer database
# have already been created for you (above).  You should complete this method which
# returns a list of Customer objects when called.  Do this by using SQLAlchemy's Session
# in a with control.  Perform a session.scalars(select(Customer)).all() to retrieve
# all customers.
def get_customers() -> Sequence[Customer]:
    pass


# Step 9. This function is a helper that will convert a list of Customers (from the above
# created method)  to a single Pandas DataFrame.  It is provided for you to save time.
def customers_to_dataframe(customers: Sequence[Customer]) -> pd.DataFrame:
    data_dict = {}
    for field in Customer.__table__.columns.keys():
        data_dict[field] = []
    for customer in customers:
        for field in Customer.__table__.columns.keys():
            data_dict[field].append(getattr(customer, field))
    return pd.DataFrame(data_dict)


# Step 10. The get_customers_preferences(customer_id) method will return a single
# CustomerPreferences object based on a provided customer_id.
# Use the following SQLAlchemy statements to achieve this:
#         stmt = select(CustomerPreferences).where(CustomerPreferences.customer_id == customer_id)
#         customer_preferences = session.scalars(stmt).first()
def get_customers_preferences(customer_id: int) -> CustomerPreferences | None:
    pass


# Step 11 is nearly identical to step 10 except it is for customer orders.
# Use the following SQLAlchemy statements to complete the method:
#         stmt = select(CustomerOrders).where(CustomerOrders.customer_id == customer_id)
#         customer_orders = session.scalars(stmt).first()
def get_customer_orders(customer_id: int) -> CustomerOrders | None:
    pass


"""
Entry point of the script. Retrieves all customers from the database
and displays their details, preferences, and orders in the console.
Run this file when finished and the code below should execute displaying all customer
information.
"""
if __name__ == '__main__':
    for customer in get_customers():
        print(customer)
        print(get_customers_preferences(customer.customer_id))
        print(get_customer_orders(customer.customer_id))
