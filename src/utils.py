import os

def get_all_json_files(directory):
    json_files = []
    for f in os.listdir(directory):
        if f.endswith(".json"):
            json_files.append(f)
    return json_files
