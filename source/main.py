import activator
import recorder
import keyboard
import converter

def main():
	activator = activator.Activator()
	recorder = recorder.Recorder(directory='./examples/', convert=(converter.Format.GIF,))

	activator.designate_area()
	activator.start_record(recorder)
	keyboard.add_hotkey('ctrl+alt+w', activator.stop_record)

if __name__ == '__main__':
	keyboard.add_hotkey('ctrl+alt+q', main)
	while True:
		time.sleep(0.1) # in order not to overload the system
