from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton


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


class DemoApp(MDApp):
    
    def build(self):
        screen = Screen()
        btn_flat = MDRectangleFlatButton(text="Hello World",
                                pos_hint={"center_x": .5, "center_y": .5})
        screen.add_widget(btn_flat)
        return screen

DemoApp().run()