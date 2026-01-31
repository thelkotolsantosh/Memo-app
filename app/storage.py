"""Save and load notes"""

import json
import os
from app.note import Note


class Storage:
    """Handle file storage"""
    
    def __init__(self, filename='notes.json'):
        self.filename = filename
    
    def save(self, notes):
        """Save to file"""
        data = [n.to_dict() for n in notes]
        with open(self.filename, 'w') as f:
            json.dump(data, f)
    
    def load(self):
        """Load from file"""
        if not os.path.exists(self.filename):
            return []
        
        with open(self.filename, 'r') as f:
            data = json.load(f)
        
        return [Note.from_dict(d) for d in data]
