import json
from pathlib import Path

def save_json(data, file_path):
    Path(file_path).parent.mkdir(parents=True, exist_ok=True)  # Ensure directory exists
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4) 
    return file_path