# StringVG

A simple GUI tool built with PyQt5 that allows batch modification of SVG files by adding or removing attributes from path elements.

## Features

- Add attributes to all `<path>` elements in SVG files
- Remove specific attributes from all `<path>` elements
- Process multiple SVG files in the current directory
- Progress bar to track batch processing
- Simple and intuitive interface

## Installation

1. Clone the repository:
```bash
git clone https://github.com/PeterCastler/StringVG.git
cd StringVG
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
.\venv\Scripts\activate  # On Windows
source venv/bin/activate  # On Unix or MacOS
```

3. Install dependencies:
```bash
pip install PyQt5
```

## Usage

1. Activate the virtual environment (if not already activated):
```bash
.\venv\Scripts\activate  # On Windows
source venv/bin/activate  # On Unix or MacOS
```

2. Run the script:
```bash
python StringVG.py
```

3. In the GUI:
   - Select whether to add or remove attributes
   - Enter the attribute string (e.g., `fill="currentColor"`)
   - Click "Process SVGs" to modify all SVG files in the current directory
   - Progress bar will show the processing status
   - Click "Close" when finished

## Requirements

- Python 3.8 or higher
- PyQt5

## License

MIT License

Copyright (c) 2024 Peter Castler
