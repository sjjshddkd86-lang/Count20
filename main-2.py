from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty

class CounterLayout(BoxLayout):
    count = NumericProperty(0)

    def increase(self):
        self.count += 1

    def decrease(self):
        self.count -= 1

    def reset(self):
        self.count = 0

class CounterApp(App):
    def build(self):
        self.title = "Counter App"
        return CounterLayout()

if __name__ == "__main__":
    CounterApp().run()
