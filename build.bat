call ./venv/Scripts/activate.bat
call pyinstaller main.py --onefile --name Table
call ./venv/Scripts/deactivate.bat
