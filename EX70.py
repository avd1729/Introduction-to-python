#program to sort the dictionary by keys
dct=eval(input("Enter a dictionary having integer values:"))
a={k: v for k, v in sorted(dct.items(), key=lambda a: a[0])}
d={k: v for k, v in sorted(dct.items(), key=lambda d: d[0], reverse=True)}
print("The dictionary sorted in ascending order based on values is:",a)
print("The dictionary sorted in descending order based on values is:",d)

