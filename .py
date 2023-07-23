madapur="Welcome @ Ekipit Solutions Start The at 10:A.M"
UPPER=""
LOWER=""
SPECIAL=""
DIGITS=""
for item in madapur:
    if item.isupper():
        UPPER+=item;
    elif item.islower():
        LOWER+=item;
    elif item.isdigit():
        DIGITS+=item;
    else:
        SPECIAL+=item;
print(UPPER)
print(LOWER)
print(SPECIAL)
print(DIGITS)


year=2022
if(year%400==0)and(year%100==0):
   print("is a leap year")
elif(year%4==0)and (year!=0):
   print("is a leap year")
else: 
 print("not a leap year")

x=20
y=40
temp=x
x=y
y=temp
print("x = ",x)
print("y =",y)


num1=(1,2,3,4,5)
num2=(6,7,8,9,10)
temp=num1
num1=num2
num2=temp
print(num1)
print(num2)

def reversed(a):
    new_a=a[::-1]
    return new_a
a=(10,20,30,40,50)
print(reversed(a))


tuple1=(12,13,14,15,16)
tuple2=tuple1[2:-1]
print(tuple2)

sum=("apple",[10,20,30],[12,13,14])
print(sum[1][1])


tuple=(40,50,60,70)
a,b,c,d=tuple
print(a)
print(b)
print(c)
print(d)

tuple3=(20,30,40,50,60,70)
tuple4=tuple3[3:-1]
print(tuple4)

tuple1=(50,10,60,50,70,50)
print(tuple1.count(50))

