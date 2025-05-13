def print_colored(text, color="white"):
    colors = {
        "grey": "\033[90m", "red": "\033[91m", "green": "\033[92m",
        "yellow": "\033[93m", "blue": "\033[94m", "magenta": "\033[95m",
        "cyan": "\033[96m", "white": "\033[97m", "reset": "\033[0m"
    }
    print(f"{colors.get(color, colors['white'])}{text}{colors['reset']}")
