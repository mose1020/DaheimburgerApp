# from kivy.app import App
# from kivy.uix.label import Label
# from kivy.uix.button import Button
# from kivy.core.window import Window


#Window.clearcolor = ( 1, 0, 0, 1)


# class MainApp(App):

#     def build(self):
#         label = Label(text="Hello from Kivy",
#                         size_hint=(.5, .5),
#                         pos_hint={"center_x": .5, "center_y": .5})
        
#         return label

# MainApp().run()

# class MainApp(App):

#     def build(self):
#         button = Button(text="Hello from Kivy",
#                         size_hint=(.5, .5),
#                         pos_hint={"center_x": .5, "center_y": .5},
#                         on_press=self.print_press,
#                         on_release=self.print_release)
        
#         return button
    
#     def print_press(self, obj):
#         print("Button pressed")
    
#     def print_release(self, obj):
#         print("Button released")
    

# MainApp().run()


# from kivy.uix.image import Image, AsyncImage


# class MainApp(App):

#     def build(self):
#         img = Image(source="logo_daheimburger.png",
#                     size_hint=(1, .5),
#                     pos_hint={"center_x": .5, "center_y": .5})
        
#         return img
    
# MainApp().run()

# from kivy.app import App
# from kivy.uix.button import Button
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.image import Image

# from kivy.core.window import Window

# Window.clearcolor = ( 1, 1, 1, 1)
# Window.size = (360, 600)

# class MainApp(App):

#     def build(self):
#         layout = BoxLayout(orientation="vertical",spacing=100,padding=80)
#         img = Image(source="logo_daheimburger.png")
#         button = Button(text='Login',
#                         size_hint=(None, None),width=100,height=50,
#                         pos_hint={"center_x": .5, "center_y": .5})
#         layout.add_widget(img)
#         layout.add_widget(button)
#         return layout



# MainApp().run()

# from kivy.app import App
# from kivy.uix.button import Button
# from kivy.uix.gridlayout import GridLayout

# class MainApp(App):

#     def build(self):
#         layout = GridLayout(cols=2,row_force_default=True, row_default_height=40)
#         layout.add_widget(Button(text='Hello 1',size_hint=(None, None),width=100,height=40))
#         layout.add_widget(Button(text='World 1'))
#         layout.add_widget(Button(text='Hello 2',size_hint=(None, None),width=100,height=40))
#         layout.add_widget(Button(text='World 2'))
#         layout.add_widget(Button(text='Hello 3',size_hint=(None, None),width=100,height=40))
#         layout.add_widget(Button(text='World 3'))
#         return layout

# MainApp().run()


# from kivy.app import App
# from kivy.uix.textinput import TextInput
# from kivy.uix.button import Button
# from kivy.uix.gridlayout import GridLayout



# class MainApp(App):

#     def build(self):
#         layout = GridLayout(cols=2,row_force_default=True, row_default_height=40)
#         self.weight = TextInput(text="Enter your weight in KG")
#         self.height = TextInput(text="Enter your height in CM")
#         submit = Button(text="Submit",on_press=self.submit)
#         layout.add_widget(self.weight)
#         layout.add_widget(self.height)
#         layout.add_widget(submit)

#         return layout
    
#     def submit(self, obj):

#         print("Weight: ", self.weight.text)
#         print("Height: ", self.height.text)

        


# MainApp().run()


