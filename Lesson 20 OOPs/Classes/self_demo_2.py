class Counter:
    def __init__(self):
        self.count = 0  # Initialize an instance variable

    def increment(self):
        self.count += 1  # Modify the instance variable

    def get_count(self):
        return self.count

# Creating an instance of Counter
counter = Counter()

# Incrementing the counter
counter.increment()
counter.increment()

# Getting the current count
print(counter.get_count())  # Output: 2
""" Here, self.count is an instance variable that keeps track of the count for each instance of the Counter class. The methods increment and get_count use self to access and modify count for the specific instance. """