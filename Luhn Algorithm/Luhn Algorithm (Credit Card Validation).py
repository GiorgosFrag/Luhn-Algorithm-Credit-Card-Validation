num=input("enter a number:")
sum1=0
sum2=0
sum3=0
if len(num)==16:
    for i in range(8):
        mult=int((num[-2::-2][i]))*2
        print(mult)
        if mult < 9 :
            sum1=sum1+mult
        elif mult > 9 :
            digits = [int(x) for x in str(mult)]
            print("-->{} is greater than 9".format(mult))
            digits1=digits[0]+digits[1]
            print("--->the sum of the digits is {}".format(digits1))
            sum2=sum2+digits1
            
    for j in range(8):
        rest=int((num[-1::-2][j]))
        sum3=sum3+rest

    print(sum1)
    print(sum2)
    print(sum3)

    finalsum=sum1+sum2+sum3
    print(finalsum)

    if (finalsum%10==0):
        print("Your credid card number is valid")
    else:
        print("Your credid card number is invalid")
            
else:
    print("Please give me a 16 digit number")
            