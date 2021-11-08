def is_lucky_ticket(number):
    string = str(number)
    length = len(string)
    a = 0
    b = 0
    for i in range(0, length):
        if i % 2 == 0:
            a += int(string[i])

        elif i % 2 == 1:
            b += int(string[i])

    return a == b


def get_nearest_lucky_ticket(number):
    n = 0
    while True:
        if is_lucky_ticket(number - n):
            return number - n
        elif is_lucky_ticket(number + n):
            return number + n
        n += 1


assert get_nearest_lucky_ticket(111111) == 111111
assert get_nearest_lucky_ticket(123321) == 123321
assert get_nearest_lucky_ticket(123320) == 123321
assert get_nearest_lucky_ticket(333999) == 334004
