import time
from functions import print_help, add_item, show_list, edit_item, check_off_item
from variables import yellow, no_color, shopping_list, help_text

# print("Welcome to your shopping list!")
# need_help = input("Do you need help? (y/n) ")
# print_help(need_help)

today = time.strftime("%d-%m-%Y")
print(today)

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
