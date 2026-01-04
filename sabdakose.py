import sys
import json
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout,
    QMessageBox, QScrollArea, QFrame, QTextEdit
)
from PyQt6.QtGui import (QFont, QIcon)

# Load the JSON file
with open("sabdakosh.json", "r", encoding="utf-8") as f:
    sabdakosh = json.load(f)

class NepaliDictionary(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("नेपाली शब्दकोश")
        self.setWindowIcon(QIcon("logo.png"))
        self.setGeometry(100, 100, 700, 500)
        self.setMinimumSize(500, 350)

        font_name = "Nirmala UI"
        font_size = 12

        layout = QVBoxLayout()

        # Title
        title_label = QLabel("नेपाली शब्दकोश")
        title_label.setFont(QFont(font_name, 16, QFont.Weight.Bold))
        layout.addWidget(title_label)

        # Input label
        input_label = QLabel("शब्द लेख्नुहोस्:")
        input_label.setFont(QFont(font_name, font_size))
        layout.addWidget(input_label)

        # Single-line input for typing Nepali
        self.entry = QLineEdit()
        self.entry.setFont(QFont(font_name, font_size))
        self.entry.returnPressed.connect(self.search_word)  # Enter triggers search
        layout.addWidget(self.entry)

        # Search button
        search_button = QPushButton("खोज्नुहोस्")
        search_button.setFont(QFont(font_name, font_size))
        search_button.clicked.connect(self.search_word)
        layout.addWidget(search_button)

        # Scroll area for results
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.result_frame = QFrame()
        self.result_layout = QVBoxLayout()
        self.result_frame.setLayout(self.result_layout)
        self.scroll_area.setWidget(self.result_frame)
        layout.addWidget(self.scroll_area)

        self.result_label = QTextEdit()
        self.result_label.setReadOnly(True)
        self.result_label.setFont(QFont(font_name, font_size))
        self.result_layout.addWidget(self.result_label)

        self.setLayout(layout)

    def search_word(self):
        word = self.entry.text().strip()
        for item in sabdakosh:
            if item["word"] == word:
                definitions = []
                for d in item.get("definitions", []):
                    senses = d.get("senses", [])
                    grammar = d.get("grammar", "")
                    etymology = d.get("etymology", "")
                    text = ""
                    if grammar:
                        text += f"व्याकरण: {grammar}\n"
                    if etymology:
                        text += f"उत्पत्ति: {etymology}\n"
                    if senses:
                        text += "अर्थहरू:\n" + "\n".join(senses)
                    definitions.append(text.strip())
                self.result_label.setPlainText("\n\n".join(definitions))
                return
        QMessageBox.information(self, "फेला परेन", f"'{word}' शब्द शब्दकोशमा छैन")
        self.result_label.setPlainText("")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NepaliDictionary()
    window.show()
    sys.exit(app.exec())
