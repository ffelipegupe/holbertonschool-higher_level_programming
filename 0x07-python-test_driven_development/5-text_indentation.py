#!/usr/bin/python3
"""
Text identation
"""


def text_indentation(text):
    """ function that prints a text with 2 new lines after each
    of these characters: ., ? and : """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    sentence = ""
    for i in text:
        if i == "\n":
            print(sentence)
            sentence = ""
            continue
        else:
            sentence += i
        if i == '.' or i == '?' or i == ':':
            sentence = sentence.strip(" ")
            print("{}".format(sentence), end ="")
            print("\n")
            sentence = ""
    sentence = sentence.strip(" ")
    print("{}".format(sentence), end="")


text_indentation(""" text indentation \n . here, ? :""")
