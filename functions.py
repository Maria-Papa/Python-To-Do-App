import helpers
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
    
    helpers.print_list_items(items, True)

    print("==============================")
    # except FileNotFoundError:
    #     print(f"{red}File NOT found!{no_color}")


def edit_item(file_path, index):
    """ Edit an item in the txt file. """
    lines = read_items(file_path)

    old_item     = lines[index].strip("\n")
    new_item     = input("Enter new item: ")
    lines[index] = new_item + "\n"

    write_items(file_path, lines)
    print(f"{green}Item [{old_item}] was changed to [{new_item}]{no_color}")


def check_off_item(file_path, index):
    """ Remove an item from the txt file. """
    lines = read_items(file_path)

    checked_off_item = lines[index].strip("\n")
    lines.pop(index)

    write_items(file_path, lines)
    print(f"{green}Item [{checked_off_item}] has been checked off.{no_color}")
