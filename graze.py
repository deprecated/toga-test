import toga
from colosseum import CSS



class Graze(toga.App):
    def startup(self):
        self.main_window = toga.MainWindow(self.name)
        self.main_window.app = self

        self.webview = toga.WebView(style=CSS(flex=1))
        self.url_input = toga.TextInput(
            initial='https://github.com/',
            style=CSS(flex=1, margin=5)
        )

        container = toga.Container(
            children=[
                toga.Container(
                    children=[self.url_input,
                              toga.Button('Go', on_press=self.load_page,
                                          style=CSS(width=50))],
                    style=CSS(flex_direction='row')),
                self.webview],
            style=CSS(
                flex_direction='column'
            )
        )

        self.main_window.content = container
        self.webview.url = self.url_input.value

        # Show the main window
        self.main_window.show()

    def load_page(self, widget):
        url = self.url_input.value
        if not url.startswith('http'):
            url = 'https://' + url
        print('Setting URL to', url)
        self.webview.url = url

if __name__ == '__main__':
    app = Graze('Graze', 'org.henney.graze')

    app.main_loop()
