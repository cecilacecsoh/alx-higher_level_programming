#!/usr/bin/python3

"""
    5-text_indentation Module task
"""


def text_indentation(text):
    """
        It prints a text with 2 new lines after each of this characters
        '.', '?', ':'

        Args:
            text: the inital string
    """
    if type(text) is not str:
        raise TypeError("the text must be a string")

    split_texts_list = list()
    new_texts = list()
    letters_list = list()

    for character in text:
        letters_list.append(character)
        if character in ['.', '?', ':']:
            split_texts_list.append(''.join(letters_list))
            letters_list.clear()

    if letters_list:
        split_texts_list.append("".join(letters_list))
    letters_list.clear()

    for sentence in split_texts_list:
        new_texts.append(sentence.strip(' '))
    split_texts_list.clear()

    for character in new_texts[-1]:
        if character in ['.', '?', ':']:
            print("\n\n".join(new_texts))
            print()
            return

    print("\n\n".join(new_texts), end='')
