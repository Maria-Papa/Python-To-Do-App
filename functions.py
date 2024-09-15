import array
from PySimpleGUI import Listbox
from helpers import print_list_items
from variables import red, green, no_color, help_text

def print_help(need_help):
    """ Print help for the commands. """
    need_help = need_help.lower().strip()

    match need_help:
        case "y" | "yes":
            for value in help_text.values():
                print("*", value)

def read_items(file_path):
    """ Get a list of the items in the txt file. """
    try:
        with open(file_path, "r") as file:
            items = file.readlines()
        return items
    except FileNotFoundError:
        print(f"{red}File NOT found!{no_color}")


def write_items(file_path, lines):
    """ Write the given lines to the txt file. """
    with open(file_path, "w") as file:
        file.writelines(lines)


def add_item(file_path, item):
    """ Add an item to the items list in the txt file. """
    lines = read_items(file_path)

    # TODO: If file not found, create it

    lines.append(item + "\n")
    write_items(file_path, lines)

    print(f"{green}Item [{item}] is added to the list!{no_color}")


def show_list(file_path):
    """ Print the shopping list from the txt file
    in the format ofprint_list_items function. """
    # try:
    items = read_items(file_path)

    print("Your current shopping list is:")
    print("==============================")
    
    print_list_items(items, True)

    print("==============================")
    # except FileNotFoundError:
    #     print(f"{red}File NOT found!{no_color}")


def edit_item(file_path, old_item, new_item) -> array:
    """ Edit an item in the txt file. """
    lines = read_items(file_path)
    index = lines.index(old_item)

    lines[index] = new_item + "\n"

    write_items(file_path, lines)
    print(f"{green}Item [{old_item.strip()}] was changed to [{new_item}]{no_color}")

    return lines


def check_off_item(file_path, index):
    """ Remove an item from the txt file. """
    lines = read_items(file_path)

    checked_off_item = lines[index].strip("\n")
    lines.pop(index)

    write_items(file_path, lines)
    print(f"{green}Item [{checked_off_item}] has been checked off.{no_color}")


def refresh_list(shopping_list: str, list_box: Listbox, auto_scroll_down = True, items = []) -> None:
    """Refresh the given listbox element.

    Args:
        shopping_list (str): The shopping list txt file name.
        list_box (Listbox): The Listbox Element.
        auto_scroll_down (bool): Whether to auto scroll down inside the given Listbox Element.
            (default is True)
        items (array): The items of the Listbox Element.
            (default is [])

    Returns:
        None
    """
    if (not items):
        items = read_items(shopping_list)

    list_box.update(values=items)

    if (auto_scroll_down):
        list_box.set_vscroll_position(1.0)
