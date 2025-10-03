"""
    16_decorators.py

    A transactional decorator.
"""
import sys


class Session:
    """Simulates a transaction session"""
    def begin(self):
        print('begin')

    def commit(self):
        print('commit')

    def rollback(self):
        print('rollback')


class Transactional(object):
    def __init__(self, session):
        self.session = session

    def tx(self, func):
        def wrapper(*args, **kwargs):
            ret=None
            self.session.begin()
            try:
                # kwargs['foo'] = 'bar'         # add this in to cause a rollback
                ret = func(*args, **kwargs)
                self.session.commit()
            except Exception as err:
                print(err, file=sys.stderr)
                self.session.rollback()

            return ret
        return wrapper


tx = Transactional(Session())


@tx.tx
def work():
    print('doing work')


work()
