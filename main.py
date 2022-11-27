from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

class MainApp(App):
    def build(self):
        layout= BoxLayout(orientation='vertical')

        label = Label(text='WATCHER', font_size='40sp')

        bttn3 = Button(text='Watch Now',
                        size_hint=(.3, .3),
                        pos_hint={'center_x': .5, 'center_y': .5})
        bttn3.bind(on_press=self.on_press_button)

        layout2 = BoxLayout(orientation='horizontal')

        bttn1 = Button(text='Add Show',
                        size_hint=(.3, .3),
                        pos_hint={'left': 1})
        bttn1.bind(on_press=self.on_press_button)

        bttn2 = Button(text='Add Movie',
                        size_hint=(.3, .3),
                        pos_hint={'right': 1})
        bttn2.bind(on_press=self.on_press_button)

        layout.add_widget(label)
        layout.add_widget(layout2)
        layout2.add_widget(bttn1)
        layout2.add_widget(bttn2)
        layout.add_widget(bttn3)

        return layout

    def on_press_button(self, instance):
        print('You pressed the button!')

if __name__ == '__main__':
    app = MainApp()
    app.run()