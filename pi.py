# Here are a few algorithms you can use to approximate pi

from random import random

# This function creates a circumscribed square around the circle
# The square is subdivided into 1x1 square
# A point is placed at each vertex of smaller square
# The area of the circle is approximated by counting how many points are in or on the circle
# A = pi*r^2 --> pi = A / r ** 2
def square_lattice():
    subdivisions = int(input("Number of square subdivisions: "))
    radius = (subdivisions - 1) / 2
    list_of_points = []
    in_or_on_circle = 0
    for x in range(0, subdivisions):
        for y in range(0, subdivisions):
            list_of_points.append((x - radius, y - radius))
    for point in list_of_points:
        x = point[0]
        y = point[1]
        if x ** 2 + y ** 2 <= radius ** 2:
            in_or_on_circle += 1
    return in_or_on_circle / radius ** 2

# This function creates a circumscribed square around a circle of radius 1
# Points are randomly placed within the square
# The ratio of the two shapes' areas is approximated by counting the number of points in each
# Area of a circle = pi*r^2 and area of the square = 4*r^2
# Thus, A_circle/A_square = pi/4 --> pi = 4 * A_circle/A_square
def monte_carlo():
    iterations = int(input("Sample size: "))
    in_or_on_circle = 0
    out_circle = 0
    for iteration in range(iterations):
        x = random()
        y = random()
        if x ** 2 + y ** 2 <= 1:
            in_or_on_circle += 1
        out_circle += 1
    return 4 * (in_or_on_circle / out_circle)

# This function uses an infinite sum to approximate pi
# Specifically, it uses the sum of infinite squares (The Basel Problem)
# pi^2/6 = infinite_sum(1/n^2) --> pi = sqrt(6 * infinite_sum(1/n^2))
def inverse_squares():
    sum_of_inverse_squares = 0
    n = 1
    iterations = int(input("Number of iterations: "))
    while n < iterations:
        sum_of_inverse_squares += n ** -2
        n += 1
    return (6 * sum_of_inverse_squares) ** 0.5

def main():
    while True:
        user_input = input("""
How would you like to approximate pi? 
[1] Square Lattice
[2] Monte Carlo
[3] Infinite Sum
[4] Help
""")
        if user_input == "1":
            print(square_lattice())
        elif user_input == "2":
            print(monte_carlo())
        elif user_input == "3":
            print(inverse_squares())
        elif user_input == "4":
            print("""
[1] SQUARE LATTICE
This function creates a circumscribed square around the circle
The square is subdivided into 1x1 square
A point is placed at each vertex of smaller square
The area of the circle is approximated by counting how many points are in or on the circle
A = pi*r^2 --> pi = A / r ** 2

[2] MONTE CARLO
This function creates a circumscribed square around a circle of radius 1
Points are randomly placed within the square
The ratio of the two shapes' areas is approximated by counting the number of points in each
Area of a circle = pi*r^2 and area of the square = 4*r^2
Thus, A_circle/A_square = pi/4 --> pi = 4 * A_circle/A_square

[3] INFINITE SUM
This function uses an infinite sum to approximate pi
Specifically, it uses the sum of infinite squares (The Basel Problem)
pi^2/6 = infinite_sum(1/n^2) --> pi = sqrt(6 * infinite_sum(1/n^2))

Press 'Q' to quit.
""")
        elif user_input == "Q" or user_input == 'q':
            break

main()
