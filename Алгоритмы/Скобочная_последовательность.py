def is_correct_bracket_seq(seq):
    r_brackets = 0
    s_brackets = 0
    braces = 0
    for i in seq:
        if i == '{':
            braces += 1
        if i == '}':
            if braces == 0:
                braces += 99
            braces -= 1
        if i == '[':
            s_brackets += 1
        if i == ']':
            if s_brackets == 0:
                s_brackets += 99
            s_brackets -= 1
        if i == '(':
            r_brackets += 1
        if i == ')':
            if r_brackets == 0:
                r_brackets += 99
            r_brackets -= 1
    if r_brackets + s_brackets + braces == 0:
        print('True')
    else:
        print('False')


def main():
    sequence = input()
    is_correct_bracket_seq(sequence)


main()
