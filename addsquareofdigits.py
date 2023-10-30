n=int(input("Enter three digit number: "))
#123
a=n%10 #3
num=n//10 #12
b=num%10 #2
c=num//10 #1
output_value=(a**2)+(b**2)+(c**2)
print(output_value)