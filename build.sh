pyinstaller --noconfirm --onefile --windowed --icon "images/cheese.ico" --name "Cheese-2.2-Ubuntu" --add-data="sounds:sounds/" --add-data="images:images/"  "main.py" --hidden-import="PIL._tkinter_finder"
./dist/Cheese-2.2-Ubuntu
