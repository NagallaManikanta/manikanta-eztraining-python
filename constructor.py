class art():

 def __init__(self,a,b,c): #its automatically call from creating an object there is no cseparate object aclling required
 
   s=a+b+c
   print(s)
 def mul(self,a,b,c):
     m=a*b*c
     print(m)
 def __del__(self):
     print("destrustor")
     
x=art(1,2,3)
x.mul(1,2,3)
 
