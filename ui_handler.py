import keyboard

options = [
    "Add Transaction",
    "Edit Transaction",
    "All Transactions",
    "Statistics",
    "Generate a Report",
    "Exit",
    ]

def print_menu(pointer_position):
    for i, option in enumerate(options):
        prefix = "> " if i == pointer_position else "  "
        print(prefix + option)
    print("\nUse ↑ ↓ to navigate, Enter to select.")

def menu(pointer_position):
    print_menu(pointer_position)
    while True:
        key_event = keyboard.read_event(suppress=True)

        if key_event.event_type == keyboard.KEY_UP:
            if key_event.name == "up":
                pointer_position = (pointer_position - 1) % len(options)
            elif key_event.name == "down":
                pointer_position = (pointer_position + 1) % len(options)
            print("\033c", end="")
            print_menu(pointer_position)
        elif key_event.event_type == keyboard.KEY_DOWN:
            if key_event.name == "enter":
                return pointer_position


def greet():
    print("Welcome! I am your Personal Finance Tracker & Budget Assistant.")

def farewell():
    print("I'll see you next time!")