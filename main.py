from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

from kivy.config import Config

Config.set("graphics", "width", 300)
Config.set("graphics", "height", 650)


class MainApp(App):
    def build(self):
        main_bl = BoxLayout(orientation="vertical")
        information_bl = BoxLayout()
        buttons_bl = BoxLayout(padding=(25, 150, 25, 25), spacing=25)

        history = Label(text='200 руб.\t-\n150 руб.\t+'.expandtabs(8))

        main_bl.add_widget(information_bl)
        main_bl.add_widget(history)
        main_bl.add_widget(buttons_bl)

        income = Label(text="Доход: 0")
        expenses = Label(text="Расход: 0")

        add = Button(text="Добавить")
        reduce = Button(text="Убавить")

        information_bl.add_widget(income)
        information_bl.add_widget(expenses)

        buttons_bl.add_widget(add)
        buttons_bl.add_widget(reduce)

        return main_bl


if __name__ == '__main__':
    app = MainApp()
    app.run()
