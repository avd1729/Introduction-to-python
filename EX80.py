#Program to print all the combinatins of strings with spaces
def toString(lst):
    s=''
    for i in lst:
        if i=='&# 092;&# 048;':
            break
        s+=i
    return s
def combin(string,buff,j,k,n):
    if j==n:
        buff[k]='&# 092;&# 048;'
        print(toString(buff))
        return
    buff[k] = string[j]
    print(combin(string,buff,j+1,k+1,n))
    buff[k]=''
    buff[k+1]=string[j]
    print(combin(string,buff,j+1,k+2,n))
def pattern(string):
    n=len(string)
    buff=[0]*(2*n)
    buff[0]=string[0]
    combin(string,buff,1,1,n)
st=input('Enter a string:')
pattern(st)



          
