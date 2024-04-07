import pyautogui
import cv2
import numpy as np
from datetime import datetime
from enum import Enum
import subprocess
import time
from converter import Converter


class Codec(Enum):
    MP4 = ('mp4v', '.mp4')
    AVI = ('XVID', '.avi')


class Recorder:
    def __init__(self, directory='D:\\Gif\\', codec=Codec.MP4, convert=()):
        self.dir = directory
        self.codec: Codec = codec
        self.convert = convert

    def record_rect(self, x, y, width: int, height: int, flag):
        frames = []
        new_timer = subprocess.Popen(["python3", "timer.py"])
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
        path = self.dir + str(datetime.now()).replace(':', '-') + self.codec.value[1]
        out = cv2.VideoWriter(path, codec, fps, resolution)

        for img in frames:
            frame = np.array(img)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            out.write(frame)

        out.release()

        for ext in self.convert:
            Converter.function(ext)(path, path[0:-4] + ext.value, fps)
