def print_list_items(list, ends_with_nl):
    for index, item in enumerate(list):
        text = f"{index + 1}. {item}"

        if ends_with_nl is True:
            print(text, end="")
        else:
            print(text)

def should_disable_add_button(add_button, values):
    if (len(values["item"]) > 0):
        add_button.update(disabled=False)
        return False
    else:
        add_button.update(disabled=True)
        return True

def should_disable_edit_button(edit_button, values):
    if (len(values["item"]) > 0
        and (values['items'] and len(values['items'][0]) > 0)):
        edit_button.update(disabled=False)
        return False
    else:
        edit_button.update(disabled=True)
        return True
    