# simple-notes/
A lightweight note-taking application for daily use.

## Features
- Create, read, update, delete notes
- Save notes to local file
- Simple command-line interface
- Search notes by keyword

## Installation

```bash
git clone https://github.com/thelkotolsantosh/simple_notes
cd simple-notes
pip install -r requirements.txt
python main.py
```

## Usage

```bash
python main.py
```

Then follow the menu options:
1. Add note
2. View all notes
3. Search notes
4. Delete note
5. Exit

## Project Structure

```
simple-notes/
├── README.md
├── requirements.txt
├── setup.py
├── LICENSE
├── .gitignore
├── notes_app/
│   ├── __init__.py
│   ├── main.py
│   ├── note.py
│   ├── storage.py
│   └── utils.py
├── tests/
│   └── test_note.py
└── examples/
    └── usage.py
```

## Windows Installation

### Prerequisites
- Install Python 3.10 or newer
- Install Git

Verify installation:

```bash
python --version
git --version
```

### Clone Repository

```bash
git clone https://github.com/thelkotolsantosh/simple_notes.git
cd simple-notes
```

### Create Virtual Environment

```bash
python -m venv venv
```

Activate virtual environment:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python main.py
```

---

## Linux Installation

### Prerequisites

Install Python, pip, and Git.

Ubuntu/Debian:

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv git -y
```

Arch Linux:

```bash
sudo pacman -S python python-pip git
```

Fedora:

```bash
sudo dnf install python3 python3-pip git
```

Verify installation:

```bash
python3 --version
git --version
```

### Clone Repository

```bash
git clone https://github.com/thelkotolsantosh/simple_notes.git
cd simple-notes
```

### Create Virtual Environment

```bash
python3 -m venv venv
```

Activate virtual environment:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python3 main.py
```

---

## Troubleshooting

### Python Not Found

Windows:
- Reinstall Python and enable:
  - `Add Python to PATH`

Linux:
- Ensure Python is installed correctly.

### Permission Denied (Linux)

Use:

```bash
chmod +x main.py
```

### Virtual Environment Not Activating

Windows PowerShell:

```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then reactivate:

```bash
venv\Scripts\activate
```

## License

MIT License
