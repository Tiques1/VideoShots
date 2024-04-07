The project is still in development
# VideoShots
Allows you to select an area of the screen that will be recorded in the video format after activating the hotkeys

## Usage example
Create objects
```python
activator = Activator()
recorder = Recorder()
```
It is possible set your own parameters
```python
from recorder import Codec
from converter import Format
recorder = Recorder(directory='D:\\Gif\\', codec=Codec.MP4, convert=(Format.Gif, ))
recorder.codec = Codec.AVI
recorder.dir = 'D:\\Folder\\'
```
Start recording
```python
activator.designate_area()
activator.start_record(recorder)
```
End recording
```python
activator.stop_record()
```
## Result
https://github.com/Tiques1/VideoShots/assets/112898566/c3d587c5-7d74-42ee-8bc0-1dec71679bc0






