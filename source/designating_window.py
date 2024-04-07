import tkinter


class Dwindow(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.config(cursor="tcross")
        # Not show in task panel
        self.attributes('-toolwindow', True)
        # Over all windows
        self.attributes('-topmost', True)
        # Transparent
        self.attributes("-alpha", 0.01)
        self.attributes('-fullscreen', True)
        # Убираем кнопки закрытия и сворачивания
        self.overrideredirect(True)


def main():
    dwindow = Dwindow()
    dwindow.mainloop()


if __name__ == '__main__':
    main()
