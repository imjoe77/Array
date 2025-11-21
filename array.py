import sys

if len(sys.argv) == 21:
    script_name = sys.argv[0]
    array = [None] * 11
    array[10] = int(sys.argv[1])   
    print("User provided inputs")
else:
    array = [1, 2, 3, 9, 7, 10, 5]  
    print("Default input")

sum_of_elements = sum(array)
print("Sum of array elements:", sum_of_elements)

avg_of_elements = sum_of_elements / len(array)
print("Average of array elements:", avg_of_elements)

print("Max element in array:", max(array))
print("Min element in array:", min(array))
