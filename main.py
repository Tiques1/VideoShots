import time
from activator import Activator
from recorder import Recorder
import keyboard
from converter import Format

if __name__ == '__main__':
    time.sleep(2)
    activator = Activator()
    recorder = Recorder(directory='./examples/', convert=(Format.GIF, ))

    activator.designate_area()
    activator.start_record(recorder)
    keyboard.add_hotkey('ctrl+alt+w', activator.stop_record)
