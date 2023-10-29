# from kivymd.app import MDApp
# from kivy.lang import Builder
# from kivy.uix.screenmanager import Screen, ScreenManager
# from kivymd.uix.list import OneLineAvatarIconListItem, IconLeftWidget, IconRightWidget

# KV = """
# ScreenManager:
#     MenuScreen:
#     OrderScreen:

# <MenuScreen>:
#     name: 'menu'
#     BoxLayout:
#         orientation: 'vertical'
#         MDTopAppBar:
#             title: 'My App'
#             md_bg_color: .2, .2, .2, 1
#             specific_text_color: 1, 1, 1, 1
#         ScrollView:
#             MDList:
#                 id: container
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
#         text: 'Back'
#         pos_hint: {'center_x': 0.5, 'center_y': 0.4}
#         on_release: app.switch_to_menu()
# """

# class MenuScreen(Screen):
#     pass

# class OrderScreen(Screen):
#     pass

# class DemoApp(MDApp):

#     def build(self):
#         return Builder.load_string(KV)

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
#             self.root.get_screen('menu').ids.container.add_widget(item)
#             self.root.get_screen('menu').ids.item_textfield.text = ""

#     def remove_item(self, item):
#         self.root.get_screen('menu').ids.container.remove_widget(item)

#     def switch_to_order(self):
#         self.root.current = 'order'

#     def switch_to_menu(self):
#         self.root.current = 'menu'

# DemoApp().run()


from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.list import OneLineAvatarIconListItem, IconLeftWidget, IconRightWidget
import sqlite3

KV = """
ScreenManager:
    MenuScreen:
    OrderScreen:

<MenuScreen>:
    name: 'menu'
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: 'My App'
            md_bg_color: .2, .2, .2, 1
            specific_text_color: 1, 1, 1, 1
        ScrollView:
            MDList:
                id: container
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
        text: 'Back'
        pos_hint: {'center_x': 0.5, 'center_y': 0.4}
        on_release: app.switch_to_menu()
"""

class MenuScreen(Screen):
    pass

class OrderScreen(Screen):
    pass

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
            self.root.get_screen('menu').ids.container.add_widget(item)

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
            self.root.get_screen('menu').ids.container.add_widget(item)
            self.root.get_screen('menu').ids.item_textfield.text = ""
            self.cur.execute("INSERT INTO items VALUES (?)", (item_name,))
            self.conn.commit()
        
        if item_name == "reset_database":
            self.cur.execute("DROP TABLE items")
            self.cur.execute('''CREATE TABLE IF NOT EXISTS items
                            (name TEXT)''')
            self.conn.commit()
            self.root.get_screen('menu').ids.container.clear_widgets()
            self.root.get_screen('menu').ids.item_textfield.text = ""

    def remove_item(self, item):
        self.root.get_screen('menu').ids.container.remove_widget(item)
        item_name = item.text
        try:
            self.cur.execute("DELETE FROM items WHERE name=?", (item_name,))
            self.conn.commit()
        except sqlite3.Error as e:
            # Handle the error, e.g., log it or print it for debugging
            print("Error deleting item:", e)

    def switch_to_order(self):
        self.root.current = 'order'

    def switch_to_menu(self):
        self.root.current = 'menu'



DemoApp().run()







