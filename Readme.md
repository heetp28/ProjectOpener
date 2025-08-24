# **Project Handeler Utility**
This is made for those who have many folders and don't want to organize them. <br>
This programs run in the backgroud to access it you need to look at system tray (The arrow in the taskbar)

## How to install
1. Clone the repository to your desired location.<br>
2. Create a virtual environment. (py -m venv "environment_name")<br>
3. Open Virtual environment and download the required libraries (in requirements [use pip install -r requirements])
4. In your preferred terminal type <br> pyinstaller --onefile --noconsole --icon=file.ico Main.py <br>
5. If successful there will be a dist folder with the exe and you can delete the build folder <br>
6. Move file.ico and directory.json to the dist folder. <br>
***optional***<br>
7. Make a shortcut of the Main.py and then ,Open Task manager, go to Startup Apps > click three dots > open file location and cut-paste the shortcut there
