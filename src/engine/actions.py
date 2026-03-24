from src.utils import console


#text input pro con el texto de la linea y de title la linea que se esta editando.
#Tal vez usar syntax?
def edit(content: list[str]) -> list[str]:
    line_amount = len(content)
    while True:
        line_number = console.show_basic_text_input(f"Enter line number to edit [1 - {line_amount}], [bold red]q[/bold red] to cancel", False)
        
        if line_number == "q":
            return

        if not line_number.isdigit():
            console.print_message("Only numbers! Use [bold red]q[/bold red] to cancel operation")
            continue
        
        line_number = int(line_number)
        
        if line_number > 0 and line_number <= line_amount:
            break
    
    console.print_styled_message(
        content[line_number - 1],
        f"Content of line N{line_number}",
        True,
        "cyan",
        expand=True,
    )

    new_text_input = console.show_basic_text_input("[bold]Text to insert (replace the selected line)[/bold]\n" \
    "[dim] You can cancel with the command [red]:q + Enter[/red][/dim]")

    if len(new_text_input[:2] == ":q"):
        console.print_message("YOU CANCEL THE OPERATION")

    # console.show_pro_text_input(
    #     f"Content of line N{line_number}",
    #     content[line_number - 1],
    #     True,
    #     True
    # )

    return []