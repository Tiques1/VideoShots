import activator
import recorder
import keyboard
import converter

if __name__ == '__main__':
	activator = activator.Activator()
	recorder = recorder.Recorder(directory='./examples/', convert=(converter.Format.GIF,))

	activator.designate_area()
	activator.start_record(recorder)
	keyboard.add_hotkey('ctrl+alt+w', activator.stop_record)
