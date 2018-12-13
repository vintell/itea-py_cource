"""
in test
Statistic of the words
"""

import string


def punctuation_strip(input_text):
    """
    Return only "words"
    :param input_text:
    :return:
    """
    for i in string.punctuation:
        # in some cases its bug. e.g. #it's an apple# acceptable, but #company ''Vivo''# its a bug
        if i != "'":
            input_text = input_text.replace(i, "")
    return input_text


def enter_str():
    """
    Return entered text
    :return: None or str
    """
    while True:
        print('All entered data are stored for next iteration.')
        entered_value = input('Enter phrase or enter Space+Enter for exit: ')
        if entered_value == ' ':
            print('Application stopped.')
            return
        else:
            return entered_value


def get_dictionary_from_list(list_of_words):
    """
    Return dictionary where words is a key and count as value
    :param list_of_words:
    :return: dict
    """
    dict_of_words = {}.fromkeys(list_of_words, 0)
    for item in list_of_words:
        dict_of_words[item] += 1
    return dict_of_words


def max_length_for_list_items(list_of):
    """
    Get max len for all item of the list
    :param list_of:
    :return:
    """
    lengths = []

    for item in list_of:
        if type(item) != type(str()):
            lengths.append(len(str(item)))
        else:
            lengths.append(len(item))
    return max(lengths)


def print_stat(dict_of_words):
    """
    Print table with statistic
    :param dict_of_words:
    :return:
    """
    max_len_word = max_length_for_list_items(dict_of_words.keys())
    tmp_list = []
    for word in dict_of_words.keys():
        for _ in range(dict_of_words[word]):
            tmp_list.append(word)

    tmp_list.sort()
    # Header
    print('|-{}-|'.format('-' * max_len_word))
    tmp_list = list(dict_of_words.keys())
    # list can be sorted only with several items
    if tmp_list.__len__() > 1:
        tmp_list.sort()

    for word in tmp_list:
        # Format Each line
        len_word = max_len_word - len(word)
        cnt = dict_of_words[word]
        print('| {}{} |'.format(word, ' ' * len_word))
    # footer
    print('|-{}-|'.format('-' * max_len_word))


print("""
____________________________________________________________________
This program is store all WORDS and show them all.
 List sorted by ABC.
So begin.....
____________________________________________________________________  
""")

entered_string = ''
clean_string = ''
while True:
    entered_string = enter_str()
    if entered_string is None:
        break
    elif entered_string.strip() == '':
        print('Entered zero length string')
    else:
        clean_string += ' ' + punctuation_strip(entered_string.lower())
        # print(entered_string) # unit test
        stat = get_dictionary_from_list(clean_string.split(' '))
        # delete all double spaces
        stat[''] = 0
        stat.pop('')
        print_stat(dict(stat))
        # break # unit test
