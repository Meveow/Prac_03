from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

M_TO_KM = 1.60934


class Conversion(App):

    def build(self):
        Window.size = (800, 400)
        self.title = "Conversion"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self, value):
        print("calculating")
        try:
            result = float(value) * M_TO_KM
            self.root.ids.output_label.text = str(result)
        except ValueError:
            self.root.ids.input_number.text = '0.0'
            self.root.ids.output_label.text = '0.0'

    def increment(self, value):
        print("increasing")
        try:
            increase = float(value) + 1
            self.root.ids.input_number.text = str(increase)
        except ValueError:
            self.root.ids.input_number.text = '0.0'

    def decrement(self, value):
        print("decreasing")
        try:
            decrease = float(value) - 1
            self.root.ids.input_number.text = str(decrease)
        except ValueError:
            self.root.ids.input_number.text = '0.0'


Conversion().run()
