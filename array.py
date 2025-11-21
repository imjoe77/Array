import sys

if len(sys.argv) == 11:
    print("User provided inputs")
    array = [int(sys.argv[i]) for i in range(1, 11)]
else:
    print("Default input")
    array = [1, 2, 3, 9, 7, 10, 5]

sum_of_elements = sum(array)
print("Sum:", sum_of_elements)

avg_of_elements = sum_of_elements / len(array)
print("Avg:", avg_of_elements)

print("Max:", max(array))
print("Min:", min(array))
