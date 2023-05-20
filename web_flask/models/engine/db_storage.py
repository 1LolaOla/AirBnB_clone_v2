# models/engine/db_storage.py

from models.state import State

class DBStorage:
    # Existing code...

    def close(self):
        """Close the current session"""
        self.__session.remove()
