#!/usr/bin/python3
"""
Initialize FileStorage and reload data from the JSON file.
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()