'''d={n:n*n for n in range(1,5)}
print(d)
#----------------------------------------
old={'rice':60,'dhaal':45,'oil':55}
new={product:price*5 for (product,price) in old.items()}
print(new)
#------------------------------------------------------------
real={'sam':24,'angel':18,'surya':57,'pavani':56}
now={name:age for (name,age) in real.items() if age>20}
print(now)
import random

#create a list with 8 costumers names display a dictionary which as costumers names along with discounts from a particular shop
l=["surya","pavani","suryason","pavanidaugther","suryamavya","suryaathhaya"]
d={}
for i in l:
    d[i]=random.randrange(10,20)
print(d)
d={ names:random.randint(20,30) for names in l}
print(d)
#create two list frist list contains with 5 students name and two list total marks of student create a dictionary student names with keys and marks with values 
l=["surya","pavani","suryason","pavanidaugther","suryamavya","suryaathhaya"]
l1=[300,400,450,460,340,499]
d={student:((int(marks)/500)*100) for (student,marks) in zip(l,l1)}
print(d)
n="hi i'am ","salva"
h='i\'am
s="Manikanta is Good Boy"
print(s.lower())
print(s.upper())
print(s.capitalize())
print(s.strip())
print(s.split())
print(s.replace("a", "th"))
print(s.center(2,"*"))
print(s.count("a"))
print(s.count("a",5,len(s)))
print(s.endswith("a",0,len(s)))
print(s.find("a",0,len(s)))
print(s.index("a",7,len(s)))
#-------------------------------------------------
str=input("enter the string")
if "a" in str:
    print("character is persent")
else:
    print("character is not persent")
or
a="yes" if "a" in str else "no"
#====================================================
str1=input("enter the string")
if str1[::-1]==str1:
    print("string is palindorme")
else:
    print("string is not a palindrome")
#==============================----------------------------
str2=input("enter the string")
sum=int()
for i in str2:
    if i==" ":
        sum+=1
print("spaces count",sum)
#-------------------------------------------------
#create a list with vowels count vowels from the string
l=['a','e','i','o','u','A','E','I','O','U']
s=input("enter the string")
l1=[]
c=0
for i in l:
    for j in s:
        if i==j:
            c+=1
            l1.append(j)
print("count of vowel",c)
print(l1)
#=================================================================='''
import math
print("cell 12.5", math.ceil(12.5))
print("floor 12.5", math.floor(12.5))
print("sqrt 2" , math.sqrt(2))
print("factorial 3", math.factorial(3))
print("power 2,3", math.pow(2, 3))
print("remainder 10,3", math.fmod(10, 3))
a,b=divmod(10,3)
print(a,b)



