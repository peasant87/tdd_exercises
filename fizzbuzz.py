'''
Regras:
1. Se multiplo de 3: fizz
2. Se multiplo de 5: buzz
3. Se multiplo de 3 e 5: fizzbuzz
4. Outros, fale o proprio numero
'''
from functools import partial

multiple_of = lambda base, num: num % base == 0
multiple_of_5 = partial(multiple_of,5)
multiple_of_3 = partial(multiple_of,3)


def robot(pos):
    say = str(pos)
    if multiple_of_3(pos) and multiple_of_5(pos):
        say = 'fizzbuzz'
    elif multiple_of_3(pos):
        say = 'fizz'
    elif multiple_of_5(pos):
        say = 'buzz'

    return say


if __name__  == '__main__':
    assert robot(1) == '1'
    assert robot(2) == '2'
    assert robot(4) == '4'

    assert robot(3) == 'fizz'
    assert robot(6) == 'fizz'
    assert robot(9) == 'fizz'

    assert robot(5) == 'buzz'
    assert robot(10) == 'buzz'
    assert robot(20) == 'buzz'

    assert robot(15) == 'fizzbuzz'
    assert robot(30) == 'fizzbuzz'
    assert robot(60) == 'fizzbuzz'