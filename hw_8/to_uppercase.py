text_example = "This is an example sentence written in lowercase"


def letter_to_uppercase(elm):
    if elm.isupper():
        return elm
    else:
        return elm.upper()


def sentence_to_uppercase(snt):
    print(snt)
    upper_text_example = ""
    for e in map(letter_to_uppercase, snt):
        upper_text_example = upper_text_example + e
    return print(upper_text_example)


sentence_to_uppercase(text_example)
