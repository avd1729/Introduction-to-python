#Program to count the number of vowels
def counting(filename):
	txt_file = open('sample.txt', "r")
	vowel = 0
	vowels_list = ['a', 'e', 'i', 'o', 'u',
				'A', 'E', 'I', 'O', 'U']
	for i in txt_file.read():
		if i in vowels_list:
			vowel += 1	
	print("Number of vowels in ", filename, " = ", vowel)
counting('sample.txt')





