from models import Note

class Session:
    notes = []

    @staticmethod
    def add(note):
        Session.notes.append(note)

    @staticmethod
    def get():
        return Session.notes
