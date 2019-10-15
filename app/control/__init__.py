from .main import MainWindow


def init_app(**kwargs):
    global main_window
    main_window = MainWindow(**kwargs)
    main_window.show()
