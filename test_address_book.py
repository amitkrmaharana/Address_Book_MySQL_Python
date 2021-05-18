import mysql.connector

from AddressBook import AddressBook


class TestAddressBook:
    client = mysql.connector.connect(
        host="localhost",
        user="root",
        password="robowars@1amit",
    )
    mycursor = client.cursor()
    address_book = AddressBook()

    def test_create_database(self):
        """

        :return: to check if database is created or not
        """
        record_list = []
        database_name = "address_book_new"
        self.address_book.create_database()
        self.mycursor.execute("SHOW DATABASES")
        record = self.mycursor.fetchall()
        for values in record:
            record_list.append(values[0])
        assert database_name in record_list, "Database not created"
