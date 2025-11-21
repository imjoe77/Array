import sys

# Expect exactly 10 user inputs
if len(sys.argv) == 11:
    array = [int(x) for x in sys.argv[1:]]
    print("User input")
else:
    array = [1, 2, 3, 9, 7, 10, 5]
    print("Default Input")

sum_of_elements = sum(array)
print("Sum of array elements:", sum_of_elements)

avg_of_elements = sum_of_elements / len(array)
print("Average of array elements:", avg_of_elements)

print("Max element in array:", max(array))
print("Min element in array:", min(array))
