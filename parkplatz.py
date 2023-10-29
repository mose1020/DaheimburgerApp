    # def show_orders(self):
    #     # Clear the orderlist screen before creating a new order list
    #     self.root.get_screen('showorders').ids.container2.clear_widgets()

    #     # Import CSV file as lists
    #     with open('food.csv', newline='') as csvfile:
    #         food_list = list(csv.reader(csvfile))

    #     # Get the orders from the database
    #     self.cur.execute("SELECT * FROM orders")
    #     orders = self.cur.fetchall()

    #     # Create a dictionary of the orders
    #     orders_dict = {}
    #     for order in orders:
    #         item_id = order[0]
    #         quantity = order[1]
    #         if item_id in orders_dict:
    #             orders_dict[item_id] += quantity
    #         else:
    #             orders_dict[item_id] = quantity

    #     for item_info in food_list:
    #         item_name = item_info[0]
    #         item_id = item_info[1]

    #         # Create a custom item widget that displays the item name and quantity
    #         quantity = orders_dict.get(item_id, 0)
    #         item_widget = CounterItem(item_name=f"{item_name} ({quantity})", counter=quantity, custom_item_id=item_id)
    #         self.root.get_screen('showorders').ids.container2.add_widget(item_widget)

    #     self.root.current = 'showorders'