import PySimpleGUI as sg
from functions import add_item, edit_item, read_items, refresh_list
from helpers import should_disable_add_button, should_disable_edit_button
from variables import shopping_list

label       = sg.Text("List an item")
input_box   = sg.Input(tooltip="Enter item", key="item", enable_events=True)
list_box    = sg.Listbox(values=read_items(shopping_list), key="items", enable_events=True, size=[45, 10])
add_button  = sg.Button("Add", disabled=True)
edit_button = sg.Button("Edit", disabled=True)
exit_button = sg.Button("Exit")

window = sg.Window("My Shopping List",
                   layout=[[label], [input_box, add_button], [list_box, edit_button], [exit_button]],
                   font=("Helvetica", 20))


while True:
    event, values = window.read()

    match event:
        case "Add":
            if (not should_disable_add_button(add_button, values)):
                add_item(shopping_list, values["item"])
                refresh_list(shopping_list, list_box, True)
        case "Edit":
            if (not should_disable_edit_button(edit_button, values)):
                old_item = values["items"][0]
                new_item = values["item"]

                items = edit_item(shopping_list, old_item, new_item)

                refresh_list(shopping_list, list_box, False, items)
        case "items" | "item":
            should_disable_add_button(add_button, values)
            should_disable_edit_button(edit_button, values)
        case sg.WIN_CLOSED | "Exit":
            break

window.close()
