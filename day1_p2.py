'''l=[1,2,3,4,5,6]
r=map(lambda x:x+x,l)
print(list(r))
r1=map(lambda n:pow(n,2),l)
print(list(r1))
n="vinay"
(lambda n:print(n))(n)
#-------------------------------------------------'''
import math
r=map(lambda x:math.sqrt(x),[x for x in range(1,20) if x%2==0])
print(list(r))
#=================================
'''from abc import ABC
class abstractiondemo(ABC):
    def display(x):
        print("vinay")
    def show(x):
        pass
class demo(abstractiondemo):
    def display(x):
        print("display method")
    def show(x):
        print("show method")
obj=demo()
obj.display()
obj.show()
#=============single inheritance================
class parent:
    def display(x):
        print("parent class")
class child(parent):
    def show(x):
        print("child class")
obj=child()
obj.display()
obj.show()
#=============================================
class a:
    n=90
class b(a):
    def cal(x):
      c=x.n+40
      print(c)
obj=b()
obj.cal()
#=============multiple===========================
class mom:
    def mdisplay(x):
        print("mom class")
class dad:
    def ddisplay(x):
        print("dad class")
class child(dad,mom):
    def cdisplay(x):
        print("child class")
obj=child()
obj.mdisplay()
obj.cdisplay()
obj.ddisplay()
#===============multi level====================
class grandparent:
    def gpdisplay(x):
        print("grandparent class")
class parent(grandparent):
    def pdisplay(x):    print("parent class")
class child(parent):
    def cdisplay(x):
        print("child class")
obj=child()
obj.gpdisplay()
obj.pdisplay()
obj.cdisplay()
#==============heirarical================
class grandparent:
    def pdisplay(x):
        print("parent class")
class child2(parent):
    def ch2display(x):
        print("class")
class child1(parent):
    def chdisplay(x):
        print("child class")
obj=child1()
obj.gpdisplay()
obj.pdisplay()
obj.cdisplay()
#==================hybrid==============
class a:
    def adisplay(y):
        print("a")
class b(a):
    def bdisplay(y):
        print("b")
class c(a):
    def cdisplay(y):
        print("c")
class d(c):
    def ddisplay(y):
        print("d")
class e(d):
    def edisplay(y):
        print("e")
o=e()
o.adisplay()
o.cdisplay()'''
           