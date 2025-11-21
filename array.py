# array_flexible.py
import os, sys

def parse_list_from_string(s):
    return [int(x) for x in s.strip().split() if x.strip()]

array = None

# 1) CLI args (preferred)
if len(sys.argv) > 1:
    try:
        array = [int(x) for x in sys.argv[1:]]
        print("User input (CLI args)")
    except ValueError:
        print("Invalid CLI args. Falling back to other sources.")

# 2) Environment var or Jenkins single param ALL_NUMS or ARRAY_INPUT
if array is None:
    env = os.environ.get('ALL_NUMS') or os.environ.get('ARRAY_INPUT')
    if env:
        try:
            array = parse_list_from_string(env)
            print("User input (env ALL_NUMS/ARRAY_INPUT)")
        except ValueError:
            array = None

# 3) default
if not array:
    array = [1, 2, 3, 9, 7, 10, 5]
    print("Default input")

print("Input array:", array)
print("Sum:", sum(array))
print("Avg:", sum(array)/len(array))
print("Max:", max(array))
print("Min:", min(array))
