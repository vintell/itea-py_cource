"""
$id=20181212

"""
from pyca import *


def choose_operation(operations_list):
    """
    User can choose an operation from the regular list.
    :param operations_list: list
    :return: None or Operation name
    """
    print('What kind opratation from the list you choose:')
    i, entered = 0, ''
    for item in operations_list:
        i += 1
        print('{}: {}'.format(i, item))

    while True:
        entered = input('Enter number in the list or type operation or type \'stop\' for terminate: ').strip()
        if entered.lower() == 'stop':
            return
        elif entered.isnumeric() and 0 <= int(entered) - 1 < i:
            i = 0
            entered = int(entered)
            for item in operations_list:
                i += 1
                if entered == i:
                    return item
        elif entered in operations_list:
            return entered
        else:
            print('Unsupported operation. Try again...')


def two_params(vars=['variable#1', 'variable#2'], min_value=None, max_value=None):
    """
    Collect two variables from user.
    :param min_value:
    :param max_value:
    :return: None or {}
    """
    variables = []
    for item in vars:
        variable = one_param(item, min_value, max_value)
        # terminate program
        if variable is None:
            return
            # set value
        variables.append(variable)
    return variables


def one_param(name, min_value=None, max_value=None):
    """
    Collect one variable from user.
    :param name: name of variable
    :param min_value: limitation for minimum value
    :param max_value: limitation for maximum value
    :return: None or Float
    """
    if min_value is not None and max_value is not None:
        print('This variable has limitation: {}>= {} <={}'.format(min_value, name, max_value))
    elif min_value is not None:
        print('This variable has limitation: {}>= {}'.format(min_value, name))
    elif max_value is not None:
        print('This variable has limitation: {}<= {}'.format(name, max_value))

    while True:
        entered = input('Enter number for {} or type \'stop\' for terminate: '.format(name)).strip()
        if entered.replace('.', '').isnumeric() and entered.count('.') <= 1:
            entered = float(entered)
            if min_value is None and max_value is None:
                return cast_to_int(entered)
            elif min_value is not None and max_value is not None and min_value >= entered <= max_value:
                return cast_to_int(entered)
            elif min_value is not None and min_value >= entered:
                return cast_to_int(entered)
            elif max_value is not None and entered <= max_value:
                return cast_to_int(entered)
        elif entered.lower() == 'stop':
            return
        else:
            print('You have entered wrong value. Try again..')


def cast_to_int(value):
    try:
        int_value = int(value)
        if value == int_value:
            return int_value
        elif value % int_value == 0:
            return int_value
        else:
            return value
    except:
        return value


if __name__ == '__main__':

    print("""
    ___________________________________________________________________
    This program work with simple operations of python likes on:
    LOGICAL NAME    | OPERATION
    plus            | +
    minus           | - 
    divide          | /
    multiplication  | *
    power           | ^ or **
    Priorities doesn't work on this program.  
    So begin.....
    ___________________________________________________________________  
    """)

    # init
    result = None
    operations = {
        # 'multiplication': multi,
        '*': multi,

        # 'divide': divide,
        '/': divide,
        '%': modulus,

        # 'power': power,
        # '**': power,
        '^': power,

        # 'minus': minus,
        '-': minus,
        # 'plus': plus,
        '+': plus,
        'sin': sin,
        'cos': cos
    }
    while True:
        operation_choosed = choose_operation(operations.keys())
        #  is terminate or not
        if operation_choosed is None:
            break
        else:
            print('DOC:')
            print(operations[operation_choosed].__doc__)
        if operation_choosed in ['cos', 'sin']:
            variable = one_param('"Angle in degrees"', 0, 360)
            if variable is None:
                break
            result = cast_to_int(operations[operation_choosed](variable))
            result = 'YOUR ANSWER IS: {}({}) = {}'.format(operation_choosed, variable, result)
        else:

            variables = two_params(['"variable"', '"power"'] \
                                       if operation_choosed in ['^', '**', 'power'] else \
                                       ['"variable#1"', '"variable#2"'])
            try:
                result = cast_to_int(operations[operation_choosed](variables[0], variables[1]))
                result = 'YOUR ANSWER IS: {} {} {} = {}'.format(variables[0], operation_choosed, variables[1], result)
            except Exception as e:
                print(e)
                continue

        if result is None:
            break
        else:
            print(result)
        print()
        print()
