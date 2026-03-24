from src.utils import console


def edit(content: list[str]) -> bool:
    
    if not content:
            content.append("")
    
    line_amount = len(content)
    
    while True:    
        
        line_number = console.show_basic_text_input(f"Enter line number to edit [1 - {line_amount}], [bold red]q[/bold red] to cancel", False)
        
        if line_number.lower() == "q":
            return False

        if not line_number.isdigit():
            console.print_message("Only numbers! Use [bold red]q[/bold red] to cancel operation")
            continue
        
        line_number = int(line_number)
        
        if line_number > 0 and line_number <= line_amount:
            break
        else:
           console.print_message(f"[yellow]Line must be between 1 and {line_amount}[/yellow]") 
    
    
    while True:
        console.print_styled_message(
            content[line_number - 1],
            f"Content of line N{line_number}",
            True,
            "cyan",
            expand=True,
            subtitle="[subtle]Edit mode[/subtle]"
        )

        new_text_input = console.show_basic_text_input("[bold]Text to insert (replace the selected line)[/bold]\n" \
        "[dim] You can cancel with the command [red]:q + Enter[/red][/dim]")

        if new_text_input[:2].lower() == ":q":
            console.print_message("[bold cyan]Operation cancelled, no changes were made[/bold cyan]")
            return False

        console.print_styled_message(
            content[line_number - 1],
            "OLD CONTENT",
            True,
            "red",
            True
        )

        console.print_styled_message(
            new_text_input,
            "NEW CONTENT",
            False,
            "green",
            True
        )

        console.print_message("Select an option\n1. [green]Save changes[/green]\n2. [yellow]Continue editing[/yellow]\n3. [red]Discard changes and exit[/red]")
        final_action = console.show_prompt("[bold green]╰─❯[/bold green]",["1","2","3"], True)

        if final_action == "1":
            content[line_number - 1] = new_text_input
            return True
        elif final_action == "2":
            continue
        else:
            return False