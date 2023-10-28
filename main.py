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



from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton, MDIconButton, MDFloatingActionButton
from kivymd.uix.dialog import MDDialog
from kivy.lang import Builder
from helpers import username_helper
from kivymd.uix.list import OneLineListItem, MDList
from kivy.uix.scrollview import ScrollView

class DemoApp(MDApp):
    
    def build(self):
        screen = Screen()

        scroll = ScrollView()
        list = MDList()
        scroll.add_widget(list)

        item1 = OneLineListItem(text="Item 1")
        item2 = OneLineListItem(text="Item 2")

        list.add_widget(item1)
        list.add_widget(item2)

        screen.add_widget(scroll)

        return screen
    
DemoApp().run()