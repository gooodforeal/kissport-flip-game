PYTHON=python3
PYTHON_BSD_LIN=python3.12
PYINSTALLER=pyinstaller
FILE_NAME=main.py
WINDOWS_SOURCE=.\source\windows\main.py
LINUX_SOURCE=`pwd`/source/linux/main.py
BSD_SOURCE=./source/netbsd/main.py
WINDOWS_OUTPUT=.\output\windows
LINUX_OUTPUT=`pwd`/output/linux
BSD_OUTPUT=`pwd`/output/netbsd
WINDOWS_OPTIONS=--onefile --console
LINUX_OPTIONS=--onefile --console
CLEANING_FILE=clear.py

all: windows linux web netbsd

windows:
	pip install -r requirements.txt
	@echo "Building for Windows..."
	$(PYINSTALLER) $(WINDOWS_OPTIONS) $(WINDOWS_SOURCE) --distpath $(WINDOWS_OUTPUT)
	$(WINDOWS_OUTPUT)\main.exe

web:
	@echo "Building for web..."
	pip install flask
	mkdir output\web\templates
	copy source\web\main.py output\web
	copy source\web\templates\flip.html output\web\templates
	python output/web/main.py

linux:
	@echo
	@echo "Building for Linux..."
	@echo
	apt install -y python3 1>/dev/null
	pip install -r requirements.txt
	$(PYINSTALLER) $(LINUX_OPTIONS) $(LINUX_SOURCE) --distpath $(LINUX_OUTPUT)
	$(LINUX_OUTPUT)/main.exe


netbsd:
	@echo "Building for NetBSD..."
	@echo
	pkgin -y install python312
	@cp -v $(BSD_SOURCE) $(BSD_OUTPUT)
	@echo
	@echo "Starting The Game"
	@echo
	$(PYTHON_BSD_LIN) $(BSD_OUTPUT)/main.py
clean:
	@echo "Cleaning..."
	python $(CLEANING_FILE)

.PHONY: all windows linux web exe netbsd clean
