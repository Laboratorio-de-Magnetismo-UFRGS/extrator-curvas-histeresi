build:
	pyrcc5 ./Resources/resources.qrc -o ./View/resources_rc.py
	pyuic5 ./UI/MainWindow.ui -o ./View/MainWindowView.py  --import-from View -i 0

create_executable:
	pyinstaller.exe .\Application.spec --icon=.\Resources\icons\icon.png

all: build create_executable

clean:
	rm -rf .\build
	rm -rf .\dist