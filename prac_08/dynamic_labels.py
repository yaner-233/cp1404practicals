from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """An application for creating tags"""
    def __init__(self, **kwargs):
        super().__init__(** kwargs)
        self.names = ["Alice", "Bob", "Charlie", "Alex", "Mike", "Frank"]

    def build(self):
        """Build the application interface and dynamically generate tags"""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create tags for each name and add them."""
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)


if __name__ == "__main__":
    DynamicLabelsApp().run()
