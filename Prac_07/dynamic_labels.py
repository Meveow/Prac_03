from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import StringProperty
from kivy.core.window import Window


class DynamicLabels(App):
    label_text = StringProperty()
    names = ['Ava', 'Bob', 'Cane', 'Dory', 'Ein', 'Fred']

    def build(self):
        Window.size = (300, 500)
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.make_label()
        return self.root

    def make_label(self):
        for name in self.names:
            label_text = Label(text=name)
            self.root.ids.main.add_widget(label_text)


DynamicLabels().run()
