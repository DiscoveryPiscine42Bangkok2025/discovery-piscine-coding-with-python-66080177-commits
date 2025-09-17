original = [2, 8, 9, 48, 8, 22, -12, 2]
arrays = list(set(original))
new = []
for i in range(len(arrays)):
    if arrays[i] not in [2,-12]:
        new.append(arrays[i]+2)
print(original)
print(set(new))
