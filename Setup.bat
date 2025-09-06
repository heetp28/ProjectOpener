if not exist Packages (
python -m venv Packages
)

call .\Packages\Scripts\activate.bat

python -m pip install --upgrade pip

pip install -r requirements

pyinstaller --onefile --noconsole --icon=file.ico Main.py

copy "file.ico" ".\dist\"
copy "directory.json" ".\dist\"

:AskStartUp
set /p choice="Add as Start App (y/n): "
if /i "%choice%"=="y" goto AddStartUp
if /i "%choice%"=="n" goto SkipStartUp
echo Enter a Valid Option y/n.
goto AskStartUp

:AskStartUp
set STARTUP_FOLDER=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup
set SHORTCUT_NAME=ProjectOpener.lnk
powershell "$s=(New-Object -COM WScript.Shell).CreateShortcut('%STARTUP_FOLDER%/%SHORTCUT_NAME%');$s.TargetPath='%CD%\dist\Main.exe';$s.Save()"

:SkipStartUp
echo done (you can't even read this message [if you run setup.bat])