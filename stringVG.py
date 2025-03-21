import sys
import os
import re
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, 
                            QRadioButton, QLineEdit, QPushButton,
                            QHBoxLayout, QButtonGroup, QProgressBar)

def modify_svg_path(file_path, add_string=None, remove_string=None):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            
        # Find all path tags
        path_pattern = r'<path([^>]*)>'
        
        if remove_string and remove_string in content:
            content = content.replace(remove_string, '')
            
        if add_string:
            def path_replacer(match):
                path_content = match.group(1)
                # Add the new string at the start of the path attributes
                return f'<path {add_string}{path_content}>'
                
            content = re.sub(path_pattern, path_replacer, content)
            
        with open(file_path, 'w') as file:
            file.write(content)
            
        return True, "SVG modified successfully"
        
    except Exception as e:
        return False, f"Error: {str(e)}"

class SVGModifierUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        layout = QVBoxLayout()
        
        # Radio buttons
        self.radio_group = QButtonGroup()
        
        self.add_radio = QRadioButton('Add string:')
        self.add_radio.setChecked(True)
        self.remove_radio = QRadioButton('Remove string:')
        
        self.radio_group.addButton(self.add_radio)
        self.radio_group.addButton(self.remove_radio)
        
        # Input field
        self.input_field = QLineEdit()
        
        # Progress bar
        self.progress_bar = QProgressBar()
        self.progress_bar.setMinimum(0)
        self.progress_bar.setValue(0)
        
        # Buttons
        btn_layout = QHBoxLayout()
        self.ok_btn = QPushButton('Process SVGs')  # Changed text to be more descriptive
        self.cancel_btn = QPushButton('Close')
        
        # Add widgets to layouts
        layout.addWidget(self.add_radio)
        layout.addWidget(self.remove_radio)
        layout.addWidget(self.input_field)
        layout.addWidget(self.progress_bar)
        
        btn_layout.addWidget(self.ok_btn)
        btn_layout.addWidget(self.cancel_btn)
        layout.addLayout(btn_layout)
        
        self.setLayout(layout)
        
        # Connect buttons
        self.ok_btn.clicked.connect(self.process_svgs)
        self.cancel_btn.clicked.connect(self.close)
        
        # Window settings
        self.setWindowTitle('StringVG')
        self.setGeometry(300, 300, 325, 150)
        
    def process_svgs(self):
        input_string = self.input_field.text().strip()
        if not input_string:
            return
            
        # Get list of SVG files first
        svg_files = [f for f in os.listdir('.') if f.endswith('.svg')]
        total_files = len(svg_files)
        
        if total_files == 0:
            return
            
        # Set up progress bar
        self.progress_bar.setMaximum(total_files)
        self.progress_bar.setValue(0)
        
        # Process all SVG files in current directory
        for i, file in enumerate(svg_files):
            if self.add_radio.isChecked():
                success, message = modify_svg_path(file, add_string=input_string)
            else:
                success, message = modify_svg_path(file, remove_string=input_string)
            print(f"{file}: {message}")
            
            # Update progress
            self.progress_bar.setValue(i + 1)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SVGModifierUI()
    ex.show()
    sys.exit(app.exec_())
