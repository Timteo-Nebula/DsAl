from Queues.Deque import Deque


def is_palin(string):
    """
    check whether a string is a palindrome string.
    Palindrome means strings such as 'abcba','radar',and 'madam'
    """
    dq = Deque()
    for char in string:
        dq.add_front(char)
    flag = True
    while flag and dq.size() > 1:
        flag = (dq.remove_rear() == dq.remove_front())

    return flag


if __name__ == '__main__':
    palin = 'radar'
    no_palin = 'aaabbbccc'
    print(is_palin(palin))
    print(is_palin(no_palin))
