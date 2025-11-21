# array_input_5.py

array = []

for i in range(5):
    value = int(input(f"Enter number {i+1}: "))
    array.append(value)

print("\nYou entered:", array)

print("Sum:", sum(array))
print("Avg:", sum(array) / len(array))
print("Max:", max(array))
print("Min:", min(array))
