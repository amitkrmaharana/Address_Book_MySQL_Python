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
                password="robowars@1amit",
                database="address_book_new"
            )
            self.mycursor = self.client.cursor()
        except Exception as e:
            logger.exception(e)

    def create_table(self):
        """

        :return: created a table
        """
        try:
            return self.mycursor.execute("CREATE TABLE contacts (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(250),"
                                         " city VARCHAR(250), state VARCHAR(250))")
        except Exception as e:
            logger.exception(e)
        finally:
            self.client.close()

    def insert_value_to_table(self):
        """

        :return:
        """
        try:
            sql = "INSERT INTO contacts (name, city, state) VALUES (%s, %s, %s)"
            val = [
                ("Amit", "Jamshedpur", "Jharkhand"),
                ('Peter', 'Longstreet 4', "US"),
                ('Amy', 'Apple st 652', "Canada"),
                ('Hannah', 'Mountain 21', "Delhi"),
                ('Michael', 'Bangalore', "Karnataka")
            ]
            return self.mycursor.execute(sql, val)
        except Exception as e:
            logger.exception(e)
        finally:
            self.client.close()
