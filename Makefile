all:
	pyrcc5 ./Resources/resources.qrc -o ./View/resources_rc.py
	pyuic5 ./UI/MainWindow.ui -o ./View/MainWindowView.py  --import-from View -i 0

# clean:
# 	rm -rf ./View/*View.py
# 	rm -rf ./View/resources_rc.py