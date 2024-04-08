# VideoShots
Allows you to select an area of the screen that will be recorded in the video format after activating the hotkeys
# Result
https://github.com/Tiques1/VideoShots/assets/112898566/c3d587c5-7d74-42ee-8bc0-1dec71679bc0
# Usage example
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
# Installation
For the reason that neither pyinstaller nor auto-py-to-exe can create a working exe file, and I can't understand why, I suggest the following scheme for installation.
## Install python
Latest on this moment 3.12.2 version is working
## Install dependencies
Don't do this in a virtual environment because it won't work. (idk why)  
If all goes wrong (idk why), don't specify versions in requirements.txt  
```
pip install -r requirements.txt
```
## Create vbs script and move it in startup folder
Simpliest way to autorun this program. Running through windows services are not working, even if c# script and service itself working correctly. I think the program doesn't see when I press key combinations (idk why)  

Win + R  
shell:startup  
Make there script.vbs  
```
Set WshShell = WScript.CreateObject("WScript.Shell")
Return = WshShell.Run("python D:\VideoShots\main.py", 0, false)
```
