#System
import sys

#Utils
from src.utils import os_utils as os
from src.utils import console
from src.utils import path

#editor
from src.engine import file_handler
from src.engine.actions import edit

#IO
from pathlib import Path

#DEFS
OS_NAME = os.get_os_name()
APP_VERSION = "1.0"

def main(args: list[str]):

    while True:

        console.print_main_menu(OS_NAME, APP_VERSION)
        
        user_input = console.show_prompt(
            "\n[bold green] Select an option[/bold green]",
            ["1","2","3"],
            False)

        try:
            match user_input:
                case "1":
                    path_input = path.path_parser(console.show_basic_text_input("[bold green] ╰─❯Enter path[/bold green]"))
                    file_content = file_handler.load_file_content(path_input)
                case "2":
                    path_input = path.path_parser(console.show_basic_text_input("[bold green] ╰─❯Enter new file path[/bold green]"))
                    file_handler.create_file(path_input)
                    file_content = file_handler.load_file_content(path_input)
                case "3":
                    console.clear()
                    console.print_message("[bold cyan]Good Bye![/bold cyan]")
                    sys.exit()
                    break
        except ValueError as ve:
            console.print_message(f"[bold red]{ve}[/bold red]")
            break
        except FileNotFoundError as fnf:
            console.print_message(f"[bold red]{fnf}[/bold red]")
            break
        except PermissionError as pe:
            console.print_message(f"[bold red]Access denied: {pe}. Maybe sudo?[/bold red]")
            break
        except Exception as ex:
            console.print_message("[bold red]An unknown error has occurred![/bold red]")
            break

        console.print_file("".join(file_content), path_input.name, path_input.suffix)

        console.print_styled_message(
            "[bold cyan]1[/bold cyan]. Edit\n"
            "[bold cyan]2[/bold cyan]. close file",
            "Actions",
            False,
            "cyan",
            True)

        file_action_input = console.show_prompt("[bold green]╰─❯[/bold green]",["1","2"], True)
        match file_action_input:
            case "1":
                console.print_message("1 selected")
                is_dirty = edit(file_content)
                if is_dirty:
                    file_handler.save_file(file_content, path_input)
                    console.print_message("[bold light_green]File saved![/bold light_green]")
            case "2":
                console.print_message("File closed")


if __name__ == "__main__":
    main(sys.argv)