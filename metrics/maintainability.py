import math


def maintainability_index(volume,
                          complexity,
                          loc,
                          comments=0):

    if loc == 0:
        return 100

    mi = (
        171
        - 5.2 * math.log(max(volume, 1))
        - 0.23 * complexity
        - 16.2 * math.log(max(loc, 1))
        + 50 * math.sin(
            math.sqrt(2.4 * comments)
        )
    )

    mi = max(0, min(100, mi))
    return round(mi, 2)