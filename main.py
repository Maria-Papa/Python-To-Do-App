############## IMPORTS ##############
import helpers

############# VARIABLES #############
red      = "\033[1;31m"
green    = "\033[1;32m"
yellow   = "\033[1;33m"
no_color = "\033[0m"

help_text = {
    "add"      : "Enter 'add [list item]' to add an item to the list.",
    "show"     : "Enter 'show' to see all the items of the list.",
    "edit"     : "Enter 'edit [item number]' to edit an item of the list.",
    "check off": "Enter 'check off [item number]' to check an item off the list.",
    "help"     : "Enter 'help' to get help about the commands.",
    "exit"     : "Enter 'exit' to exit the list."
}

############# FUNCTIONS #############
def print_help(need_help):
    """ TEST """
    need_help = need_help.lower().strip()

    match need_help:
        case "y" | "yes":
            for value in help_text.values():
                print("*", value)

def read_items(file_path):
    try:
        with open(file_path, "r") as file:
            items = file.readlines()
        return items
    except FileNotFoundError:
        print(f"{red}File NOT found!{no_color}")


def write_items(file_path, lines):
    with open(file_path, "w") as file:
        file.writelines(lines)


def add_item(file_path, item):
    lines = read_items(file_path)

    lines.append(item + "\n")
    write_items(file_path, lines)

    print(f"{green}Item [{item}] is added to the list!{no_color}")


def show_list(file_path):
    # try:
    items = read_items(file_path)

    print("Your current shopping list is:")
    print("==============================")
    
    helpers.print_list_items(items, True)

    print("==============================")
    # except FileNotFoundError:
    #     print(f"{red}File NOT found!{no_color}")


def edit_item(file_path, index):
    lines = read_items(file_path)

    old_item     = lines[index].strip("\n")
    new_item     = input("Enter new item: ")
    lines[index] = new_item + "\n"

    write_items(file_path, lines)
    print(f"{green}Item [{old_item}] was changed to [{new_item}]{no_color}")


def check_off_item(file_path, index):
    lines = read_items(file_path)

    checked_off_item = lines[index].strip("\n")
    lines.pop(index)

    write_items(file_path, lines)
    print(f"{green}Item [{checked_off_item}] has been checked off.{no_color}")


############### CODE ################
# print("Welcome to your shopping list!")
# need_help = input("Do you need help? (y/n) ")
# print_help(need_help)

shopping_list = "files/shopping_list.txt"

while True:
        user_action = input("What would you like to do? ")
        user_action = user_action.strip()

        if user_action.startswith("add"):
            item = user_action[4:]
            add_item(shopping_list, item)
            show_list(shopping_list)

        elif user_action.startswith("show"):
            show_list(shopping_list)

        elif user_action.startswith("edit"):
            try:
                index = int(user_action[5:])
                index = index - 1
                edit_item(shopping_list, index)
            except ValueError:
                print(f"{yellow}This command is not valid.{no_color}")
                print(f"{yellow}Help --> {help_text['edit']}{no_color}")
                continue
            except IndexError:
                print(f"{yellow}There is no item in the list with this number.{no_color}")
                print(f"{yellow}Please check again.{no_color}")
                show_list(shopping_list)
                continue

        elif user_action.startswith("check off"):
            try:
                index = int(user_action[10:])
                index = index - 1
                check_off_item(shopping_list, index)
            except IndexError:
                print(f"{yellow}There is no item in the list with this number.{no_color}")
                print(f"{yellow}Please check again.{no_color}")
                show_list(shopping_list)
                continue

        elif user_action.startswith("help"):
            print_help("yes")

        elif user_action.startswith("exit"):
            break

        else:
            print("You entered an unknown command. \nPlease enter one of the following: add, show, edit, check off, help, exit.")
             
print("Bye!")
