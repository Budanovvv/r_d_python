import re

file_name = input("Enter file name: ")
# fixture/rnd_contacts.txt

try:
    with open(file_name, 'r') as f:
        text = f.read()
except Exception as e:
    print(e)


def replace_all_emails_in_file_on_mask():

    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    return re.sub(pattern, '*@*', text)


def replace_email():

    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    new_text = text

    for match in re.finditer(pattern, text):
        email = match.group(0)
        first_char = email[0]
        last_char = email[-1]
        mask_email = f"{first_char}{'*' * 4}@{'*' * 4}{last_char}"
        new_text = new_text.replace(email, mask_email)
    return new_text


print(replace_all_emails_in_file_on_mask())
print(replace_email())

