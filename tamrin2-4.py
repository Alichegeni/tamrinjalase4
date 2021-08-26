import math


def delta(a, b , c):

    if a != 0:
        b = b / a
        c = c / a

        p = c / a
        print('p=', p)
        q = -b / a
        print('q= ', q)

        delta = (b ** 2) - (4 * a * c)
     print('delta= ', delta)


