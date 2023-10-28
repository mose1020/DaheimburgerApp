from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton, MDIconButton, MDFloatingActionButton


# class DemoApp(MDApp):
    
#     def build(self):

#         label = MDLabel(text="Hello from Kivy",
#                         halign="center",
#                         theme_text_color="Error",
#                         text_color=(0, 0, 1, 1),
#                         font_style="H2")

#         icon_label = MDIcon(icon="language-python",
#                             halign="center")
#                             #heme_text_color="Custom",
#                             #text_color=(1, 0, 1, 1))
#         return icon_label


# DemoApp().run()


# class DemoApp(MDApp):
    
#     def build(self):
#         screen = Screen()
#         btn_flat = MDRectangleFlatButton(text="Hello World",
#                                 pos_hint={"center_x": .5, "center_y": .5})
#         icon_bnt = MDFloatingActionButton(icon="language-python",
#                                 pos_hint={"center_x": .5, "center_y": .5})
#         #screen.add_widget(btn_flat)
#         screen.add_widget(icon_bnt)
#         return screen

# DemoApp().run()

# class DemoApp(MDApp):
    
#     def build(self):
#         self.theme_cls.primary_palette = "Green"
#         self.theme_cls.primary_hue = "A700"
#         self.theme_cls.theme_style = "Dark"
#         screen = Screen()
#         btn_flat = MDRectangleFlatButton(text="Hello World",
#                                         pos_hint={"center_x": .5, "center_y": .5})
#         screen.add_widget(btn_flat)
#         return screen
    
# DemoApp().run()


from kivymd.app import MDApp
from kivymd.uix.screen import Screen

# class DemoApp(MDApp):
    
#     def build(self):
#         screen = Screen()
#         return screen
    
# DemoApp().run()

from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton, MDIconButton, MDFloatingActionButton
from kivymd.uix.dialog import MDDialog
from kivy.lang import Builder
from helpers import username_helper


# class DemoApp(MDApp):
    
#     def build(self):
#         self.theme_cls.primary_palette = "Green"
#         screen = Screen()
#         button = MDRectangleFlatButton(text="Show",
#                                         pos_hint={"center_x": .5, "center_y": .4},
#                                         on_release=self.show_data)
#         self.username = Builder.load_string(username_helper)  
#         screen.add_widget(self.username)
#         screen.add_widget(button)
#         return screen
    
#     def show_data(self, obj):
#         if self.username.text is "":
#             check_string = "Please enter a username"
#         else:
#             check_string = self.username.text + " does not exist"

#         self.close_button = MDFlatButton(text="Close", on_release=self.close_dialog)
#         self.more_button = MDFlatButton(text="More")
#         self.dialog = MDDialog(title="Username Check", 
#                           text=check_string,
#                           size_hint=(0.7,1),
#                           buttons=[self.close_button, self.more_button])
#         self.dialog.open()

#     def close_dialog(self, obj):
#         self.dialog.dismiss()

# DemoApp().run()



# from kivymd.app import MDApp
# from kivymd.uix.label import MDLabel, MDIcon
# from kivymd.uix.screen import Screen
# from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton, MDIconButton, MDFloatingActionButton
# from kivymd.uix.dialog import MDDialog
# from kivy.lang import Builder
# from helpers import username_helper
# from kivymd.uix.list import ThreeLineListItem, MDList,ThreeLineIconListItem,IconLeftWidget,ThreeLineAvatarListItem
# from kivy.uix.scrollview import ScrollView
# from kivymd.uix.list import IconLeftWidget, ImageLeftWidget

# class DemoApp(MDApp):
    
#     def build(self):
#         screen = Screen()

#         scroll = ScrollView()
#         list = MDList()
#         scroll.add_widget(list)

#         for i in range(20):
#             icon = IconLeftWidget(icon="language-python")
#             image = ImageLeftWidget(source="logo_daheimburger.png")
#             items = ThreeLineAvatarListItem(text="Item " + str(i+1), 
#                                       secondary_text="Hello World", 
#                                       tertiary_text="Third Text")
#             items.add_widget(image)
#             list.add_widget(items)


#         screen.add_widget(scroll)

#         return screen
    
# DemoApp().run()

# from kivymd.app import MDApp
# from kivy.lang import Builder
# from kivymd.uix.list import OneLineListItem


# list_helper = """

# Screen:
#     ScrollView:
#         MDList:
#             id: container
            
# """



# class DemoApp(MDApp):
    
#     def build(self):
#         screen = Builder.load_string(list_helper)

#         return screen

#     def on_start(self):
#         for i in range(20):
#             item = OneLineListItem(text="Item " + str(i+1))
#             self.root.ids.container.add_widget(item)

# DemoApp().run()




# from kivymd.app import MDApp
# from kivymd.uix.screen import Screen
# from kivymd.uix.datatables import MDDataTable
# from kivy.metrics import dp

# class DemoApp(MDApp):
    
#     def build(self):
#         screen = Screen()
#         table = MDDataTable(
#             column_data=
#             [("No.", dp(30)),
#             ("Food", dp(30)),
#             ("Calories", dp(30))],
#             row_data=[("1", "Burger", "300"),
#                       ])
              
#         screen.add_widget(table)
#         return screen
    
# DemoApp().run()



# from kivymd.app import MDApp
# from kivy.lang import Builder
# from kivy.core.window import Window

# Window.size = (300,500)


# screen_helper = """

# Screen:
#     BoxLayout:
#         orientation: 'vertical'
#         MDTopAppBar:
#             title: 'Demo'
#             left_action_items: [["menu", lambda x: app.navigation_draw()]]
#             right_action_items: [["clock", lambda x: app.navigation_draw()]]
#             elevation: 3
#         MDLabel:
#             text: 'Hello World'
#             halign: 'center'
# """

# class DemoApp(MDApp):
    
#     def build(self):
#         self.theme_cls.primary_palette = "Green"
#         screen = Builder.load_string(screen_helper)
#         return screen
    
#     def navigation_draw(self):
#         print("Navigation")
    
# DemoApp().run()


from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

screen_helper = """

ScreenManager:
    MenuScreen:
    ProfileScreen:

<MenuScreen>:
    name: 'menu'
    MDRectangleFlatButton:
        text: 'Profile'
        pos_hint: {'center_x':0.5,'center_y':0.5}
        on_press: root.manager.current = 'profile'

<ProfileScreen>:
    name: 'profile'
    MDLabel:
        text: 'Welcome'
        halign: 'center'
    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x':0.5,'center_y':0.4}
        on_press: root.manager.current = 'menu'
"""




class MenuScreen(Screen):
    pass

class ProfileScreen(Screen):
    pass

sm  = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(ProfileScreen(name='profile'))


class DemoApp(MDApp):

    def build(self):
        screen = Builder.load_string(screen_helper)
        return screen
    

DemoApp().run()