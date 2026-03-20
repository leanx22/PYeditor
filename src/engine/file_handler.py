from pathlib import Path
from src.utils import console
from src.definitions.const import ALLOWED_FILES

def is_valid_file(path: Path) -> bool:
    suffix = path.suffix.lower()

    if suffix == "":
        return True
    
    return suffix in ALLOWED_FILES

def open_file(path: Path):
    
    if not path.exists():
        raise FileNotFoundError(f"Error: {path} | Not found!")

    if path.is_dir():
        raise ValueError(f"Path: {path} | Is not a file!")

    #En caso de existir, verifico que sea una extension permitida
    if not is_valid_file(path):
        raise ValueError(f"File: {path} | Is not supported!")

    content = []

    with path.open("r", encoding="utf-8") as f:
        for line in f:
            content.append(line)

    full_content = "".join(content)

    console.print_file(full_content, path.name, path.suffix)

    return