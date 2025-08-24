# **Project Handeler Utility**
This is made for those who have many folders and don't want to organize them. <br>
This programs run in the backgroud to access it you need to look at system tray (The arrow in the taskbar)

### *To Install just run Setup.bat <br>(you can check the code if you don't trust it)*

## How to install (if Setup doesn't work)
1. Clone the repository to your desired location.<br>
```sh
git clone https://github.com/heetp28/ProjectOpener.git
cd ProjectOpener
```
2. Create a virtual environment.<br>
```sh
python -m venv "Libraries"
```
3. Open Virtual environment and download the required libraries.
```sh
Libraries/Scripts/activate.bat
pip install -r requirements
```
4. In your preferred terminal type <br>
```sh
pyinstaller --onefile --noconsole --icon=file.ico Main.py
```
5. If successful there will be a dist folder with the exe and you can delete the build folder <br>
6. Move file.ico and directory.json to the dist folder. <br>
***optional***<br>
7. Make a shortcut of the Main.py and then ,Open Task manager, go to Startup Apps > click three dots > open file location and cut-paste the shortcut there
