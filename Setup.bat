if not exist Packages (
python -m venv Packages
)

call .\Packages\Scripts\activate.bat

python -m pip install --upgrade pip

pip install -r requirements

pyinstaller --onefile --noconsole --icon=file.ico Main.py

copy "file.ico" ".\dist\"
copy "directory.json" ".\dist\"