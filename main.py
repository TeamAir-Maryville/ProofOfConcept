'''
Created on Nov 27, 2022
Last Updated on Dec 4, 2022
 
@author: Alison Glore

READ ME
Kivy Framework

'''

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

Builder.load_string("""
<MenuScreen>:
    canvas.before:
        Color: 
            rgba: (1, 222/255, 167/255, 1) 
        Rectangle: 
            pos: self.pos
            size: self.size

    BoxLayout:
        orientation: 'vertical'
        Label: 
            text: 'WATCHER'
            font_size: '60sp'
            size_hint: 1,1
            color: (0, 0, 0, 1)
        BoxLayout: 
            orientation: 'horizontal'
            Button:
                text: 'Add Show'
                font_size: '40sp'
                size_hint: .5, 1
                pos_hint: { 'left': .5}
                background_normal: ''
                background_color: (1, 199/255, 146/255, 1)
                color: (0, 0, 0, 1)
                on_press: root.manager.current = 'Add Show'
            Button: 
                text: 'Add Movie'
                font_size: '40sp'
                size_hint: .5, 1
                pos_hint: { 'right': .5}
                background_normal: ''
                background_color: (1, 199/255, 146/255, 1)
                color: (0, 0, 0, 1)
                on_press: root.manager.current = 'Add Movie'
        Button:
            text: 'Watch Now'
            font_size: '40sp'
            size_hint: .75, 1
            pos_hint: { 'center_x': .5}
            background_normal: ''
            background_color: (252/255, 149/255, 45/255, 1)
            color: (0, 0, 0, 1)
            on_press: root.manager.current = 'Watch Now'

<AddShowScreen>:
    canvas.before:
        Color: 
            rgba: (1, 222/255, 167/255, 1) 
        Rectangle: 
            pos: self.pos
            size: self.size

    BoxLayout:
        orientation: 'vertical'
        Button:
            text: 'Back to Menu'
            font_size: '40sp'
            size_hint: .5, 1
            pos_hint: { 'left': .5}
            background_normal: ''
            background_color: (252/255, 149/255, 45/255, 1)
            color: (0, 0, 0, 1)
            on_press: root.manager.current = 'Menu'
        Label:
            text: 'SHOWS'
            font_size: '60sp'
            size_hint: 1,1
            color: (0, 0, 0, 1)
        BoxLayout: 
            orientation: 'vertical'
            BoxLayout: 
                orientaion: 'horizontal'
                Button:
                    text: 'Insert Title'
                    font_size: '40sp'
                    size_hint: .5, 1
                    pos_hint: { 'center_x': .5}
                    background_normal: ''
                    background_color: (1, 199/255, 146/255, 1)
                    color: (0, 0, 0, 1)
                Button:
                    text: 'Insert Watch Time'
                    font_size: '40sp'
                    size_hint: .5, 1
                    pos_hint: { 'center_x': .5}
                    background_normal: ''
                    background_color: (1, 199/255, 146/255, 1)
                    color: (0, 0, 0, 1)
        Button:
            text: 'Enter'
            font_size: '40sp'
            size_hint: .75, 1
            pos_hint: { 'center_x': .5}
            background_normal: ''
            background_color: (252/255, 149/255, 45/255, 1)
            color: (0, 0, 0, 1)

<AddMovieScreen>:
    canvas.before:
        Color: 
            rgba: (1, 222/255, 167/255, 1) 
        Rectangle: 
            pos: self.pos
            size: self.size

    BoxLayout:
        orientation: 'vertical'
        Button:
            text: 'Back to Menu'
            font_size: '40sp'
            size_hint: .5, 1
            pos_hint: { 'left': .5}
            background_normal: ''
            background_color: (252/255, 149/255, 45/255, 1)
            color: (0, 0, 0, 1)
            on_press: root.manager.current = 'Menu'
        Label:
            text: 'MOVIES'
            font_size: '60sp'
            size_hint: 1,1
            color: (0, 0, 0, 1)
        BoxLayout: 
            orientation: 'vertical'
            BoxLayout: 
                orientaion: 'horizontal'
                Button:
                    text: 'Insert Title'
                    font_size: '40sp'
                    size_hint: .5, 1
                    pos_hint: { 'center_x': .5}
                    background_normal: ''
                    background_color: (1, 199/255, 146/255, 1)
                    color: (0, 0, 0, 1)
                Button:
                    text: 'Insert Watch Time'
                    font_size: '40sp'
                    size_hint: .5, 1
                    pos_hint: { 'center_x': .5}
                    background_normal: ''
                    background_color: (1, 199/255, 146/255, 1)
                    color: (0, 0, 0, 1)
        Button:
            text: 'Enter'
            font_size: '40sp'
            size_hint: .75, 1
            pos_hint: { 'center_x': .5}
            background_normal: ''
            background_color: (252/255, 149/255, 45/255, 1)
            color: (0, 0, 0, 1)

""")

class MenuScreen(Screen):
    pass

class AddShowScreen(Screen):
    def addShow(self, title, duration):
        with open("shows_list.txt", "a") as showList:
            showList.write(title.text + "," + duration.text + "\n")
        title.text = ''
        duration.text = ''
    pass

class AddMovieScreen(Screen):
    def addMovie(self, title, duration):
        with open("movies_list.txt", "a") as showList:
            showList.write(title.text + "," + duration.text + "\n")
        title.text = ''
        duration.text = ''
    pass

class TestApp(App):

    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='Menu'))
        sm.add_widget(AddShowScreen(name='Add Show'))
        sm.add_widget(AddMovieScreen(name='Add Movie'))

        return sm

if __name__ == '__main__':
    TestApp().run()
