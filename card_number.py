import random


def check_card_number(number):
    return number % 10 == get_last_number(number)


def check_card_number_str(string):
    a = string[len(string) - 1]
    b = get_last_number_str(string)
    return a == b


def generate_card_number(card_type):
    head = '0'
    if card_type == 'visa':
        head = '4'
    elif card_type == 'mastercard':
        head = '5'
    random_number = random.randint(10 ** 15, (10 ** 16) - 1)
    str1 = head + str(random_number)
    tail = get_last_number_str(str1)
    # tail should not be 10,so let's change random number
    if tail == '10':
        str1 = head + str(random_number + 10)
        tail = get_last_number_str(str1)
    return str1[:-1] + tail


def get_last_number(number):
    a = 0
    i = 0
    while number > 1:
        last_number = number % 10
        if i != 0:
            if i % 2 == 1:
                temp = last_number * 2
                if temp < 10:
                    a += temp
                else:
                    a += temp // 10 + temp % 10
            else:
                a += last_number
        i += 1
        number = number//10

    return 10 - (a % 10)


def get_last_number_str(string):
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

if __name__ == '__main__':
    assert check_card_number(5082337440657928)
    assert not check_card_number_str('4601496706376197')
    assert check_card_number_str(generate_card_number('visa'))
    assert check_card_number_str(generate_card_number('mastercard'))
