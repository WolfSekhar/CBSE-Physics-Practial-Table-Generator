echo "Activating Virtual Environment"
.\venv\Scripts\Activate.ps1
echo "Creating executable file"
pyinstaller main.py --onefile --name "PhysicsPracticalTable_by_P.Sekhar" --clean --icon=.\icon.ico
echo "Output file is saved in /dist folder"
echo 'Deactivating Virtual Environment'
deactivate
