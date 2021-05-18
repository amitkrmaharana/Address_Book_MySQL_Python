import mysql.connector

from logger import logger


class AddressBook:

    def __init__(self):
        """
        connecting to MySQL server
        """
        try:
            self.client = mysql.connector.connect(
                host="localhost",
                user="root",
                password="robowars@1amit"
            )
            self.mycursor = self.client.cursor()
        except Exception as e:
            logger.exception(e)

    def create_database(self):
        """

        :return: created a database
        """
        try:
            return self.mycursor.execute("CREATE DATABASE address_book_new")
        except Exception as e:
            logger.exception(e)
