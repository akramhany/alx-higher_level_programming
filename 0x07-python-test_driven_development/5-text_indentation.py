#!/usr/bin/python3

""" this module would contain the answer for task 4 in ALX """


def text_indentation(text):
    """
    Takes text and splits it over '.', '?', ':' and remove trailing white
    spaces
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    list_of_sen = []
    sent = ""
    for it in range(len(text)):
        sent += text[it]
        if text[it] == '.' or text[it] == '?' or text[it] == ':':
            list_of_sen.append(sent)
            sent = ""

    for sen in list_of_sen:
        print(sen.strip())
        print()

    if len(sent) > 0:
        print(sent.strip(), end='')
