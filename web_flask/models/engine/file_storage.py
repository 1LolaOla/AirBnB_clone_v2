# models/engine/file_storage.py

class FileStorage:
    # Existing code...

    def close(self):
        """Deserialize the JSON file to objects"""
        self.reload()
