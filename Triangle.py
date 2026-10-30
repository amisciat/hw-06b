def classifyTriangle(a,b,c):
    """
    Returns the type of triangle from three integer side lengths:
    'Equilateral', 'Isoceles', 'Scalene', 'Right', 'NotATriangle' or 'InvalidInput'
    """

    # inputs must be integers (checked first so a string doesn't crash the comparisons)
    if not(isinstance(a,int) and isinstance(b,int) and isinstance(c,int)):
        return 'InvalidInput'

    # inputs must be between 1 and 200
    if a > 200 or b > 200 or c > 200:
        return 'InvalidInput'

    if a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput'

    # the sum of any two sides must be greater than the third side
    if (a >= (b + c)) or (b >= (a + c)) or (c >= (a + b)):
        return 'NotATriangle'

    if a == b and b == c:
        return 'Equilateral'
    elif ((a ** 2) + (b ** 2)) == (c ** 2) or ((a ** 2) + (c ** 2)) == (b ** 2) or ((b ** 2) + (c ** 2)) == (a ** 2):
        return 'Right'
    elif (a != b) and  (b != c) and (a != c):
        return 'Scalene'
    else:
        return 'Isoceles'
