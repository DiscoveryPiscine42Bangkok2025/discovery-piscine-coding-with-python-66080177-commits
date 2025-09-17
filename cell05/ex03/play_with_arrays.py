original = [2, 8, 9, 48, 8, 22, -12, 2]
new_arrays = list(set(original))
new = []
for i in range(len(new_arrays)):
    if new_arrays[i] not in [2,-12]:
        new.append(new_arrays[i]+2)
print(original)
print(set(new))
