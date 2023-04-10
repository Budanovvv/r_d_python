from tabulate import tabulate


class MyCustomException(Exception):
    pass


def add_contact_list(list=None):  # Add this like some function which should check and get some data for pb
    try:
        if list is None:
            raise MyCustomException("Custom exception is occurred")
    except MyCustomException as e:
        print(e)
    finally:
        if list is None:
            list = []
        return list


cnt_lst = [
    {"name": "sss", "phone": "2222"},
    {"name": "ddd", "phone": "2222"}
]

contact_list = add_contact_list(cnt_lst)


def make_contact(max_tries: int = 3) -> dict:
    name = ""
    phone = ""
    while max_tries >= 0:
        try:
            if name == "":
                name = input("Please add a name: ")
            if phone == "":
                phone = int(input("Please add a phone number: "))
            if not name:
                raise MyCustomException("Custom exception is occurred")
        except MyCustomException as e:
            print(e)
        except ValueError:
            print(f"\nPhone can contain only digits. You have {max_tries} tries")
        else:
            new_contact = {"name": name, "phone": phone}
            print(f"\nMake_contact {new_contact}")
        finally:
            if name and phone:
                return new_contact
            max_tries -= 1


def find_name_in_pb(contact_name: str) -> dict:
    check_len = check_contact_list_length()
    if check_len > 0:
        for contact in contact_list:
            if contact["name"] == contact_name:
                return contact
    else:
        print(f"You don't have any contacts")


def check_for_duplicate(contact: dict) -> bool:
    new_contact_name = contact.get("name")
    if find_name_in_pb(new_contact_name):
        print(f"\nThis name => {new_contact_name},  is already in your contact list try another contact name")
        return False
    else:
        print("\nContact is unique")
        return True


def add_new_contact(contact: dict):
    if check_for_duplicate(contact):
        if contact is not None:
            contact_list.append(contact)
            print(f"\nContact was added => {contact}")
            return True
        else:
            print("\nContact couldn't be created")
            return False


def delete_contact_by_name(contact_name: str) -> bool:
    contact = find_name_in_pb(contact_name)
    if contact is not None:
        print(f"\nI found this contact and deleted them")
        contact_list.remove(contact)
        return True
    else:
        print("\nI dont find this contact in yore phone book")
        return False


def show_contact_by_name(contact_name):
    contact = find_name_in_pb(contact_name)
    if contact is not None:
        print(f"\nThis is contact that you search: \n {contact}")
    else:
        print("\nI dont find this contact in yore phone book")


def list_all_contacts():
    check_len = check_contact_list_length()
    if check_len > 0:
        print(tabulate(contact_list, headers="keys"))
        # for contact in contact_list:
        #     contact_name = contact.get("name")
        #     contact_phone = contact.get("phone")
        #     print(f"name: {contact_name}, phone: {contact_phone}")
    else:
        print(f"\nYou don't have any contacts")


def check_contact_list_length():
    try:
        cnt_len = len(contact_list)
    except TypeError as e:
        print(f"\nContact list doesn't exist. \n {e}")
    else:
        return cnt_len


def work_with_phone_book():
    print("Hi my phone book can: \n",
          "- add contact           => Add \n",
          "- delete a contact      => Delete <name> \n",
          "- Show contact details  => Show <name> \n",
          "- get number of contact => Stats \n",
          "- list all contacts     => List \n",
          "- Stop working          => Stop \n",
          "- Helper                => Help \n",
          )

    while True:
        cmd = input("Enter your command: ")
        command = cmd.lower()
        if command == "add":
            new_contact = make_contact()
            if not contact_list:
                if check_for_duplicate(new_contact) is True:
                    add_new_contact(new_contact)
            else:
                add_new_contact(new_contact)
        elif command == "delete":
            contact_name_to_delete = input("Which contact do you want to delete?: ")
            delete_contact_by_name(contact_name_to_delete)
        elif command == "show":
            contact_name = input("Which contact do you want to find?: ")
            show_contact_by_name(contact_name)
        elif command == "stats":
            cnt_ln = check_contact_list_length()
            if cnt_ln is not None:
                print(f"\nYour phone book have {cnt_ln} contacts")
        elif command == "list":
            list_all_contacts()
        elif command == "Help":
            print(
                "- add contact           => Add \n",
                "- delete a contact      => Delete <name> \n",
                "- Show contact details  => Show <name> \n",
                "- get number of contact => Stats \n",
                "- list all contacts     => List \n",
                "- Stop working          => Stop \n",
                "- Helper                => Help \n",
            )
        elif command == "stop":
            break
        else:
            print(f"\nI don't know this command => {command}")


work_with_phone_book()
