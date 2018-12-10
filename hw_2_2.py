import math

def enter_val(name='value'):
    while True:
        entered_value = input('Enter {} or enter word \'stop\' for exit: '.format(name))
        if entered_value == 'stop':
            print('Application stopped.')
            return
        if entered_value.replace('.', '').isnumeric() and (entered_value.count('.') <= 1):
            if float(entered_value) < 0:
                print('You have enter unacceptable or negative value.')
            else:
                return entered_value
        else:
            print('You have enter wrong value.')


result = 0

print("""
    ####################################
    ### SUM of the natural values.   ###
    ####################################
""")

entered_value_a = enter_val('variable a')
entered_value_b = enter_val('variable b')

if entered_value_a and entered_value_b:

    entered_value_a = float(entered_value_a)
    entered_value_b = float(entered_value_b)

    if entered_value_a > entered_value_b:
        entered_value_a = entered_value_b + entered_value_a
        entered_value_b = entered_value_a - entered_value_b
        entered_value_a = entered_value_a - entered_value_b
    # fix on next line
    # was:    range(int(round(entered_value_a)), int(round(entered_value_b)) + 1)
    for iteration in range(int(math.ceil(entered_value_a)), int(entered_value_b) + 1):
        result += iteration
        print('iteration={} Result is {}'.format(iteration, result))
    else:
        print('Sequence till {} is factorial value is {}'.format(int(entered_value_b), result))
