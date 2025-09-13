#!/bin/bash
echo "Installing PyInstaller..."
pip install pyinstaller

echo ""
echo "Building executable..."
pyinstaller --onefile --windowed --name "Calculator" calculator.py

echo ""
echo "Build complete! The executable can be found in the 'dist' folder."
echo "File: dist/Calculator"
