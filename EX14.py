#program to compute the simple intrest and compound interest
prnc=int(input("principal:"))
time=int(input("time(in years):"))
rate=float(input("rate(in%):"))
SI=(prnc*time*rate)/100
print("simple intrest is",SI)
amnt=prnc*(pow((1+rate/100),time))
CI=amnt-prnc
print("compound interest is",CI)
