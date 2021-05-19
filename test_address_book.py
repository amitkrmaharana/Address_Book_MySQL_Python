import mysql.connector

from AddressBook import AddressBook


class TestAddressBook:
    client = mysql.connector.connect(
        host="localhost",
        user="root",
        password="robowars@1amit",
        database="address_book_new"
    )
    mycursor = client.cursor()
    address_book = AddressBook()

    def test_create_table(self):
        """

        :return: to check if table is created or not
        """
        record_list = []
        table_name = "contacts"
        self.address_book.create_table()
        self.mycursor.execute("SHOW TABLES")
        record = self.mycursor.fetchall()
        for values in record:
            record_list.append(values[0])
        assert table_name in record_list, "Table not created"

    def test_insert_values(self):
        """

        :return: to check number of rows inserted
        """
        result = self.address_book.insert_value_to_table()
        assert result == 5, "Values not inserted"

    def test_delete_row(self):
        """

        :return: to check if row referenced is deleted or not
        """
        name = "Hannah"
        result = self.address_book.delete_row(name)
        assert result == 1, "Row not deleted"

