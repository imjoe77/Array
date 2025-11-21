# array_input.py

# Ask user for number of inputs
n = int(input("How many numbers do you want to enter? "))

array = []

for i in range(n):
    value = int(input(f"Enter number {i+1}: "))
    array.append(value)

print("\nYou entered:", array)

sum_of_elements = sum(array)
print("Sum:", sum_of_elements)

avg_of_elements = sum_of_elements / len(array)
print("Avg:", avg_of_elements)

print("Max:", max(array))
print("Min:", min(array))
