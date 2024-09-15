PYTHON=python3
PYINSTALLER=pyinstaller
FILE_NAME=main.py
SOURCE_WINDOWS=./source/windows/main.py
SOURCE_LINUX=./source/linux/main.py
OUTPUT_WINDOWS=./output/exe
OUTPUT_LINUX=./output/linux
WINDOWS_OPTIONS = --onefile --console
LINUX_OPTIONS = --onefile --console

all: install exe windows linux web

install:
	pip install -r requirements.txt

exe:
	@echo "Building exe..."
	$(PYINSTALLER) $(WINDOWS_OPTIONS) $(SOURCE_WINDOWS) --distpath $(OUTPUT_WINDOWS)

windows:
	@echo "Building for Windows..."
	copy source\windows\main.py output\windows
	python output/windows/main.py

linux:
	@echo "Building for Linux..."
	cp $(SOURCE_LINUX) $(OUTPUT_LINUX)
	cd $(OUTPUT_LINUX)
	$(PYTHON) $(FILE_NAME)

web:
	@echo "Building for web..."
	pip install flask


clean:
	@echo "Cleaning..."
	python clear.py

.PHONY: all windows linux web exe clean