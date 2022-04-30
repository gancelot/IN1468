"""
    simpsons.py - Allows for selecting data from the simpsons table in the database

    Table name: simpsons
    Columns: id, name, actor, role, episode_debut, original_air_date
"""
from contextlib import closing
import sqlite3


class Simpsons:
    SELECT_SIMPSONS_SQL = 'SELECT name, actor, role, episode_debut, original_air_date FROM simpsons WHERE name like ?'

    def __init__(self, db_filename):
        self.db_filename = db_filename

    def find(self, name: str):
        """
        Searches the Simpsons character info by providing a character name
        :param name: partial name of a Simpsons character
        :return: a list of Simpson characters returned
        """
        results = []
        err_msg = ''

        if not name:
            err_msg = 'char_name parameter is required.'
        else:
            with closing(sqlite3.connect(self.db_filename)) as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                params = ('%' + name + '%',)
                cursor.execute(self.SELECT_SIMPSONS_SQL, params)
                results = [dict(row) for row in cursor.fetchall()]

        return results