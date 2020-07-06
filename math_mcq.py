
from random import randint


def get_math_str(op):
    return f'{randint(0, 30)} {op} {randint(0, 30)}'


def ask_question(math_str):
    global correct
    global total

    total += 1

    try:
        ans = int(input(math_str + ' = '))

        if ans == eval(math_str):
            print('Correct answer.')
            correct += 1
        else:
            raise Exception
    except KeyboardInterrupt:
        quit()
    except:
        print('Wrong answer.')


def print_res():
    print('\nQuestions: {q}'.format(q=total))
    print('Correct: {c}'.format(c=correct))
    try:
        print('Score: {s}%'.format(s=correct / total * 100))
    except ZeroDivisionError:
        print('Score: 0% (0 question answered)')


def get_op():
    print('\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Integer Division\n5. Exit\n')
    choice = input('Your choice (1-5): ')

    while choice not in '1 2 3 4 5'.split():
        choice = input('Your choice (1-5): ')

    return ['+', '-', '*', '//', ''][int(choice) - 1]
    

total = correct = 0


def main():
    while True:
        op = get_op()

        if not op:
            break

        m_str = get_math_str(op)
        ask_question(m_str)

    print_res()


if __name__ == '__main__':
    main()
