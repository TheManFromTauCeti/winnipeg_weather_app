"""
This module holds the context manager which allows for a
more robust connection to the database.
"""

import sqlite3
import logging

class DBCM():
    """
    DBCM serves as the context manager for all operations
    with the database.
    """

    logger = logging.getLogger("main." + __name__)

    def __init__(self, app_database):
        """
        Initializes attributes for the DBCM context manager.
        """
        try:
            self.database_configuration = app_database
            self.conn = None
            self.cursor = None
        except Exception as error_message:
            self.logger.error("DBCM::__init__::%s", error_message)

    def __enter__(self):
        """
        Executes the setup code to connect to the database.
        """
        try:
            self.conn = sqlite3.connect(self.database_configuration)
            self.cursor = self.conn.cursor()

            return self.cursor
        except Exception as error_message:
            self.logger.error("DBCM::__enter__::%s", error_message)

    def __exit__(self, exc_type, exc_value, exc_trace):
        """
        Executes the teardown code to close the
        connection to the database.
        """
        try:
            self.conn.commit()
            self.cursor.close()
            self.conn.close()
        except Exception as error_message:
            self.logger.error("DBCM::__exit__::%s", error_message)
