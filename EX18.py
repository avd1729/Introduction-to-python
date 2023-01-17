#pogram to check if 2 strings are anagram
s1=str(input("Enter a string"))
s2=str(input("Enter a string"))
def anagram(s1,s2):
    if(sorted(s1)==sorted(s2)):
        print("The strings are anagrams.")
    else:
        print("The srtings are not anagrams")
anagram(s1,s2)
