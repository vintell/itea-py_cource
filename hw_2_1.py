"""
    define function "Enter value"
"""


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
                return float(entered_value)
        else:
            print('You have enter wrong value.')


print("""
    ####################################
    ###                              ###
    ####################################
""")

val_a = enter_val('variable a')
val_b = enter_val('variable b')
val_c = enter_val('variable c')

if val_a and val_b and val_c:

    D = val_b ** 2 - 4 * val_a * val_c

    if D >= 0:
        x1 = (-val_b + D ** .5) / 2 * val_a
        x2 = (-val_b - D ** .5) / 2 * val_a
        x_type = 'float'
    else:
        x1 = complex(-val_b, abs(D) ** 0.5) / 2 * val_a
        x2 = complex(-val_b, -1 * abs(D) ** 0.5) / 2 * val_a
        x_type = 'complex'

    if x_type == 'complex':
        result = 'The solution of the equation is the complex numbers: \n x1 = ' + str(x1) + '\n x2 = ' + str(x2)
    elif x1 == x2:
        result = 'The equation has one root: \n x = ' + str(x1)
    else:
        result = 'The solution of the equation is the numbers: \n x1 = ' + str(x1) + '\n x2 = ' + str(x2)

    print(result)
else:
    print('Something goes wrong.')
