#!/usr/bin/python3
"""pas_triangle module
"""


def pascal_triangle(n):
    """Function that returns a list of lists of integers
        representing the Pascal’s triangle of n
    """
    if n <= 0:
        return ""
    else:
        final = []
        for i in range(n):
            line = [1] 
            if final:
                last = final[-1]
                line.extend([sum(pair) for pair in zip(last, last[1:])])
                line.append(1)
            final.append(line)
        return final
            