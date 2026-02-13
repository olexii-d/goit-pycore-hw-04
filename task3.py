import sys
from pathlib import Path

from colorama import Fore, Style, init


def print_tree(path: Path, prefix: str = "") -> None:
    """Рекурсивно друкує структуру директорії."""
    items = sorted(path.iterdir(), key=lambda p: (p.is_file(), p.name.lower()))

    for index, item in enumerate(items):
        is_last = index == len(items) - 1
        branch = "└── " if is_last else "├── "
        next_prefix = prefix + ("    " if is_last else "│   ")

        if item.is_dir():
            print(prefix + branch + Fore.CYAN + item.name + Style.RESET_ALL)
            print_tree(item, next_prefix)
        else:
            print(prefix + branch + Fore.GREEN + item.name + Style.RESET_ALL)


def main() -> None:
    init(autoreset=True)

    if len(sys.argv) != 2:
        print("Використання: python task3.py /шлях/до/директорії")
        sys.exit(1)

    dir_path = Path(sys.argv[1])

    if not dir_path.exists():
        print(Fore.RED + f"Помилка: шлях не існує -> {dir_path}")
        sys.exit(1)

    if not dir_path.is_dir():
        print(Fore.RED + f"Помилка: це не директорія -> {dir_path}")
        sys.exit(1)

    print(Fore.MAGENTA + f"📦 {dir_path.name}" + Style.RESET_ALL)
    print_tree(dir_path)


if __name__ == "__main__":
    main()
