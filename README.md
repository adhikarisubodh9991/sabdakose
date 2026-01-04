# शब्दकोश (Sabdakosh) - Nepali Dictionary

<p align="center">
  <img src="logo.png" alt="Sabdakosh Logo" width="120"/>
</p>

<p align="center">
  <strong>A beautiful desktop Nepali Dictionary application built with PyQt6</strong>
</p>

<p align="center">
  <a href="#features">Features</a> •
  <a href="#download">Download</a> •
  <a href="#installation">Installation</a> •
  <a href="#usage">Usage</a> •
  <a href="#screenshots">Screenshots</a> •
  <a href="#contributing">Contributing</a>
</p>

---

## ✨ Features

- 🔍 **Fast Word Search** - Instantly search for Nepali words
- 📖 **Comprehensive Definitions** - Get detailed meanings, grammar info, and etymology
- 🎨 **Beautiful UI** - Clean and intuitive interface with native Nepali font support
- ⚡ **Lightweight** - Fast startup and minimal resource usage
- 🖥️ **Cross-platform** - Works on Windows, macOS, and Linux

## 📥 Download

### Windows Installer

Download the latest version from the [**Releases**](../../releases/latest) page:

| Platform | Download |
|----------|----------|
| Windows (64-bit) | [**Sabdakosh.exe**](../../releases/latest/download/sabdakosh.exe) |

> 💡 **Note**: The Windows executable is a standalone application - no installation required! Just download and run.

## 🛠️ Installation (From Source)

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/sabdakosh.git
   cd sabdakosh
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python sabdakose.py
   ```

## 📖 Usage

1. Launch the application
2. Type a Nepali word in the search box
3. Press **Enter** or click **"खोज्नुहोस्"** (Search)
4. View the word's definition, grammar, and etymology

## 📸 Screenshots

<p align="center">
  <img src="screenshots/main.png" alt="Main Window" width="600"/>
</p>

## 🏗️ Building Executable

To create a standalone executable:

```bash
pip install pyinstaller
pyinstaller --onefile --windowed --icon=icon.ico --add-data "sabdakosh.json;." --add-data "logo.png;." sabdakose.py
```

## 📁 Project Structure

```
sabdakosh/
├── sabdakose.py      # Main application code
├── sabdakosh.json    # Dictionary database
├── logo.png          # Application logo
├── icon.ico          # Windows icon
├── requirements.txt  # Python dependencies
└── README.md         # This file
```

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** your changes (`git commit -m 'Add some AmazingFeature'`)
4. **Push** to the branch (`git push origin feature/AmazingFeature`)
5. **Open** a Pull Request

### Adding Words to Dictionary

You can contribute by adding new words to `sabdakosh.json`:

```json
{
  "word": "नेपाल",
  "definitions": [
    {
      "grammar": "नाम",
      "etymology": "संस्कृत",
      "senses": ["हिमालयको काखमा रहेको देश", "दक्षिण एशियाको एक देश"]
    }
  ]
}
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Your Name**

- GitHub: [@YOUR_USERNAME](https://github.com/YOUR_USERNAME)

---

<p align="center">
  Made with ❤️ for the Nepali language
</p>
