#program to count the number of vowels in a string
char=str(input("Enter a string:"))
lst=['a','e','i','o','u','A','E','I','O','U']
count=0
for i in char:
    for j in lst:
        if i==j:
            count+=1
print("The number of vowels in",char,"is",count)
    
