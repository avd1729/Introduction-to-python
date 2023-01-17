#Program to copy a text file to another text file
with open('sample.txt','r') as f1,open('new.txt','a') as f2:
    for i in f1:
        f2.write(i)




        


