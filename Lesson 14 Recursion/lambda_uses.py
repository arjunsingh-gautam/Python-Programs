# Uses:

# with map():
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # Output: [1, 4, 9, 16, 25]


# With filter():
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6]


# With sorted():
points = [(1, 2), (3, 1), (5, 3), (2, 4)]
sorted_points = sorted(points, key=lambda x: x[1])
print(sorted_points)  # Output: [(3, 1), (1, 2), (5, 3), (2, 4)]
