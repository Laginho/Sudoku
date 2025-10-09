from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout


class MyApp(App):
    def build(self):
        return BoxLayout(orientation="vertical")

    def on_start(self):
        self.root.add_widget(Label(text="Hello, world!"))
        self.root.add_widget(Button(text="Click me!"))


if __name__ == "__main__":
    MyApp().run()
