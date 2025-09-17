import sys

params = sys.argv[1:]

if len(params) != 2:
    print("none")
else:
    try:
        start = int(params[0])
        end = int(params[1])

        result = list(range(start, end + 1))
        print(result)
    except ValueError:
        print("none")
