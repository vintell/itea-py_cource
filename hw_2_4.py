"""
    Fibonacci numbers
"""


is_not_valid_value = True
stop_fl = False
max_entered_value = 10000
result = None

print("""
    ####################################
    ### This is a Fibonacci numbers. ###
    ####################################
""")

while is_not_valid_value:
    entered_value = input('Enter number or enter word \'stop\' for exit: ')
    if entered_value == 'stop':
        print('Application stopped.')
        break
    is_not_valid_value = False if entered_value.replace('.', '').isnumeric() and (entered_value.count('.') == 0) else True
    if is_not_valid_value == False and int(entered_value) > max_entered_value:
        is_not_valid_value = True
        print('Try enter smaller value. Cause value final value is huge.')
else:
    result = 0
    res_minus_1 = 0
    res_minus_2 = 0
    for iteration in range(int(entered_value)+1):
        if iteration >= 2:
            res_minus_2 = res_minus_1
            res_minus_1 = result
            result = res_minus_1+res_minus_2
        elif iteration == 1:
            result = 1
        # print('iteration={} Result is {}'.format(iteration, result))
    else:
        print('Sequence till {} is Fibonacci value is {}'.format(entered_value, result))
