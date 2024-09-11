'''
Programmer: Amna(23k-0066)
Date: 11/Sept/2024
Q5) Write a Python class Restaurant with attributes like menu_items, book_table, and
    customer_orders, and methods like add_item_to_menu, book_tables, and customer_order.
    Perform the following tasks now:
     Now add items to the menu.
     Make table reservations.
     Take customer orders.
     Print the menu.
     Print table reservations.
     Print customer orders.
    Note: Use dictionaries and lists to store the data.
'''

class Restaurant:
    def __init__(self):
        self.menu_items = {}  
        self.booked_tables = []  
        self.customer_orders = {}  

    # Methods
    def add_item_to_menu(self, item_name, price):
        self.menu_items[item_name] = price
        print(f"{item_name} has been added to the menu.")

    def book_table(self, table_number):
        if table_number not in self.booked_tables:
            self.booked_tables.append(table_number)
            print(f"Table {table_number} has been booked.")
        else:
            print(f"Table {table_number} is already booked.")

    def customer_order(self, table_number, order_items):
        if table_number not in self.booked_tables:
            print(f"Table {table_number} is not booked yet. Please book a table first.")
        else:
            if table_number in self.customer_orders:
                self.customer_orders[table_number].extend(order_items)
            else:
                self.customer_orders[table_number] = order_items
            print(f"Order for table {table_number} has been placed: {', '.join(order_items)}")

    def print_menu(self):
        print("\nMenu:")
        for item, price in self.menu_items.items():
            print(f"{item}: ${price}")

    def print_table_reservations(self):
        print("\nBooked Tables:")
        if self.booked_tables:
            for table in self.booked_tables:
                print(f"Table {table}")
        else:
            print("No tables booked yet.")

    def print_customer_orders(self):
        print("\nCustomer Orders:")
        if self.customer_orders:
            for table, orders in self.customer_orders.items():
                print(f"Table {table}: {', '.join(orders)}")
        else:
            print("No orders placed yet.")

# Example usage
if __name__ == "__main__":
    restaurant = Restaurant()
    restaurant.add_item_to_menu("Burger", 5.99)
    restaurant.add_item_to_menu("Pizza", 8.99)
    restaurant.add_item_to_menu("Pasta", 7.50)
    restaurant.book_table(1)
    restaurant.book_table(2)
    restaurant.customer_order(1, ["Burger", "Pasta"])
    restaurant.customer_order(2, ["Pizza"])
    restaurant.print_menu()
    restaurant.print_table_reservations()
    restaurant.print_customer_orders()
