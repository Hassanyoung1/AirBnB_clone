#!/usr/bin/python3
def create_storage_instance():
    from . import file_storage
    storage = file_storage.FileStorage()
    storage.reload()
    return storage
