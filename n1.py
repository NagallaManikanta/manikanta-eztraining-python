'''print(10^3)
print(12^4)
print(~10)
print(9^8)
print(10<<2)
print(10>>2)
print(8<<2)
#get any two numbers as input both the number as less than 15 perform bitwise and or xor operations
a,b=input("enter two numbers ").split()
a,b=int(a),int(b)
if a<15 and b<15:
 print("bitwise and operation:",a&b)
 print("bitwise or operation:",a|b)
 print("bitwise xor operation:",a^b)
else:
    print("your inputs are greater than 15")
#============================================================
n=int(input("size of the list"))
a=list(map(int,input("number").strip().split()))[:n]
print(a)#number1 2 3 4
#[1, 2, 3, 4]
#=============================================================
a=list(map(int,input("number").strip().split()))[:10]
d=1
for i in range(len(a)):
    d=d*a[i]
print(d)#3628800
#===================================================================
print("its ", "a", "good", "day" ,end=" ")
print("all","is","good" ,sep="***",end=" ")#its  a good day all***is***good 
col=3 
row=5
for row=0 and col=0:
    print()
print("𓆏")
#================================================
n=int(input("enter the number"))
if n==500:
    print("equal")
else:
    print("not equal")#enter the number10
#not equal
#================================================
n1=int(input("enter the number"))
if n1%2==0 and n1>0:
    print("even positive")
elif n1%2==0 and n1<0:
    print("even negative")
elif n1%2!=0 and n1>0:
    print("odd positive")
else:
    print("odd negative")
#================================================
n2,n3=input("enter the numbers").split()
n2,n3=int(n2),int(n3)
if n2>n3:
    print(n2,"is biggest")
else:
    print(n3,"is biggest")
#=====================================================
n4=10.4
if int(n4)==n4:
    print(n4,"is integer")
else:
    print(n4,"is floating")
or
n4=10.4
if isinstance(n4,int)==True:
    print(n4,"is integer")
else:
    print(n4,"is floating")
or 
n4=10.3
result=n-int(n)
if result==0:
  print(n4,"is integer")
else:
    print(n4,"is floating")
or 
n4=10.4
if int(n4)%n4==0:
    print(n4,"is integer")
else:
    print(n4,"is floating")
#======================================================
l=list(input("enter the number").split())[:3]
l.sort()
print(l[-1])
#=======================================================
n5=int(input("enter the number"))
if n5%11==0:
    print("the number divisible by 11")
else:
    print("the number not divisible by 11")
#======================================================
n6=int(input("enter the number"))
if n6%2==0 and n6%5==0:
    print("the number divisible by 2 qnd 5")
else:
    print("the number not divisible by 2 and 5")  
#=====================================================
#loop
i=1
while i<=10:
    print(i)
    i+=1
#------------------------------------------------------'''
i=1
while i<=20:
    if i%2==0:
      print(i)
      i+=1