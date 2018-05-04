import datetime


def print_header():
    print('--------------')
    print(' Birthday App')
    print('--------------')
    print()


def get_user_birthday():

    user_yr = int(input('What year were you born? [YYYY]: '))
    user_mo = int(input('What month were you born? [MM]: '))
    user_da = int(input('What day were you born? [DD]: '))

    birthday = datetime.date(user_yr, user_mo, user_da)
    # print(birthday) - debugging
    return birthday


def days_delta(user, target):
    this_year = datetime.date(target.year, user.month, user.day)

    dt = this_year - target
    # print(dt) - debugging

    # By specifying the type of data you send back, it will send only an integer which can then be used to compare.
    # Otherwise it will remain in a datetime format which can not be compared.
    # This gave me a lot of issues as my code seemed fine until I got to the comparisons.
    return dt.days  # Note to self: ALWAYS SPECIFY YOUR DATA TYPE WHEN YOU ONLY NEED ONE PIECE OF IT


def print_info(days_int):
    if days_int > 0:
        print('Your birthday is in {} days!' .format(days_int))
    elif days_int < 0:
        print('You\'ve had your birthday this year, {} days ago!' .format(-days_int))
    elif days_int == 0:
        print('Today is your birthday! Happy Birthday to you!')


def main():
    print_header()
    user_date = get_user_birthday()
    current_date = datetime.date.today()
    days_between = days_delta(user_date, current_date)
    print_info(days_between)


main()