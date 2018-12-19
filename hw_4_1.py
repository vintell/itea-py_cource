import string

def clear_word(word, filterstr):
    """
    Clean up string
    :param word:
    :param filterstr:
    :return:
    """
    check_str = string.punctuation + string.whitespace + string.digits + string.ascii_letters
    result = word
    i = 0
    while i < len(word):
        if word[i] not in check_str:
            raise ValueError(word[i], i)
        elif word[i] in filterstr:
            result = result.replace(word[i], '')
            i += 1
        else:
            i += 1
            continue
    return result


if __name__ == "__main__":
    entered_string = 's0me ,/!string'
    exception_str = ',!/'
    print('Исправленный текст:',clear_word(entered_string, exception_str))
