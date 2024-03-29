from tabulate import tabulate
import json
import os
import time


class MyCustomException(Exception):
    log_file = "fixture/exception.log"

    if not os.path.exists(log_file):
        with open(log_file, "w") as file:
            print(f"{time.asctime()} ====> {Exception.__cause__}", file=file)
    else:
        with open(log_file, "a") as file:
            print(f"{time.asctime()} ====> {Exception.__cause__}", file=file)


def launch_logging(func):
    log_file = "fixture/launch.log"

    def wrapper(*args, **kwargs):
        if not os.path.exists(log_file):
            with open(log_file, "w") as file:
                print(f"{time.asctime()} ====> {func.__name__}", file=file)
        else:
            with open(log_file, "a") as file:
                print(f"{time.asctime()} ====> {func.__name__}", file=file)
        result = func(*args, **kwargs)
        return result

    return wrapper


@launch_logging
def add_contact_list() -> list:
    try:
        with open("fixture/phone_book.json", "r") as file:
            f = file.read()
            return json.loads(f)
    except FileNotFoundError as e:
        print(e)
        with open("fixture/phone_book.json", "w") as file:
            file.write("[]")
        with open("fixture/phone_book.json", "r") as file:
            f = file.read()
        return json.loads(f)


contact_list = add_contact_list()
print(contact_list)


@launch_logging
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


@launch_logging
def find_name_in_pb(contact_name: str) -> dict:
    check_len = check_contact_list_length()
    if check_len > 0:
        for contact in contact_list:
            try:
                if contact["name"] == contact_name:
                    return contact
            except TypeError as e:
                print(e)
    else:
        print(f"You don't have any contacts")


@launch_logging
def check_for_duplicate(contact: dict) -> bool:
    try:
        new_contact_name = contact.get("name")
        if find_name_in_pb(new_contact_name):
            print(f"\nThis name => {new_contact_name},  is already in your contact list try another contact name")
            return False
        else:
            print("\nContact is unique")
            return True
    except AttributeError as e:
        print(e)


@launch_logging
def add_new_contact(contact: dict):
    if check_for_duplicate(contact):
        if contact is not None:
            try:
                contact_list.append(contact)
                print(f"\nContact was added => {contact}")
                return True
            except AttributeError as e:
                print(e)
        else:
            print("\nContact couldn't be created")
            return False


@launch_logging
def delete_contact_by_name(contact_name: str) -> bool:
    contact = find_name_in_pb(contact_name)
    if contact is not None:
        print(f"\nI found this contact and deleted them")
        contact_list.remove(contact)
        return True
    else:
        print("\nI dont find this contact in yore phone book")
        return False


@launch_logging
def show_contact_by_name(contact_name):
    contact = find_name_in_pb(contact_name)
    if contact is not None:
        print(f"\nThis is contact that you search: \n {contact}")
    else:
        print("\nI dont find this contact in yore phone book")


@launch_logging
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


@launch_logging
def check_contact_list_length():
    try:
        cnt_len = len(contact_list)
    except TypeError as e:
        print(f"\nContact list doesn't exist. \n {e}")
    else:
        return cnt_len


@launch_logging
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
        with open("fixture/phone_book.json", "w") as file:
            f = json.dumps(contact_list, indent=4)
            file.write(f)


work_with_phone_book()
