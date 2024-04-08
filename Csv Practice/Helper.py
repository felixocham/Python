def days_to_units(num_of_days,conversion_unit):
    if conversion_unit=='hours':
        return (f'{num_of_days} days are {num_of_days*24} {conversion_unit}')
    elif conversion_unit=='minutes':
        return (f'{num_of_days} days are {num_of_days * 24*60} {conversion_unit}')
    else:
        return ''

def input_validation_and_execution(Days_and_units_Dictionary):
    try:
        user_input_number = int(Days_and_units_Dictionary['Days'])
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number,Days_and_units_Dictionary['Units'])
            print(calculated_value)
        elif num_of_days==0:
            print('You entered a 0, please enter a valid positive integer')
    except ValueError:
        print('Your input is not a valid number, please do not ruin my program')


user_input_message='Hey user please enter  a number of days and convertion unit!\n'