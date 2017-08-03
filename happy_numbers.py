def sum_of_squares(num):
    string = str(num)
    digits = [int(char) ** 2 for char in string]
    return sum(digits)

def happy(num):
    box = []
    n = num

    while n != 1 and n not in box:
        box.append(n)
        n = sum_of_squares(n)
    return n == 1

assert happy(97)
assert happy(1)
assert happy(10)
assert happy(100)
assert happy(130)
assert not happy(4)