# Functional Programming Section

# Flattens and sorts a list of integers in ascending order
def flatten_and_sort(lst):
    # Flatten the list using a list comprehension
    flattened = [item for sublist in lst for item in sublist]
    # Sort the flattened list and return it
    return sorted(flattened)

# Example usage of the functional part
array_to_flatten = [[3, 2, 1], [4, 6, 5], [], [9, 7, 8]]
sorted_array = flatten_and_sort(array_to_flatten)
print(sorted_array)  # Output should be [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Object Oriented Programming Section

class Podracer:
    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price

    def repair(self):
        self.condition = "repaired"

class AnakinsPod(Podracer):
    def boost(self):
        self.max_speed *= 2

class SebulbasPod(Podracer):
    def flame_jet(self, other):
        other.condition = "trashed"

# Example usage of the OOP part
sebulbas_pod = SebulbasPod(120, "perfect", 300)
anakins_pod = AnakinsPod(110, "perfect", 280)
sebulbas_pod.flame_jet(anakins_pod)
anakins_pod.boost()
print(anakins_pod.condition)  # Output should be "trashed"
print(anakins_pod.max_speed)  # Output should be 220 after the boost

# Reflections and answers to thought prompts are in the code comments above each section
