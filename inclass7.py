import math
def is_square(x):
    """ Returns True if x is perfect square
        x must be >= 2
    """
    
    square = math.sqrt(x)

    round = int(square)

    if square == round:
        return True
    
    return False


def sum_odd_squares(start, end):

    sum = 0

    for i in range(start, end):
        if i % 2 == 1:
            if is_square(i):
                sum += i

    return sum

if __name__ == "__main__":

    print(is_square(10))
    print(is_square(16))
    print(sum_odd_squares(1, 100))