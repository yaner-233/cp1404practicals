from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty


class MilesToKilometersConverter(App):
    """Mile to Kilometer Converter App, Processing Logic and Data Binding"""
    output_km = StringProperty()

    def build(self):
        """Build the application interface"""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_increment(self, change):
        """Handle the Up/Down buttons: increase or decrease the number of miles"""
        new_miles = self.get_valid_miles() + change
        self.root.ids.input_miles.text = str(new_miles)
        self.handle_convert()

    def handle_convert(self):
        """Handle calculation,update output_km"""
        miles = self.get_valid_miles()
        new_miles = miles * 1.60934
        self.output_km = f"{new_miles}"

    def get_valid_miles(self):
        """Return 0 if input is empty/invalid, else return float miles"""
        try:
            miles = float(self.root.ids.input_miles.text)
            return miles
        except ValueError:
            return 0


if __name__ == "__main__":
    MilesToKilometersConverter().run()

