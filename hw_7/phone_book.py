contact_list = [{"name": "sss", "phone": "2222"}, {"name": "ddd", "phone": "2222"}]


def make_contact():
    name = input("Please add a name: ")
    phone = input("Please add a phone number: ")
    new_contact = {"name": name, "phone": int(phone)}
    print(f"Make_contact {new_contact}")
    return new_contact


def find_name_in_pb(contact_name):
    for contact in contact_list:
        if contact["name"] == contact_name:
            return contact


def check_for_duplicate(contact: dict):
    new_contact_name = contact.get("name")
    if find_name_in_pb(new_contact_name):
        print(f"This name => {new_contact_name},  is already in your contact list try another contact name")
        exit()
    else:
        print("Contact is unique")
        return True


def add_new_contact(contact: dict):
    contact_list.append(contact)
    print(f"Contact was added => {contact}")
    return contact_list


def delete_contact_by_name(contact_name):
    contact = find_name_in_pb(contact_name)
    if contact is not None:
        print(f"I found this contact and deleted them")
        contact_list.remove(contact)
        return contact_list
    else:
        print("I dont find this contact in yore phone book")
        exit()


def show_contact_by_name(contact_name):
    contact = find_name_in_pb(contact_name)
    if contact is not None:
        print(f"This is contact that you search: \n {contact}")
        exit()
    else:
        print("I dont find this contact in yore phone book")
        exit()


def list_all_contacts():
    for contact in contact_list:
        contact_name = contact.get("name")
        contact_phone = contact.get("phone")
        print(f"name: {contact_name}, phone: {contact_phone}")
    exit()


def work_with_phone_book():
    print("Hi my phone book can: \n",
          "- add contact           => Add \n",
          "- delete a contact      => Delete <name> \n",
          "- Show contact details  => Show <name> \n",
          "- get number of contact => stats \n",
          "- list all contacts     => list \n",
          )

    cmd = input("Enter your command: ")
    command = cmd.lower()
    if command == "add":
        new_contact = make_contact()
        if check_for_duplicate(new_contact) is not None:
            return add_new_contact(new_contact)
    elif command == "delete":
        contact_name_to_delete = input("Which contact do you want to delete?: ")
        return delete_contact_by_name(contact_name_to_delete)
    elif command == "show":
        contact_name = input("Which contact do you want to find?: ")
        show_contact_by_name(contact_name)
    elif command == "stats":
        length = lambda x: len(contact_list)
        return print(f"Your phone book have {length} contacts")
    elif command == "list":
        list_all_contacts()
    else:
        print(f"I don't know this command => {command}")


# print(make_contact())
print(work_with_phone_book())

# print(add_new_contact(check_for_duplicate(make_contact())))