import sys

if len(sys.argv) != 2:
    print("none")
else:
    parameters = sys.argv[1]  

    count = parameters.count("z")

    if count == 0:
        print("none")
    else:
        print("z" * count)
