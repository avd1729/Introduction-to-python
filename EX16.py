#program to generate electricity bill using if-else ladder
unit=int(input("Enter the number of units consumed:"))
if unit<=100:
    charge=unit*10
elif unit>100 and unit<=200:
    charge=unit*12
elif unit>200:
    charge=unit*15
else:
    print("-Invalid")
print("sur charges is 5%")
total=charge*5
print("Electricity bill is",total,"rs")
