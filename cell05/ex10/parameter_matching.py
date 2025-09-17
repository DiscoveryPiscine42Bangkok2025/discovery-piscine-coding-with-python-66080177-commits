import sys

if len(sys.argv) != 2:
    print("none")
else:
    parameter = sys.argv[1]
    matching = input("What was the parameter? :")

    if matching == parameter:
        print("Good job!")
    else:
        print("Nope, sorry...")
