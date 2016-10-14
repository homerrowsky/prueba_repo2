
import sys

for arg in sys.argv[1:]:
    try:
        with open(arg) as file:
            for line in file:
                print (line, end="")
    except FileNotFoundError:
        print ('ERROR: file "' + arg + '" not found')

