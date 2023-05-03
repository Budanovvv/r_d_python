import re


def replace_all_emails_in_file_on_mask():
    file_name = input("Enter file name: ")

    try:
        with open(file_name, 'r') as f:
            text = f.read()
    except Exception as e:
        print(e)

    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    result = re.sub(pattern, '*@*', text)
    return result


print(replace_all_emails_in_file_on_mask())
