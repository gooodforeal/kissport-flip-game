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
BSD_PRE_PRE_FLAGS=LD_LIBRARY_PATH=/usr/pkg/include/python3.12/:/usr/pkg/lib/
BSD_PRE_FLAGS=-Os -I/usr/pkg/include/python3.12 -I/usr/pkg/include/python3.12 -L/usr/pkg/lib  -lintl -lpthread -lcrypt -lutil -lm

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
	copy source\web\app.py output\web
	copy source\web\templates\flip.html output\web\templates
	copy source\web\templates\index.html output\web\templates
	python output/web/app.py

linux:
	@echo "Building for Linux..."
	@echo
	@echo "Installing python, pip, PyInstaller...\n"
	@apt install -y python3 python3-pip make
	@pip install --break-system-packages -r requirements.txt
	@echo "Done\n"
	@echo "Building Binary file..."
	@$(PYINSTALLER) $(LINUX_OPTIONS) $(LINUX_SOURCE) --distpath $(LINUX_OUTPUT)
	@echo "Done\n"
	@echo
	@echo "Built file located in $(LINUX_OUTPUT)"
	@echo


netbsd:
	@echo "Building for NetBSD..."
	@echo
	@printf "Installing python, pip, cython..."
	@pkgin -y install python312 py312-pip
	@pip3.12 -q install cython
	@printf "Done\n"
	@cp -v $(BSD_SOURCE) $(BSD_OUTPUT)
	@echo "Building C++ file..."
	@$(PYTHON_BSD_LIN) -m cython $(BSD_OUTPUT)/$(FILE_NAME) --embed
	@printf "Done\n"
	@printf "Compiling C++ file..."
	@ $(BSD_PRE_PRE_FLAGS) gcc $(BSD_PRE_FLAGS) $(BSD_OUTPUT)/main.c -o $(BSD_OUTPUT)/main -lpython3.12
	@printf "Done\n"
	@echo
	@echo "Built file located in $(BSD_OUTPUT)"
	@echo

clean:
	@echo "Cleaning..."
	python $(CLEANING_FILE)

.PHONY: all windows linux web netbsd clean
