echo "Activating Virtual Environment"
call ./venv/Scripts/activate.bat

echo "Creating executable file"
call pyinstaller main.py --onefile --name "PhysicsPracticalTable_by_P.Sekhar"

echo "Output file is saved in /dist folder"

echo 'Deactivating Virtual Environment'
call ./venv/Scripts/deactivate.bat
