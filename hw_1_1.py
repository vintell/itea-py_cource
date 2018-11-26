# constants
DAYS_IN_MONTH = 30
MONTHS_IN_YEAR = 12
DAY_IS_NOW = 19
MON_IS_NOW = 11
YEAR_IS_NOW = 2018

# init
is_error = False
# inputs
f_name = input('What is your first name: ')
l_name = input('What is your last name: ')
print('Hey, ', f_name, ' ', l_name, '.')

# day_ = 3
# mon_ = 9
# year_ = 1982

day_ = int(input('Enter your day of birthday: '))
if day_ == 31:
    day_ = 30
elif day_ > 31 or day_ < 1:
    is_error = True
mon_ = int(input('Enter your month of birthday: '))
if mon_ > 12 or mon_ < 1:
    is_error = True
year_ = int(input('Enter your year of birthday: '))
if year_ > YEAR_IS_NOW:
    is_error = True

if is_error:
    print('Wrong entered date.')
else:
    # calculate days in totally
    days_are_alive = (DAY_IS_NOW - day_)
    days_are_alive = days_are_alive + ((MON_IS_NOW - mon_) * DAYS_IN_MONTH)
    days_are_alive = days_are_alive + (YEAR_IS_NOW - year_) * MONTHS_IN_YEAR * DAYS_IN_MONTH

    #
    leaved_y = days_are_alive // (MONTHS_IN_YEAR * DAYS_IN_MONTH)
    leaved_m = (days_are_alive - (leaved_y * (MONTHS_IN_YEAR * DAYS_IN_MONTH))) // DAYS_IN_MONTH
    leaved_d = (days_are_alive - (leaved_y * (MONTHS_IN_YEAR * DAYS_IN_MONTH)) - (leaved_m * DAYS_IN_MONTH))

    print(f_name, ' ', l_name, ' You have been live ', days_are_alive, ' days till ', DAY_IS_NOW, '.', MON_IS_NOW, '.', YEAR_IS_NOW, '.', sep='')
    print('Or is totally: ', leaved_y, ' year(-s) and', leaved_m, ' month(-s) and ', leaved_d, ' day(-s).')
