import tkinter


class Timer(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title("Timer")

        # Задаем фиксированный размер
        self.geometry("300x200")

        # Убираем кнопки закрытия и сворачивания
        self.overrideredirect(True)

        # Создаем рамку с скругленными краями
        self['bg'] = 'black'
        self.attributes('-transparentcolor', 'black')
        self.attributes("-alpha", 0.5)

        # Поверх всех окон
        self.attributes('-topmost', True)

        # Создаем метку для отображения таймера
        self.timer_label = tkinter.Label(self, text="", font=("Tahoma", 24), fg='white', bg='#242630')
        self.timer_label.pack(pady=20)

        # Запускаем функцию update_timer для обновления времени
        self.elapsed_time = 0
        self.update_timer()

    def update_timer(self):
        self.elapsed_time += 1
        hours = self.elapsed_time // 3600
        minutes = (self.elapsed_time % 3600) // 60
        seconds = (self.elapsed_time % 3600) % 60
        self.timer_label.config(text="{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds))
        # Запустить функцию update_timer снова через 1 секунду (1000 миллисекунд)
        self.after(1000, self.update_timer)


def main():
    timer = Timer()
    timer.mainloop()


if __name__ == '__main__':
    main()
