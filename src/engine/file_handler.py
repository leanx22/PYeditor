from pathlib import Path
from src.utils import console
from src.definitions.const import ALLOWED_FILES

def is_valid_file(path: Path) -> bool:
    suffix = path.suffix.lower()

    if suffix == "":
        return True
    
    return suffix in ALLOWED_FILES

def create_file(path: Path):
    if path.exists():
        raise ValueError(f"File already exists. Use 'open file' option instead.")

    if path.is_dir():
        raise ValueError("File name and extension must be declared in path")
    
    if not is_valid_file(path):
        raise ValueError(f"File: {path} | Is not supported!")
    
    with path.open("w", encoding="utf-8") as f:
        f.write("")

def load_file_content(path: Path) -> list[str]:
    
    if not path.exists():
        raise FileNotFoundError(f"Error: {path} | Not found!")

    if path.is_dir():
        raise ValueError(f"Path: {path} | Is not a file!")

    #En caso de existir, verifico que sea una extension permitida
    if not is_valid_file(path):
        raise ValueError(f"File: {path} | Is not supported!")    

    with path.open("r", encoding="utf-8") as f:
        content = f.readlines()

    #console.print_file(full_content, path.name, path.suffix)
    return content

def save_file(content: list[str], path: Path):
    with path.open("w", encoding="utf-8") as f:
        f.writelines(content)
