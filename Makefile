all: create_executable

compile_views:
	pyrcc5 ./Resources/resources.qrc -o ./View/resources_rc.py
	pyuic5 ./UI/MainWindow.ui -o ./View/MainWindowView.py  --import-from View -i 0

create_executable: compile_views
	pyinstaller.exe "Extrator de Histerese.py" --onefile --windowed


clean:
	DEL /Q/S build
	DEL /Q/S dist