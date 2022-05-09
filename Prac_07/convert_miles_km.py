from kivy.app import App
from kivy.lang import Builder

M_TO_KM = 1.60934


class ConvertMilesToKm(App):
    def build(self):
        self.title = "Conversion"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self, value):
        result = float(value) * M_TO_KM
        self.root.ids.output_label.text = str(result)
        return result


ConvertMilesToKm().run()
