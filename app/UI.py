"""User interface"""

def show_menu():
    """Display menu"""
    print("\n" + "="*30)
    print("  QUICK NOTES")
    print("="*30)
    print("1. Add note")
    print("2. View notes")
    print("3. Search")
    print("4. Delete")
    print("5. Exit")
    print("="*30)


def show_note(note):
    """Display single note"""
    print(f"\nID: {note.id}")
    print(f"Title: {note.title}")
    print(f"Text: {note.text}")
    print(f"Date: {note.date}")


def show_notes(notes):
    """Display all notes"""
    if not notes:
        print("No notes")
        return
    
    for i, note in enumerate(notes, 1):
        print(f"{i}. {note.title} ({note.id})")


def input_note():
    """Get note input"""
    title = input("Title: ")
    text = input("Text: ")
    return title, text


def input_id():
    """Get note ID"""
    return input("Note ID: ")


def input_search():
    """Get search term"""
    return input("Search: ")
