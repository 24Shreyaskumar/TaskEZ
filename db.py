'''Configure Database Connection'''

import sqlite3

class Database:
    '''Task EZ Database'''
    def __init__(self, db_name="taskez.db"):
        '''Initialize DB Connection'''
        self.conn = sqlite3.connect(db_name)
        self.conn.execute("PRAGMA foreign_keys = ON") # to support foreign key references
        self.conn.row_factory = sqlite3.Row()

    def execute(self, query, params=()):
        '''Execute given DB command'''
        cursor = self.conn.cursor()
        cursor.execute(query, params)
        self.conn.commit()
        return cursor

    def executemany(self, query, param_list):
        '''Execute multiple DB commands at once'''
        cursor = self.conn.cursor()
        cursor.executemany(query, param_list)
        self.conn.commit()
        return cursor

    def close(self):
        '''Close DB connection'''
        self.conn.close()
