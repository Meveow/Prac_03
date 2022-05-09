from kivy.app import App
from kivy.lang import Builder

M_TO_KM = 1.60934


class Conversion(App):
    def build(self):
        self.title = "Conversion"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self, value):
        result = float(value) * M_TO_KM
        self.root.ids.output_label.text = str(result)

    def increment(self, value):
        increase = int(value) + 1
        self.root.ids.input_number.text = str(increase)

    def decrement(self, value):
        decrease = int(value) - 1
        self.root.ids.input_number.text = str(decrease)



Conversion().run()
