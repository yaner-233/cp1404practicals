from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Obtain the input name and display a greeting"""
        print("test")
        self.root.ids.output_label.text = "Hello "
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def handle_clear(self):
        """Clear the contents of the text input box and output label"""
        self.root.ids.input_name.text = ""
        self.root.ids.output_label.text = ""



BoxLayoutDemo().run()
