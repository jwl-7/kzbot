"""Database Helper

This module helps the bot interface with the sqlite database.
"""


import sqlite3


class Database:
    """This class provides helper functions to communicate with the sqlite database."""

    def __init__(self, dbname='db/kzbot-localdb.sqlite'):
        """Creates database connection."""
        self.dbname = dbname
        self.conn = sqlite3.connect(dbname)

    def setup(self):
        """Creates new table and column."""
        stmt = '''
            CREATE TABLE IF NOT EXISTS
                players(
                    discord_id TEXT NOT NULL,
                    steam_id TEXT NOT NULL
                )
        '''
        self.conn.execute(stmt)
        self.conn.commit()

    def add_item(self, discord_id, steam_id):
        """Inserts item into table."""
        stmt = '''
            INSERT INTO
                players(discord_id, steam_id)
            VALUES
                (?, ?)
        '''
        args = (discord_id, steam_id)
        self.conn.execute(stmt, args)
        self.conn.commit()

    def delete_item(self, discord_id):
        """Deletes item from table."""
        stmt = '''
            DELETE FROM
                players
            WHERE
                discord_id = (?)
        '''
        args = (discord_id, )
        self.conn.execute(stmt, args)
        self.conn.commit()

    def update_item(self, discord_id, steam_id):
        """Update item in table."""
        stmt = '''
            UPDATE
                players
            SET
                steam_id = (?)
            WHERE
                discord_id = (?)
        '''
        args = (steam_id, discord_id)
        self.conn.execute(stmt, args)
        self.conn.commit()

    def get_items(self):
        """Gets all items from table."""
        stmt = '''
            SELECT
                *
            FROM
                players
            ORDER BY
                discord_id
        '''
        return [x for x in self.conn.execute(stmt)]

    def get_account(self, discord_id):
        """Get discord_id and steam_id from table."""
        stmt = '''
            SELECT
                *
            FROM
                players
            WHERE
                discord_id = (?)
        '''
        args = (discord_id, )
        return self.conn.execute(stmt, args).fetchone()
