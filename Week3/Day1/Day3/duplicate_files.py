import os
import sys
import hashlib


def file_hash(filename):
    has = hashlib.sha256()
    with open(filename, 'rb', buffering=0) as f:
        for i in iter(lambda: f.read(128 * 1024), b''):
            has.update(i)
    return has.hexdigest()


def dup_files(main_folder):
    dictionary = {}
    stack = [main_folder]
    list_duplicate = []

    while stack:
        current = stack.pop()
        if os.path.isdir(current):
            for path in os.listdir(current):
                full_path = os.path.join(current, path)
                stack.append(full_path)
        else:
            file = file_hash(current)
            current_path = os.path.getmtime(current)
            if file in dictionary:
                element, ep = dictionary[file]
                if current_path > element:
                    list_duplicate.append((current, ep))
                else:
                    list_duplicate.append((ep, current))
                    dictionary[file] = (current_path, current)
            else:
                dictionary[file] = (current_path, current)
    return list_duplicate
