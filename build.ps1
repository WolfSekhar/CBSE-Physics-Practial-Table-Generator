echo "Activating Virtual Environment"
.\venv\Scripts\Activate.ps1

echo "Creating executable file"
pyinstaller main.py --onefile --name "table" --clean --icon=.\icon.ico

echo "Output file is saved in /dist folder"

echo 'Deactivating Virtual Environment'
deactivate

echo "renaming file"
Rename-Item .\dist\table.exe PhyPGen_by_PSEKHAR.exe
