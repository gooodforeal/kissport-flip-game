PYTHON=python3
PYINSTALLER=pyinstaller
FILE_NAME=main.py
SOURCE_WINDOWS=./source/windows/main.py
SOURCE_LINUX=./source/linux/main.py
OUTPUT_WINDOWS=./output/windows
OUTPUT_LINUX=./output/linux
WINDOWS_OPTIONS = --onefile --console
LINUX_OPTIONS = --onefile --console

all: windows linux web

windows:
	@echo "Building for Windows..."
	$(PYINSTALLER) $(WINDOWS_OPTIONS) $(SOURCE_WINDOWS) --distpath $(OUTPUT_WINDOWS)

linux:
	@echo "Building for Linux..."
	cp $(SOURCE_LINUX) $(OUTPUT_LINUX)
	cd $(OUTPUT_LINUX)
	$(PYTHON) $(FILE_NAME)

web:
	@echo "Building for web..."

clean:
	@echo "Cleaning..."
	del /f main.spec
	rd /s /q output
	rd /s /q build

.PHONY: all windows linux web clean