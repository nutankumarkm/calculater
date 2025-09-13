# Calculator Application

A modern GUI calculator application built with Python and tkinter that can be converted to a standalone executable (.exe) file.

## Features

- **Basic Operations**: Addition (+), Subtraction (-), Multiplication (×), Division (÷)
- **Advanced Functions**: Square root (√), Square (x²), Reciprocal (1/x), Percentage (%)
- **Utility Functions**: Clear (C), Clear Entry (CE), Backspace (⌫), Sign Toggle (±)
- **Modern UI**: Clean, colorful interface with intuitive button layout
- **Error Handling**: Proper error messages for invalid operations

## Running the Application

### Option 1: Run as Python Script
```bash
python calculator.py
```

### Option 2: Build Executable (.exe)

#### Windows:
1. Install PyInstaller:
   ```bash
   pip install pyinstaller
   ```

2. Run the build script:
   ```bash
   build.bat
   ```

3. Or manually build:
   ```bash
   pyinstaller --onefile --windowed --name "Calculator" calculator.py
   ```

#### Linux/Mac:
1. Install PyInstaller:
   ```bash
   pip install pyinstaller
   ```

2. Run the build script:
   ```bash
   chmod +x build.sh
   ./build.sh
   ```

3. Or manually build:
   ```bash
   pyinstaller --onefile --windowed --name "Calculator" calculator.py
   ```

## Output

After building, you'll find the executable in the `dist` folder:
- **Windows**: `dist/Calculator.exe`
- **Linux/Mac**: `dist/Calculator`

## Requirements

- Python 3.6 or higher
- tkinter (included with Python)
- PyInstaller (for building executable)

## Installation

1. Clone or download this repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Numbers**: Click number buttons (0-9) to input numbers
2. **Operations**: Click operation buttons (+, -, ×, ÷) to perform calculations
3. **Equals**: Click '=' to get the result
4. **Clear**: Use 'C' to clear everything or 'CE' to clear current entry
5. **Advanced**: Use √, x², 1/x, % for advanced calculations
6. **Backspace**: Use ⌫ to delete the last entered digit
7. **Sign**: Use ± to toggle positive/negative

## File Structure

```
├── calculator.py          # Main calculator application
├── requirements.txt       # Python dependencies
├── build.bat             # Windows build script
├── build.sh              # Linux/Mac build script
└── README.md             # This file
```

## Troubleshooting

- **Import Error**: Make sure you have Python installed with tkinter support
- **Build Error**: Ensure PyInstaller is installed: `pip install pyinstaller`
- **Executable Not Working**: Try building without `--windowed` flag for console output

## License

This project is open source and available under the MIT License.
