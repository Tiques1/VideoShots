import imageio
# import pyperclip
import os
from enum import Enum


class Format(Enum):
    GIF = '.gif'


class Converter:
    @staticmethod
    def gif(another, new, _fps):
        if not os.path.exists(another):
            return
        with imageio.get_writer(new, mode='I', fps=_fps) as writer:
            video = imageio.get_reader(another)
            for frame in video:
                writer.append_data(frame)

    # @staticmethod
    # def copy_to_clipboard(path):
    #     if not os.path.exists(path):
    #         return
    #     with open(path, 'rb') as f:
    #         video_data = f.read().decode('latin-1')
    #         pyperclip.copy(video_data)

    @staticmethod
    def function(ext):
        func = {Format.GIF: Converter.gif}
        return func.get(ext)
