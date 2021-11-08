def check_card_number_str(string):
    a = string[len(string) - 1]
    b = get_last_number(string)
    return a == b


def check_card_number(number):
    string = str(number)
    return check_card_number_str(string)


def generate_card_number(card_type):
    import random
    head = '0'
    if card_type == 'visa':
        head = '4'

    elif card_type == 'mastercard':
        head = '5'

    random.randint(10 ** 15, (10 ** 16) - 1)
    str1 = head + str(random.randint(10 ** 15, (10 ** 16) - 1))
    tail = get_last_number(str1)
    return str1[:-1] + tail


def get_last_number(string):
    a = 0
    for i in range(0, len(string)):
        index = len(string) - 1 - i
        if i != 0:
            if i % 2 == 1:
                temp = int(string[index]) * 2
                if temp < 10:
                    a += temp
                else:
                    a += temp // 10 + temp % 10
            else:
                a += int(string[index])
    return str(10 - (a % 10))


assert check_card_number(5082337440657928)
assert not check_card_number_str('4601496706376197')
assert check_card_number(generate_card_number('visa'))
assert check_card_number(generate_card_number('mastercard'))
