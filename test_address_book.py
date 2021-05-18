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
        self.client.close()
        assert table_name in record_list, "Table not created"

    def test_insert_values(self):
        """

        :return:
        """
        self.address_book.insert_value_to_table()
        rows_count = self.mycursor.rowcount
        self.client.close()
        assert rows_count == 1, "Values not inserted to table"
