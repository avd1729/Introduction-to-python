#program to sort the dictionary by values
dct=eval(input("Enter a dictionary having integer values:"))
a={k: v for k, v in sorted(dct.items(), key=lambda a: a[1])}
d={k: v for k, v in sorted(dct.items(), key=lambda d: d[1], reverse=True)}
print("The dictionary sorted in ascending order based on values is:",a)
print("The dictionary sorted in descending order based on values is:",d)




