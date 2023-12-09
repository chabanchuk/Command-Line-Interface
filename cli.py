dict_contacts = {}


def input_error(func):
    def wrappper(*args):
        try:
            result = func(*args)
        except KeyError:
            return "Enter the command, name or phone number correctly."
        except ValueError:
            return "Enter the command, name or phone number correctly."
        except IndexError:
            return "Enter the command, name or phone number correctly."
        except TypeError:
            return "Enter the command, name or phone number correctly."
        except Exception:
            return "Enter the command, name or phone number correctly."
        return result
    return wrappper


@input_error
def bot_hello():
    return "How can I help you?"


@input_error
def bot_add_contact(name, phone_number):
    if name.isdigit():
        raise ValueError
    elif name not in dict_contacts:
        dict_contacts[name] = int(phone_number)
        return "Contact details saved."
    else:
        return "A contact with this name already exists."


@input_error
def bot_change_phone(name, new_phone_number):
    if name in dict_contacts:
        dict_contacts[name] = int(new_phone_number)
        return f"Phone number for {name} changed to {new_phone_number}."
    else:
        return "Contact with this name does not exist."


@input_error
def bot_get_phone(name):
    if name in dict_contacts:
        return dict_contacts[name]
    else:
        return "Contact with this name does not exist."


@input_error
def bot_show_all():
    if not dict_contacts:
        return "The contact list is empty."
    else:
        return "\n".join([f"Name: {name}, Phone: {phone}"
                          for name, phone in dict_contacts.items()])


@input_error
def bot_exit():
    return "Good bye!"


@input_error
def bot_check_command():
    raise ValueError


@input_error
def main():
    handler = {
        "hello": bot_hello,
        "add": bot_add_contact,
        "change": bot_change_phone,
        "phone": bot_get_phone,
        "show all": bot_show_all,
        "good bye": bot_exit,
        "close": bot_exit,
        "exit": bot_exit
    }
    while True:
        user_input = input(">>> ").lower()
        args = user_input.split()

        if len(args) > 1 and f"{args[0]} {args[1]}" in handler:
            handler_name = f"{args[0]} {args[1]}"
            args = args[2:]
        else:
            handler_name = args[0]
            args = args[1:]

        if handler_name not in handler:
            result = bot_check_command()
            print(result)
        else:
            result = handler[handler_name](*args)
            print(result)

        if result == "Good bye!":
            break


if __name__ == "__main__":
    main()
