from pynput.mouse import Listener
import designating_window as dw
import threading
import multiprocessing


class Activator:
    def __init__(self):
        self.__flag = [False]
        self.__a = (0, 0)
        self.__b = (0, 0)

    def designate_area(self):
        des_win = multiprocessing.Process(target=dw.main)
        des_win.start()
        try:
            def on_click(x, y, button, pressed):
                if pressed:
                    self.__a = (x, y)
                else:
                    self.__b = (x, y)
                    listener.stop()

            with Listener(on_click=on_click) as listener:
                listener.join()
        finally:
            des_win.terminate()
        if self.__a[0] > self.__b[0] or self.__a[1] > self.__b[1]:
            x, y = self.__b[0:2]
            self.__b = self.__a
            self.__a = (x, y)

    def start_record(self, recorder):
        if self.__a[0] == self.__b[0] and self.__a[1] == self.__b[1]:
            return
        width = abs(self.__a[0] - self.__b[0])
        height = abs(self.__a[1] - self.__b[1])
        t = threading.Thread(target=recorder.record_rect, args=(self.__a[0], self.__a[1], width, height, self.__flag))
        t.start()

    def stop_record(self):
        self.__flag[0] = True
