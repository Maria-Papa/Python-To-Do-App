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
    need_help = need_help.lower().strip()

    match need_help:
        case "y" | "yes":
            for value in help_text.values():
                print("*", value)

def add_item(file_name, item):
    with open(file_name, "a+") as file:
        lines = file.readlines()
        lines.append(item + "\n")
        file.writelines(lines)

    print(f"{green}Item [{item}] is added to the list!{no_color}")

def show_list(file_name):
    try:
        print("Your current shopping list is:")
        print("==============================")

        with open(file_name, "r") as file:
            lines = file.readlines()
        
        helpers.print_list_items(lines, True)

        print("==============================")
    except FileNotFoundError:
        print(f"{red}File NOT found!{no_color}")

def edit_item(file_name, index):
    with open(file_name, "r") as file:
        lines = file.readlines()

    old_item     = lines[index].strip("\n")
    new_item     = input("Enter new item: ")
    lines[index] = new_item + "\n"

    with open(file_name, "w") as file:
        file.writelines(lines)

    print(f"{green}Item [{old_item}] was changed to [{new_item}]{no_color}")

def check_off_item(file_name, index):
    with open(file_name, "r") as file:
        lines = file.readlines()

    checked_off_item = lines[index].strip("\n")
    lines.pop(index)

    with open(file_name, "w") as file:
        file.writelines(lines)

    print(f"{green}Item [{checked_off_item}] has been checked off.{no_color}")

############### CODE ################
# print("Welcome to your shopping list!")
# need_help = input("Do you need help? (y/n) ")
# print_help(need_help)

file_path = "files/shopping_list.txt"

while True:
        user_action = input("What would you like to do? ")
        user_action = user_action.strip()

        if user_action.startswith("add"):
            item = user_action[4:]
            add_item(file_path, item)
            show_list(file_path)

        elif user_action.startswith("show"):
            show_list(file_path)

        elif user_action.startswith("edit"):
            try:
                index = int(user_action[5:])
                index = index - 1
                edit_item(file_path, index)
            except ValueError:
                print(f"{yellow}This command is not valid.{no_color}")
                print(f"{yellow}Help --> {help_text['edit']}{no_color}")
                continue
            except IndexError:
                print(f"{yellow}There is no item in the list with this number.{no_color}")
                print(f"{yellow}Please check again.{no_color}")
                show_list(file_path)
                continue

        elif user_action.startswith("check off"):
            try:
                index = int(user_action[10:])
                index = index - 1
                check_off_item(file_path, index)
            except IndexError:
                print(f"{yellow}There is no item in the list with this number.{no_color}")
                print(f"{yellow}Please check again.{no_color}")
                show_list(file_path)
                continue

        elif user_action.startswith("help"):
            print_help("yes")

        elif user_action.startswith("exit"):
            break

        else:
            print("You entered an unknown command. \nPlease enter one of the following: add, show, edit, check off, help, exit.")
             
print("Bye!")
