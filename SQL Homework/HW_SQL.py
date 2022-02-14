import mysql.connector

"""Подключился к уже существующей базе данных"""
connect_database = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='145863',
    database='test_database'
)

cursor = connect_database.cursor()

# cursor.execute('CREATE TABLE orders (ord_no INT NOT NULL, '
#                'purch_amt DECIMAL(10,2), '
#                'ord_date DATE NOT NULL, '
#                'customer_id INT NOT NULL, '
#                'salesman_id INT NOT NULL)')

# cursor.execute('SHOW TABLES')
# for tables in cursor:
#     print(tables)

# insert_info = "INSERT INTO orders (ord_no, purch_amt, ord_date, customer_id, salesman_id)" \
#               "VALUES " \
#               "(70001, 150.5, '2012-10-05', 3005, 5002)," \
#               "(70009, 270.65, '2012-09-10', 3001, 5005)," \
#               "(70002, 62.26, '2012-10-05', 3002, 5001)," \
#               "(70004, 110.5, '2012-08-17', 3009, 5003), " \
#               "(70007, 948.5, '2012-09-10', 3005, 5002), " \
#               "(70005, 2400.6, '2012-07-27', 3007, 5001), " \
#               "(70008, 5760, '2012-09-10', 3002, 5001)," \
#               "(70010, 1983.43, '2012-10-10', 3004, 5006)," \
#               "(70003, 2480.4, '2012-10-10', 3009, 5003)," \
#               "(70012, 250.45, '2012-06-27', 3008, 5002)," \
#               "(70011, 75.29, '2012-08-17', 3003, 5007)," \
#               "(70013, 3045.6, '2012-04-25', 3002, 5001)"
# cursor.execute(insert_info)
# connect_database.commit()

"""информация о продавце 5002"""
cursor.execute('SELECT * FROM test_database.orders WHERE salesman_id = 5002')
for info in cursor:
    print(info)

"""id всех продавцов"""
cursor.execute("SELECT DISTINCT salesman_id FROM orders")
for i in cursor:
    print(i)

"""заказы между 70001 и 70007"""
cursor.execute("SELECT ord_no, purch_amt, customer_id FROM orders WHERE ord_no BETWEEN 70001 AND 70007")
for ord_info in cursor:
    print(ord_info)

"""сотировка id"""
cursor.execute("SELECT DISTINCT salesman_id FROM orders")
ids_list = []
for i in cursor:
    ids_list.append(str(i))
ids_list.sort()
print(f'Sorted salesman id is: {".".join((map(str, ids_list)))}')

"""сортировка номера заказа"""
cursor.execute("SELECT ord_no FROM orders")
list_of_orders = []
for order in cursor:
    list_of_orders.append(str(order))
list_of_orders.sort()
print(f'Sorted orders is: {".".join((map(str, list_of_orders)))}')

"""сортировка количества"""
cursor.execute("SELECT purch_amt FROM orders ORDER BY purch_amt ASC")
for amt in cursor:
    print(amt)

"""сортировка даты"""
cursor.execute("SELECT ord_date FROM orders ORDER BY ord_date ASC")
for date in cursor:
    print(date)
#
# connect_database.close()
