import sys
A = sys.argv[1:]
if len(A) == 0:
    print("none")
else:
    print(f"parameters: {len(A)}")
    for i in A:
        print(f"{i}: {len(i)}")
