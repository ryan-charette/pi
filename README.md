# pi

## [1] SQUARE LATTICE ##

This function creates a circumscribed square around the circle

The square is subdivided into 1x1 square

A point is placed at each vertex of smaller square

The area of the circle is approximated by counting how many points are in or on the circle

A = pi*r^2 --> pi = A / r ** 2

## [2] MONTE CARLO ##

This function creates a circumscribed square around a circle of radius 1

Points are randomly placed within the square

The ratio of the two shapes' areas is approximated by counting the number of points in each

Area of a circle = pi*r^2 and area of the square = 4*r^2

Thus, A_circle/A_square = pi/4 --> pi = 4 * A_circle/A_square

## [3] INFINITE SUM ##

This function uses an infinite sum to approximate pi

Specifically, it uses the sum of infinite squares (The Basel Problem)

pi^2/6 = infinite_sum(1/n^2) --> pi = sqrt(6 * infinite_sum(1/n^2))
