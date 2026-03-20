#System
import sys

#Utils
from src.utils import os_utils as os
from src.utils import console
from src.utils import path

#editor
from src.engine import file_handler

#IO
from pathlib import Path

#DEFS
OS_NAME = os.get_os_name()
APP_VERSION = "1.0"

def main(args: list[str]):
    
    console.print_main_menu(OS_NAME, APP_VERSION)
    
    user_input = console.show_prompt(
        "\n[bold green] Select an option[/bold green]",
        ["1","2","3"],
        False)

    match user_input:
        case "1":
            path_input = path.path_parser(console.show_basic_text_input("[bold green] ╰─❯Enter path[/bold green]"))
            print(f"Se va a abrir: {path_input}")
            file_handler.open_file(path_input)
        case "2":
            print("2 selected")
        case "3":
            console.clear()
            console.print_message("[bold cyan]Good Bye![/bold cyan]")
            sys.exit()
        case _:
            print("Nothing selected")









if __name__ == "__main__":
    main(sys.argv)