
i=1
fac = 1
num=int(input("Enter number: " ))
#if (num==0 or num==1):
#    print(num,"factorial is", 1)
#else:
while(i<=num):
    print ("next number to multiply is:", i)
    fac = i * fac
    print ("multiplied number is: ", fac)
    i=i+1
print("the final result is:  ", fac)