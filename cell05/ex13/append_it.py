import sys

params = sys.argv[1:]
output = []

if not params:
    print("none")
else:
    for word in params:
        if not word.endswith("ism"):
            output.append(word + "ism")

    if output:
        for item in output:
            print(item)
    else:
        print("none")
