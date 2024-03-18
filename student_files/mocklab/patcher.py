import json
from contextlib import closing
from pathlib import Path
import sqlite3
from threading import RLock

patched_items = {}


def patch(module, attr, newitem):
    olditem = getattr(module, attr, object())
    if olditem is not object():
        patched_items[(module, attr)] = olditem
    setattr(module, attr, newitem)


class RequestsGet:
    def __init__(self):
        self.url = None

    def __call__(self, *args, **kwargs):
        self.requests_get(*args, **kwargs)
        return self

    def requests_get(self, url='', params=None, **kwargs):
        self.url = url
        return self

    def json(self):
        return json.loads(self.text)

    @property
    def text(self):
        sql = 'SELECT url, text FROM websites WHERE url=?'

        data_file = Path(__file__).parent / 'urls.db'
        try:
            with closing(sqlite3.connect(data_file)) as conn:
                cursor = conn.cursor()
                cursor.execute(sql, (self.url,))
                results = cursor.fetchone()
                return results[1]
        except Exception as err:
            return f'<html><head><title>Error within Mocklab</title></head><body>{err}.</body></html>'
