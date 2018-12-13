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
        # in some cases its bug. e.g. #it's an apple# acceptable, but #company ''Vivo''# or #Мар''яна# its a bug
        if i != "'":
            input_text = input_text.replace(i, "")
    return input_text


def enter_str(text='Enter fraze or enter Space+Enter for exit: ', is_break_it=True ):
    """
    Return entered text
    :return: None or str
    """
    while True:
        # entered_value = 'SOme text entered here. AdD my  value again and     again .' # unit test
        entered_value = input(text)
        if entered_value == ' ' and is_break_it:
            print('Application stopped.')
            return
        else:
            return entered_value

def set_empty_i8(word_name):
    str = ''
    while str == '':
        str = enter_str('Insert translation for word "{}": '.format(word_name), False).strip()
    return str

def list_empty_i8(dictionary):
    """

    :param dictionary:
    :return:
    """
    result = dict()
    str = ''
    for item in dictionary.keys():
        if dictionary[item] is None:
            result[item] = set_empty_i8(item)

    # print(result)

    return result


def get_dictionary_from_list(list_of_words):
    """
    Return dictionary where words is a key and count as value
    :param list_of_words:
    :return: dict
    """
    dict_of_words = {}.fromkeys(list_of_words, None)
    # for item in list_of_words:
    #     if dict_of_words[item] is None:
    #         dict_of_words[item] = None
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


def print_table(dict_of_words):
    """
    Print table with statistic
    :param dict_of_words:
    :return:
    """

    """ 
    Variables
    word is word in dictionary
    i8 is transtation to another language
    """
    max_len_word = max_length_for_list_items(dict_of_words.keys())
    max_len_i8 = max_length_for_list_items(dict_of_words.values())
    # Header
    print('|-{}----{}-|'.format('-' * max_len_word, '-' * max_len_i8))
    for word in dict_of_words:
        # Format Each line
        len_word = max_len_word - len(word)
        len_i8 = max_len_i8 - len(str(dict_of_words[word]))
        i8 = dict_of_words[word]
        print('| {}{} => {}{} |'.format(word, ' ' * len_word, ' ' * len_i8, i8))
    # footer
    print('|-{}----{}-|'.format('-' * max_len_word, '-' * max_len_i8))


print("""
__________________________________________________________________________
This program is store all WORDS in phrase and asking you about translation
 an another language.
So begin.....
____________________________________________________________________  
""")

entered_string = ''
clean_string = ''
dictionary = dict()

while True:
    entered_string = enter_str()
    if entered_string is None:
        break
    elif entered_string.strip() == '':
        print('Entered zero length string. Try again.')
    else:
        clean_string += ' ' + punctuation_strip(entered_string.lower())
        stat = get_dictionary_from_list(clean_string.split(' '))
        # delete all double spaces
        stat[''] = None
        stat.pop('')
        stat = dict(stat)
        stat.update(dictionary)
        dictionary.update(list_empty_i8(stat))
        print_table(dictionary)

