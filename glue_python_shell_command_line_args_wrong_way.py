import sys

# Access command-line arguments
if len(sys.argv) != 3:
    print("Usage: python script.py <arg1> <arg2>")
    sys.exit(1)

print(sys.argv)
print(type(sys.argv))
# arg1 = sys.argv[1]
# arg2 = sys.argv[2]

# print(f"Argument 1: {arg1}")
# print(f"Argument 2: {arg2}")
