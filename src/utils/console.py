from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.syntax import Syntax

console = Console()

def print_main_menu(os_name: str, app_version: str):

    options = (
        "[bold cyan]1.[/bold cyan] Open file\n"
        "[bold cyan]2.[/bold cyan] New file\n"
        "[bold cyan]3.[/bold cyan] Exit"
    )

    title = f"[bold yellow]PYeditor[/bold yellow] - Leandro Guia - {os_name} - v{app_version}"

    menu = Panel(
        options,
        title = title,
        #subtitle="[dim]Pick an option[/dim]", #Texto inferior
        border_style="blue", #Color de marco
        expand=False,#Se ajusta al texto en lugar de expandirse en toda la pantalla
        padding=(1,5)
    )
   
    console.clear()
    console.print(menu)


def show_prompt(message: str, options: list[str], show_options: bool) -> str:
    user_selection = Prompt.ask(
        message,
        choices=options,
        show_choices=show_options,
    )
    return user_selection

def show_basic_text_input(message: str, clear=False) -> str:
    if clear:
        console.clear()
    user_input = Prompt.ask(message)
    return user_input.strip()

def show_pro_text_input(title:str, message: str, clear=False)->str:
    panel = Panel(
        message,
        title=title,
        title_align="left",
        border_style="cyan",
        padding=(0,2),
        expand=False
    )
    
    if clear:
        console.clear()
    
    console.print(panel)
    user_input = console.input("[bold cyan]╰─❯ [/bold cyan]").strip()
    return user_input

def print_message(message: str):
    console.print(message)

def print_file(content: str, file_name: str, file_suffix: str):
    file_type = file_suffix.lstrip(".") or "text"

    styled_text = Syntax(
        content,
        lexer=file_type,
        theme="lightbulb",
        background_color="default",
        line_numbers=True,
        word_wrap=True
    )

    visor = Panel(
        styled_text,
        title=f"[bold cyan]PYeditor[/bold cyan] | [bold yellow]{file_name}[/bold yellow]",
        subtitle="[dim]READ MODE[/dim]",
        border_style="cyan",
        padding=(1,1)
    )

    console.clear()
    console.print(visor)

def clear():
    console.clear()
