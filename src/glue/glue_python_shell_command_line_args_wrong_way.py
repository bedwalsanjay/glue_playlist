import sys

print(sys.argv)
# Access command-line arguments
if len(sys.argv) < 3:
    print("Usage: python script.py <arg1> <arg2>")
    sys.exit(1)

c=0
for args in sys.argv:
    print(f" {c} : {args}")
    c=c+1
