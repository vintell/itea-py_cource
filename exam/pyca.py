from math import cos as mycos, sin as mysin

def plus(val_1, val_2):
    """
    This is calculate a sum for two params
    :param val_1: int or float
    :param val_2: int or float
    :return: int or float
    """
    return val_1 + val_2


def minus(val_1, val_2):
    """
    This is calculate a different for two params
    :param val_1: int or float
    :param val_2: int or float
    :return: int or float
    """
    return val_1 - val_2


def multi(val_1, val_2):
    """
    This is calculate multiplication of two params
    :param val_1: int or float
    :param val_2: int or float
    :return: int or float
    """
    return val_1 * val_2


def divide(val_1, val_2):
    """
    This is calculate a divide of two params
    :param val_1: int or float
    :param val_2: int or float
    :return: int or float or None
    """
    if val_2 == 0:
        raise ZeroDivisionError('{} / {} = {}'.format(val_1, val_2, 'division by zero error'))
    return val_1 / val_2


def power(value, power):
    """
    This is calculate a power
    :param value: int or float - number
    :param power: int or float - in power
    :return: int or float or None
    """
    return value ** power


def modulus(val_1, val_2):
    """
    This is calculate a divide of two params and return rest
    :param val_1: int or float
    :param val_2: int or float
    :return: int or float or None
    """
    if val_2 == 0:
        raise ZeroDivisionError('{} % {} = {}'.format(val_1, val_2, 'division by zero error'))
    return val_1 % val_2

def cos(var_1):
    """
    Return a Cosine for angle.
    :param var_1: int or float as "Angle in degrees"
    :return: int or float
    """
    return mycos(var_1)
def sin(var_1):
    """
    Return a Sine for angle.
    :param var_1: int or float as "Angle in degrees"
    :return: int or float
    """
    return mysin(var_1)
