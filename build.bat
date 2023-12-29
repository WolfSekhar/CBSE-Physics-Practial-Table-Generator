echo "Activating Virtual Environment"
call ./venv/Scripts/activate.bat

echo "Creating executable file"
call pyinstaller main.py --onefile --name "table" --icon=./icon.ico

echo "Output file is saved in /dist folder"

echo 'Deactivating Virtual Environment'
call deactivate

echo "renaming file"
rename "dist\table.exe" "PhyPGen_by_PSEKHAR.exe"
