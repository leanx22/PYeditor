from pathlib import Path
from src.definitions.enums import PathType

MAIN_PATH = Path.cwd() / "src"

def path_parser(path: str) -> Path:
    complete_path = MAIN_PATH / path
    #resolve puede manejar ruta absoluta o relativa de forma automatica
    parsed = complete_path.resolve()
    return parsed

