import toga

def button_handler(widget):
    print('hello')


def build(app):
    container = toga.Container()
    button = toga.Button('Hello World', on_press=button_handler)
    button.style.set(margin=50)
    container.add(button)

    return container

if __name__ == '__main__':
    app = toga.App('First App', 'org.pybee.helloworld', startup=build)
    app.main_loop()
