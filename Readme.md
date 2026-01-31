# Memo App
A lightweight note-taking application for daily use.

## Features
- Create, read, update, delete notes
- Save notes to local file
- Simple command-line interface
- Search notes by keyword

## Installation

```bash
git clone https://github.com/thelkotolsantosh/Memo-app
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

## License

MIT License
