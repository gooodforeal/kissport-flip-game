PYTHON=python3
PYINSTALLER=pyinstaller
SOURCE=main.py
TARGET=your_game
WINDOWS_OPTIONS = --onefile --console
LINUX_OPTIONS = --onefile --console

all: windows linux web

windows:
	@echo "Building for Windows..."
	$(PYINSTALLER) $(WINDOWS_OPTIONS) $(SOURCE) --distpath ./output/windows

linux:
	@echo "Building for Linux..."
	$(PYINSTALLER) $(LINUX_OPTIONS) $(SOURCE) --distpath ./dist/linux

web:
	@echo "Building for web..."

clean:
	@echo "Cleaning..."
	del /f main.spec
	rd /s /q dist
	rd /s /q build

.PHONY: all windows linux web clean