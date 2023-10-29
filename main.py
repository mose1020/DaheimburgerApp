

# from kivymd.app import MDApp
# from kivy.lang import Builder
# from kivymd.uix.button import MDRectangleFlatButton
# from kivy.uix.screenmanager import Screen, ScreenManager
# from kivymd.uix.list import OneLineAvatarIconListItem, IconLeftWidget, IconRightWidget
# import sqlite3
# import csv


# KV = """
# ScreenManager:
#     MenuScreen:
#     OrderScreen:
#     OrderlistScreen:

# <MenuScreen>:
#     name: 'menu'
#     BoxLayout:
#         orientation: 'vertical'
#         MDTopAppBar:
#             title: 'Hauptmenü'
#             md_bg_color: .2, .2, .2, 1
#             specific_text_color: 1, 1, 1, 1
#         ScrollView:
#             MDList:
#                 id: table_name
#         MDTextField:
#             id: item_textfield
#             hint_text: "Enter item name"
#             size_hint_y: None
#             height: "48dp"
#             mode: "rectangle"
#         MDRectangleFlatButton:
#             text: "Add Item"
#             pos_hint: {'center_x': 0.5, 'center_y': 0.5}
#             on_release: app.add_item()

# <OrderScreen>:
#     name: 'order'
#     MDRectangleFlatButton:
#         text: 'Back to menu'
#         pos_hint: {'center_x': 0.5, 'center_y': 0.4}
#         on_release: app.switch_to_menu()
    
#     MDRectangleFlatButton:
#         text: 'Take Order'
#         pos_hint: {'center_x': 0.5, 'center_y': 0.3}
#         on_release: app.switch_to_order_list()

# <OrderlistScreen>:
#     name: 'orderlist'
#     BoxLayout:
#         orientation: 'vertical'
#         ScrollView:
#             MDList:
#                 id: container

# """

# class MenuScreen(Screen):
#     pass

# class OrderScreen(Screen):
#     pass

# class OrderlistScreen(Screen):
#     pass

# class CounterItem(OneLineAvatarIconListItem):
#     def __init__(self, item_name, counter, **kwargs):
#         super(CounterItem, self).__init__(**kwargs)
#         self.item_name = item_name
#         self.counter = counter
#         self.text = f"{self.item_name} ({self.counter})"

# class DemoApp(MDApp):

#     def build(self):
#         return Builder.load_string(KV)

#     def on_start(self):
#         self.conn = sqlite3.connect('items.db')
#         self.cur = self.conn.cursor()
#         self.cur.execute('''CREATE TABLE IF NOT EXISTS items
#                             (name TEXT)''')
#         self.conn.commit()
#         self.cur.execute("SELECT * FROM items")
#         items = self.cur.fetchall()
#         for item in items:
#             item_name = item[0]
#             icon_left = IconLeftWidget(icon="delete")
#             icon_right = IconRightWidget(icon="import")
#             item = OneLineAvatarIconListItem(text=item_name)
#             item.add_widget(icon_left)
#             item.add_widget(icon_right)
#             icon_left.bind(on_release=lambda x: self.remove_item(item))
#             icon_right.bind(on_release=lambda x: self.switch_to_order())
#             self.root.get_screen('menu').ids.table_name.add_widget(item)

#     def add_item(self):
#         item_name = self.root.get_screen('menu').ids.item_textfield.text.strip()

#         if item_name:
#             icon_left = IconLeftWidget(icon="delete")
#             icon_right = IconRightWidget(icon="import")
#             item = OneLineAvatarIconListItem(text=item_name)
#             item.add_widget(icon_left)
#             item.add_widget(icon_right)
#             icon_left.bind(on_release=lambda x: self.remove_item(item))
#             icon_right.bind(on_release=lambda x: self.switch_to_order())
#             self.root.get_screen('menu').ids.table_name.add_widget(item)
#             self.root.get_screen('menu').ids.item_textfield.text = ""
#             self.cur.execute("INSERT INTO items VALUES (?)", (item_name,))
#             self.conn.commit()
        
#         if item_name == "reset_database":
#             self.cur.execute("DROP TABLE items")
#             self.cur.execute('''CREATE TABLE IF NOT EXISTS items
#                             (name TEXT)''')
#             self.conn.commit()
#             self.root.get_screen('menu').ids.table_name.clear_widgets()
#             self.root.get_screen('menu').ids.item_textfield.text = ""

#     def remove_item(self, item):
#         self.root.get_screen('menu').ids.table_name.remove_widget(item)
#         item_name = item.text
#         try:
#             self.cur.execute("DELETE FROM items WHERE name=?", (item_name,))
#             self.conn.commit()
#         except sqlite3.Error as e:
#             # Handle the error, e.g., log it or print it for debugging
#             print("Error deleting item:", e)
    
#     def create_order_list(self):

#         # import csv file as lists
#         with open('food.csv', newline='') as csvfile:
#             food_list = list(csv.reader(csvfile))

#         for i in range(len(food_list)):
#             item_name = food_list[i][0]
            
#             # Create a custom item widget that includes the counter
#             item_widget = CounterItem(item_name=item_name, counter=0)
            
#             icon_left = IconLeftWidget(icon="minus")
#             icon_right = IconRightWidget(icon="plus")
#             item_widget.add_widget(icon_left)
#             item_widget.add_widget(icon_right)

#             # Bind the plus and minus buttons to update the counter
#             icon_left.bind(on_release=lambda x, item_widget=item_widget: self.update_counter(item_widget, -1))
#             icon_right.bind(on_release=lambda x, item_widget=item_widget: self.update_counter(item_widget, 1))
            
#             self.root.get_screen('orderlist').ids.container.add_widget(item_widget)
        
#         self.root.get_screen('orderlist').ids.container.add_widget(MDRectangleFlatButton(text="Confirme order", on_release=lambda x: self.confirm_order()))

#     def update_counter(self, item_widget, delta):
#         item_widget.counter += delta  # Update the counter
#         item_widget.text = f"{item_widget.item_name} ({item_widget.counter})"


#     def switch_to_order(self):
#         self.root.current = 'order'

#     def switch_to_menu(self):
#         self.root.current = 'menu'
    
#     def switch_to_order_list(self):
#         self.root.current = 'orderlist'
#         self.create_order_list()
    
#     def confirm_order(self):
#         print("Order confirmed")




# DemoApp().run()









# from kivymd.app import MDApp
# from kivy.lang import Builder
# from kivymd.uix.button import MDRectangleFlatButton
# from kivy.uix.screenmanager import Screen, ScreenManager
# from kivymd.uix.list import OneLineAvatarIconListItem, IconLeftWidget, IconRightWidget
# import sqlite3
# import csv


# KV = """
# ScreenManager:
#     MenuScreen:
#     OrderScreen:
#     OrderlistScreen:
#     ShowOrdersScreen:

# <MenuScreen>:
#     name: 'menu'
#     BoxLayout:
#         orientation: 'vertical'
#         MDTopAppBar:
#             title: 'Hauptmenü'
#             md_bg_color: .2, .2, .2, 1
#             specific_text_color: 1, 1, 1, 1
#         ScrollView:
#             MDList:
#                 id: table_name
#         MDTextField:
#             id: item_textfield
#             hint_text: "Enter item name"
#             size_hint_y: None
#             height: "48dp"
#             mode: "rectangle"
#         MDRectangleFlatButton:
#             text: "Add Item"
#             pos_hint: {'center_x': 0.5, 'center_y': 0.5}
#             on_release: app.add_item()

# <OrderScreen>:
#     name: 'order'
#     MDRectangleFlatButton:
#         text: 'Back to menu'
#         pos_hint: {'center_x': 0.5, 'center_y': 0.4}
#         on_release: app.switch_to_menu()
    
#     MDRectangleFlatButton:
#         text: 'Take Order'
#         pos_hint: {'center_x': 0.5, 'center_y': 0.3}
#         on_release: app.switch_to_order_list()
    
#     MDRectangleFlatButton:
#         text: 'Look at order'
#         pos_hint: {'center_x': 0.5, 'center_y': 0.2}
#         on_release: app.show_orders()

# <OrderlistScreen>:
#     name: 'orderlist'
#     BoxLayout:
#         orientation: 'vertical'
#         ScrollView:
#             MDList:
#                 id: container

# <ShowOrdersScreen>:
#     name: 'showorders'
#     BoxLayout:
#         orientation: 'vertical'
#         ScrollView:
#             MDList:
#                 id: container2

# """

# class MenuScreen(Screen):
#     pass

# class OrderScreen(Screen):
#     pass

# class OrderlistScreen(Screen):
#     pass

# class ShowOrdersScreen(Screen):
#     pass

# class CounterItem(OneLineAvatarIconListItem):
#     def __init__(self, item_name, counter, custom_item_id, **kwargs):
#         #super(CounterItem, self).__init__(**kwargs)
#         super().__init__(**kwargs)
#         self.item_name = item_name
#         self.counter = counter
#         self.custom_item_id = custom_item_id
#         self.text = f"{self.item_name} ({self.counter})"


# class DemoApp(MDApp):

#     def build(self):
#         return Builder.load_string(KV)

#     def on_start(self):
#         self.conn = sqlite3.connect('items.db')
#         self.cur = self.conn.cursor()
#         self.cur.execute('''CREATE TABLE IF NOT EXISTS items
#                             (name TEXT)''')
#         self.cur.execute('''CREATE TABLE IF NOT EXISTS orders
#                         (item_id TEXT, quantity INTEGER)''')  # Create the "orders" tabl
#         self.conn.commit()
#         self.cur.execute("SELECT * FROM items")
#         items = self.cur.fetchall()
#         for item in items:
#             item_name = item[0]
#             icon_left = IconLeftWidget(icon="delete")
#             icon_right = IconRightWidget(icon="import")
#             item = OneLineAvatarIconListItem(text=item_name)
#             item.add_widget(icon_left)
#             item.add_widget(icon_right)
#             icon_left.bind(on_release=lambda x: self.remove_item(item))
#             icon_right.bind(on_release=lambda x: self.switch_to_order())
#             self.root.get_screen('menu').ids.table_name.add_widget(item)

#     def add_item(self):
#         item_name = self.root.get_screen('menu').ids.item_textfield.text.strip()

#         if item_name:
#             icon_left = IconLeftWidget(icon="delete")
#             icon_right = IconRightWidget(icon="import")
#             item = OneLineAvatarIconListItem(text=item_name)
#             item.add_widget(icon_left)
#             item.add_widget(icon_right)
#             icon_left.bind(on_release=lambda x: self.remove_item(item))
#             icon_right.bind(on_release=lambda x: self.switch_to_order())
#             self.root.get_screen('menu').ids.table_name.add_widget(item)
#             self.root.get_screen('menu').ids.item_textfield.text = ""
#             self.cur.execute("INSERT INTO items VALUES (?)", (item_name,))
#             self.conn.commit()
        
#         if item_name == "reset_database":
#             self.cur.execute("DROP TABLE items")
#             self.cur.execute('''CREATE TABLE IF NOT EXISTS items
#                             (name TEXT)''')
#             self.conn.commit()
#             self.root.get_screen('menu').ids.table_name.clear_widgets()
#             self.root.get_screen('menu').ids.item_textfield.text = ""

#     def remove_item(self, item):
#         self.root.get_screen('menu').ids.table_name.remove_widget(item)
#         item_name = item.text
#         try:
#             self.cur.execute("DELETE FROM items WHERE name=?", (item_name,))
#             self.conn.commit()
#         except sqlite3.Error as e:
#             # Handle the error, e.g., log it or print it for debugging
#             print("Error deleting item:", e)
    
#     def create_order_list(self):
#         # Clear the orderlist screen before creating a new order list
#         self.root.get_screen('orderlist').ids.container.clear_widgets()

#         # Import CSV file as lists
#         with open('food.csv', newline='') as csvfile:
#             food_list = list(csv.reader(csvfile))

#         for item_info in food_list:
#             item_name = item_info[0]
#             item_id = item_info[1]  # Assuming the second column in the CSV contains item IDs

#             # Create a custom item widget that includes the counter
#             item_widget = CounterItem(item_name=item_name, counter=0, custom_item_id=item_id)
#             icon_left = IconLeftWidget(icon="minus")
#             icon_right = IconRightWidget(icon="plus")
#             item_widget.add_widget(icon_left)
#             item_widget.add_widget(icon_right)

#             # Bind the plus and minus buttons to update the counter
#             icon_left.bind(on_release=lambda x, item_widget=item_widget: self.update_counter(item_widget, -1))
#             icon_right.bind(on_release=lambda x, item_widget=item_widget: self.update_counter(item_widget, 1))

#             self.root.get_screen('orderlist').ids.container.add_widget(item_widget)

#         self.root.get_screen('orderlist').ids.container.add_widget(MDRectangleFlatButton(text="Confirm order", on_release=lambda x: self.confirm_order()))

#     def update_counter(self, item_widget, delta):
#         item_widget.counter += delta  # Update the counter
#         item_widget.text = f"{item_widget.item_name} ({item_widget.counter})"

#     def confirm_order(self):
#         # Iterate through the items in the order list and save them to the orders table
#         for item_widget in self.root.get_screen('orderlist').ids.container.children:
#             if isinstance(item_widget, CounterItem):
#                 item_id = item_widget.custom_item_id
#                 quantity = item_widget.counter
#                 self.cur.execute("INSERT INTO orders (item_id, quantity) VALUES (?, ?)", (item_id, quantity))
#                 self.conn.commit()

#         self.root.current = 'order'
    
#     def show_orders(self):
#         # Clear the orderlist screen before creating a new order list
#         self.root.get_screen('showorders').ids.container2.clear_widgets()

#         # Import CSV file as lists
#         with open('food.csv', newline='') as csvfile:
#             food_list = list(csv.reader(csvfile))

#         # Get the orders from the database
#         self.cur.execute("SELECT * FROM orders")
#         orders = self.cur.fetchall()

#         # Create a dictionary of the orders
#         orders_dict = {}
#         for order in orders:
#             item_id = order[0]
#             quantity = order[1]
#             orders_dict[item_id] = quantity

#         # Iterate through the items in the order list and save them to the orders table
#         for item_info in food_list:
#             item_name = item_info[0]
#             item_id = item_info[1]

#             # Create a custom item widget that displays the item name and quantity
#             quantity = orders_dict.get(item_id, 0)
#             item_widget = CounterItem(item_name=f"{item_name} ({quantity})", counter=quantity, custom_item_id=item_id)
#             self.root.get_screen('showorders').ids.container2.add_widget(item_widget)

#         self.root.current = 'showorders'


#     def switch_to_order(self):
#         self.root.current = 'order'

#     def switch_to_menu(self):
#         self.root.current = 'menu'
    
#     def switch_to_order_list(self):
#         self.root.current = 'orderlist'
#         self.create_order_list()
    




#DemoApp().run()


from kivymd.app import MDApp
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.label import MDLabel
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.list import OneLineAvatarIconListItem, IconLeftWidget, IconRightWidget
import sqlite3
import csv
import os


KV = """
ScreenManager:
    MenuScreen:
    OrderScreen:
    OrderlistScreen:
    ShowOrdersScreen:

<MenuScreen>:
    name: 'menu'
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: 'Hauptmenü'
            md_bg_color: .2, .2, .2, 1
            specific_text_color: 1, 1, 1, 1
        ScrollView:
            MDList:
                id: table_name
        MDTextField:
            id: item_textfield
            hint_text: "Enter item name"
            size_hint_y: None
            height: "48dp"
            mode: "rectangle"
        MDRectangleFlatButton:
            text: "Add Item"
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            on_release: app.add_item()

<OrderScreen>:
    name: 'order'
    MDRectangleFlatButton:
        text: 'Back to menu'
        pos_hint: {'center_x': 0.5, 'center_y': 0.4}
        on_release: app.switch_to_menu()
    
    MDRectangleFlatButton:
        text: 'Take Order'
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        on_release: app.switch_to_order_list()
    
    MDRectangleFlatButton:
        text: 'Look at order'
        pos_hint: {'center_x': 0.5, 'center_y': 0.2}
        on_release: app.show_orders()

<OrderlistScreen>:
    name: 'orderlist'
    BoxLayout:
        orientation: 'vertical'
        ScrollView:
            MDList:
                id: container

<ShowOrdersScreen>:
    name: 'showorders'
    BoxLayout:
        orientation: 'vertical'
        ScrollView:
            MDList:
                id: container2

"""

class MenuScreen(Screen):
    pass

class OrderScreen(Screen):
    pass

class OrderlistScreen(Screen):
    pass

class ShowOrdersScreen(Screen):
    pass

class CounterItem(OneLineAvatarIconListItem):
    def __init__(self, item_name, counter, custom_item_id, **kwargs):
        #super(CounterItem, self).__init__(**kwargs)
        super().__init__(**kwargs)
        self.item_name = item_name
        self.counter = counter
        self.custom_item_id = custom_item_id
        self.text = f"{self.item_name} ({self.counter})"


class DemoApp(MDApp):

    def build(self):
        return Builder.load_string(KV)

    def on_start(self):
        self.conn = sqlite3.connect('items.db')
        self.cur = self.conn.cursor()
        self.cur.execute('''CREATE TABLE IF NOT EXISTS items
                            (name TEXT)''')
        self.cur.execute('''CREATE TABLE IF NOT EXISTS orders
                        (item_id TEXT, quantity INTEGER)''')  # Create the "orders" tabl
        self.conn.commit()
        self.cur.execute("SELECT * FROM items")
        items = self.cur.fetchall()
        for item in items:
            item_name = item[0]
            icon_left = IconLeftWidget(icon="delete")
            icon_right = IconRightWidget(icon="import")
            item = OneLineAvatarIconListItem(text=item_name)
            item.add_widget(icon_left)
            item.add_widget(icon_right)
            icon_left.bind(on_release=lambda x: self.remove_item(item))
            icon_right.bind(on_release=lambda x: self.switch_to_order(item_name))
            self.root.get_screen('menu').ids.table_name.add_widget(item)

    def add_item(self):
        item_name = self.root.get_screen('menu').ids.item_textfield.text.strip()

        if item_name:
            icon_left = IconLeftWidget(icon="delete")
            icon_right = IconRightWidget(icon="import")
            item = OneLineAvatarIconListItem(text=item_name)
            item.add_widget(icon_left)
            item.add_widget(icon_right)
            icon_left.bind(on_release=lambda x: self.remove_item(item))
            icon_right.bind(on_release=lambda x, item_name=item_name: self.switch_to_order(item_name))
            self.root.get_screen('menu').ids.table_name.add_widget(item)
            self.root.get_screen('menu').ids.item_textfield.text = ""
            self.cur.execute("INSERT INTO items VALUES (?)", (item_name,))
            self.conn.commit()
        
        if item_name == "reset_database":
                self.cur.execute("DROP TABLE items")
                self.cur.execute('''CREATE TABLE IF NOT EXISTS items
                                (name TEXT)''')
                self.conn.commit()
                self.root.get_screen('menu').ids.table_name.clear_widgets()
                self.root.get_screen('menu').ids.item_textfield.text = ""
                os.remove("items.db")

    def remove_item(self, item):
        self.root.get_screen('menu').ids.table_name.remove_widget(item)
        item_name = item.text
        try:
            self.cur.execute("DELETE FROM items WHERE name=?", (item_name,))
            self.conn.commit()
        except sqlite3.Error as e:
            # Handle the error, e.g., log it or print it for debugging
            print("Error deleting item:", e)
    
    def create_order_list(self):
        # Clear the orderlist screen before creating a new order list
        self.root.get_screen('orderlist').ids.container.clear_widgets()

        # Import CSV file as lists
        with open('food.csv', newline='') as csvfile:
            food_list = list(csv.reader(csvfile))

        for item_info in food_list:
            item_name = item_info[0]
            item_id = item_info[1]  # Assuming the second column in the CSV contains item IDs

            # Create a custom item widget that includes the counter
            item_widget = CounterItem(item_name=item_name, counter=0, custom_item_id=item_id)
            icon_left = IconLeftWidget(icon="minus")
            icon_right = IconRightWidget(icon="plus")
            item_widget.add_widget(icon_left)
            item_widget.add_widget(icon_right)

            # Bind the plus and minus buttons to update the counter
            icon_left.bind(on_release=lambda x, item_widget=item_widget: self.update_counter(item_widget, -1))
            icon_right.bind(on_release=lambda x, item_widget=item_widget: self.update_counter(item_widget, 1))

            self.root.get_screen('orderlist').ids.container.add_widget(item_widget)

        self.root.get_screen('orderlist').ids.container.add_widget(MDRectangleFlatButton(text="Confirm order", on_release=lambda x: self.confirm_order()))

    def update_counter(self, item_widget, delta):
        item_widget.counter += delta  # Update the counter
        item_widget.text = f"{item_widget.item_name} ({item_widget.counter})"

    def confirm_order(self):
        # Iterate through the items in the order list and save them to the orders table
        for item_widget in self.root.get_screen('orderlist').ids.container.children:
            if isinstance(item_widget, CounterItem):
                item_id = item_widget.custom_item_id
                quantity = item_widget.counter
                self.cur.execute("INSERT INTO orders (item_id, quantity) VALUES (?, ?)", (item_id, quantity))
                self.conn.commit()

        self.root.current = 'order'
    

    def show_orders(self):
        # Clear the orderlist screen before creating a new order list
        self.root.get_screen('showorders').ids.container2.clear_widgets()

        # Retrieve orders from the database
        self.cur.execute("SELECT item_id, quantity FROM orders")
        orders = self.cur.fetchall()

        if orders:
            counter = 0
            for order in orders:
                print(order)
                item_id, quantity = order

                # Retrieve the item name from the database
                self.cur.execute("SELECT name FROM items WHERE ROWID=?", (item_id,))
                item_name_result = self.cur.fetchone()

                if item_name_result:
                    item_name = item_name_result[0]

                    if item_name == self.selected_item:

                        # Create a BoxLayout to organize the order information
                        order_layout = BoxLayout(orientation='vertical', size_hint_y=None, height=dp(48))

                        # Create labels to display the order details
                        counter_label = MDLabel(text=str(counter), halign="center", theme_text_color="Primary")
                        item_label = MDLabel(text=item_name, halign="center", theme_text_color="Primary")
                        quantity_label = MDLabel(text=str(quantity), halign="center", theme_text_color="Primary")

                        # Add labels to the order layout
                        order_layout.add_widget(counter_label)
                        order_layout.add_widget(item_label)
                        order_layout.add_widget(quantity_label)

                        # Add the order layout to the container
                        self.root.get_screen('showorders').ids.container2.add_widget(order_layout)
                        counter += 1
        else:
            # Display a message when there are no orders
            label = MDLabel(text="No orders yet.", halign="center", theme_text_color="Secondary")
            self.root.get_screen('showorders').ids.container2.add_widget(label)

        # Switch to the 'showorders' screen
        self.root.current = 'showorders'


    def switch_to_order(self,item_name):
        self.selected_item = item_name  # Store the selected item name
        self.root.current = 'order'

    def switch_to_menu(self):
        self.root.current = 'menu'
    
    def switch_to_order_list(self):
        self.root.current = 'orderlist'
        self.create_order_list()
    




DemoApp().run()


