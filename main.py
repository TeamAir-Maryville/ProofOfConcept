from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
import random
import os


class HomeScreen(Screen):
    pass


class AddMovieScreen(Screen):
    def addMovie(self, title, duration):
        with open("movies_list.txt", "a") as showLst:
            showLst.write(title.text + "," + duration.text + "\n")
        title.text = ''
        duration.text = ''

    pass


class AddTvScreen(Screen):

    def addShow(self, title, duration):
        with open("shows_list.txt", "a") as showLst:
            showLst.write(title.text + "," + duration.text + "\n")
        title.text = ''
        duration.text = ''

    pass


class GetRecommendationScreen(Screen):
    pass


class GetRecommendationMovieScreen(Screen):
    def movieRecommendation(self, availableTime):
        movies = []
        with open("movies_list.txt", "r") as movieLst:
            lines = movieLst.readlines()
            for line in lines:
                line = line.strip()
                movies.append(line)

        while True:
            index = random.randrange(0, len(movies))
            recommendation = movies[index]
            recommendation = recommendation.split(",")

            if int(recommendation[1]) <= int(availableTime.text):
                recommendationName = recommendation[0]

                layout = GridLayout(cols=1, padding=10)
                popupLabel = Label(text=str(recommendationName))
                closeButton = Button(text="Close the pop-up")
                layout.add_widget(popupLabel)
                layout.add_widget(closeButton)
                popup = Popup(title='Recommendation',
                              content=layout)
                popup.open()
                closeButton.bind(on_press=popup.dismiss)
                break

    pass


class GetRecommendationTvScreen(Screen):
    pass


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("settings.kv")


class WatcherApp(App):
    def build(self):
        return kv


if __name__ == '__main__':
    WatcherApp().run()
