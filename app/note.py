"""Note model"""

from datetime import datetime
import uuid


class Note:
    """Single note"""
    
    def __init__(self, title, text):
        self.id = str(uuid.uuid4())[:8]
        self.title = title
        self.text = text
        self.date = datetime.now().isoformat()
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'text': self.text,
            'date': self.date
        }
    
    @staticmethod
    def from_dict(data):
        note = Note(data['title'], data['text'])
        note.id = data['id']
        note.date = data['date']
        return note
