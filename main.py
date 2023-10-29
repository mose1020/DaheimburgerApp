
# from kivymd.app import MDApp
# from kivy.lang import Builder
# from kivy.uix.screenmanager import Screen, ScreenManager
# from kivymd.uix.list import OneLineAvatarIconListItem, IconLeftWidget, IconRightWidget
# import sqlite3
# import csv
# from food_list import food_list

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
#             icon_left = IconLeftWidget(icon="minus")
#             icon_right = IconRightWidget(icon="plus")
#             print(food_list[i][0])
#             item = OneLineAvatarIconListItem(text=str(food_list[i][0]))
#             item.add_widget(icon_left)
#             item.add_widget(icon_right)
#             self.root.get_screen('orderlist').ids.container.add_widget(item)


#     def switch_to_order(self):
#         self.root.current = 'order'

#     def switch_to_menu(self):
#         self.root.current = 'menu'
    
#     def switch_to_order_list(self):
#         self.root.current = 'orderlist'
#         self.create_order_list()




# DemoApp().run()







from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.list import OneLineAvatarIconListItem, IconLeftWidget, IconRightWidget
import sqlite3
import csv


KV = """
ScreenManager:
    MenuScreen:
    OrderScreen:
    OrderlistScreen:

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

<OrderlistScreen>:
    name: 'orderlist'
    BoxLayout:
        orientation: 'vertical'
        ScrollView:
            MDList:
                id: container

"""

class MenuScreen(Screen):
    pass

class OrderScreen(Screen):
    pass

class OrderlistScreen(Screen):
    pass

class CounterItem(OneLineAvatarIconListItem):
    def __init__(self, item_name, counter, **kwargs):
        super(CounterItem, self).__init__(**kwargs)
        self.item_name = item_name
        self.counter = counter
        self.text = f"{self.item_name} ({self.counter})"

class DemoApp(MDApp):

    def build(self):
        return Builder.load_string(KV)

    def on_start(self):
        self.conn = sqlite3.connect('items.db')
        self.cur = self.conn.cursor()
        self.cur.execute('''CREATE TABLE IF NOT EXISTS items
                            (name TEXT)''')
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
            icon_right.bind(on_release=lambda x: self.switch_to_order())
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
            icon_right.bind(on_release=lambda x: self.switch_to_order())
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

        # import csv file as lists
        with open('food.csv', newline='') as csvfile:
            food_list = list(csv.reader(csvfile))

        for i in range(len(food_list)):
            item_name = food_list[i][0]
            
            # Create a custom item widget that includes the counter
            item_widget = CounterItem(item_name=item_name, counter=0)
            
            icon_left = IconLeftWidget(icon="minus")
            icon_right = IconRightWidget(icon="plus")
            item_widget.add_widget(icon_left)
            item_widget.add_widget(icon_right)

            # Bind the plus and minus buttons to update the counter
            icon_left.bind(on_release=lambda x, item_widget=item_widget: self.update_counter(item_widget, -1))
            icon_right.bind(on_release=lambda x, item_widget=item_widget: self.update_counter(item_widget, 1))
            
            self.root.get_screen('orderlist').ids.container.add_widget(item_widget)

    def update_counter(self, item_widget, delta):
        item_widget.counter += delta  # Update the counter
        item_widget.text = f"{item_widget.item_name} ({item_widget.counter})"


    def switch_to_order(self):
        self.root.current = 'order'

    def switch_to_menu(self):
        self.root.current = 'menu'
    
    def switch_to_order_list(self):
        self.root.current = 'orderlist'
        self.create_order_list()




DemoApp().run()




































