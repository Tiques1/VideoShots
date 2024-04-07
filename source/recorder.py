import multiprocessing
import pyautogui
import cv2
import numpy as np
import datetime
import enum
import time
import timer
import converter


class Codec(enum.Enum):
    MP4 = ('mp4v', '.mp4')
    AVI = ('XVID', '.avi')


class Recorder:
    def __init__(self, directory='D:\\Gif\\', codec=Codec.MP4, convert=()):
        self.dir = directory
        self.codec: Codec = codec
        self.convert = convert

    def record_rect(self, x, y, width: int, height: int, flag):
        frames = []
        new_timer = multiprocessing.Process(target=timer.main)
        new_timer.start()
        start = time.perf_counter()

        try:
            while not flag[0]:
                frames.append(pyautogui.screenshot(region=(x, y, width, height)))
        finally:
            end = time.perf_counter()
            new_timer.terminate()

        total = end - start
        fps = int(len(frames)/total)

        resolution = (width, height)
        codec = cv2.VideoWriter_fourcc(*self.codec.value[0])
        path = self.dir + str(datetime.datetime.now()).replace(':', '-') + self.codec.value[1]
        out = cv2.VideoWriter(path, codec, fps, resolution)

        for img in frames:
            frame = np.array(img)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            out.write(frame)

        out.release()

        for ext in self.convert:
            func = converter.Converter.function(ext)
            p = multiprocessing.Process(target=func, args=(path, path[0:-4] + ext.value, fps))
            p.start()
            p.join()
