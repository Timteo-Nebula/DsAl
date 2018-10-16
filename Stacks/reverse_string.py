from Stacks.Stack import Stack


def rev_string(string):
    s = Stack()
    for character in string:
        s.push(character)
    l = []
    while not s.is_empty():
        l.append(s.pop())
    return ''.join(l)


if __name__ == '__main__':
    string = 'abcde'
    print(string, '\n', rev_string(string))
