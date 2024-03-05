def print_list_items(list, ends_with_nl):
    for index, item in enumerate(list):
        text = f"{index + 1}. {item}"

        if ends_with_nl is True:
            print(text, end="")
        else:
            print(text)
