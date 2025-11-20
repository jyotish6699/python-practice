# a=4.3
# b=4
# print("a=%d#b=%.2f" % (a, b))

# print(0b11)
# print(0o11)
# print(0x11)
# print(0x1f)
# print(ord("a"))
# print(chr(97))
# print(ord("A"))
# #sky value or unicode value
# # A=65 to Z=90
# # a=97 to z=122
# a=4.5
# b=4
# print("a=%d"%a,"b=%.2f"%b)
# print("a=%d#b=%.2f" % (a, b))
# a=6
# b=4
# print(f"a={a}#b={b}")
# print(a&b)
# print(a|b)
# print(a^b)
# print(~a)
# print(a<<b)

# print(a>>b)
# #floor operator

# print(a//b)
# a=4
# b=5
# print(a and b)
# #membership operator like in and not in
# str1="welcome"
# print("s"in str1)
# print("s"not in str1)
# print("a=%d#b=%f"%(a,b))
# print(f"a={a}#b={b}")
# print(a|b)

# print(a&b)
# print(a^b)
# print(~a)
# print(a and b)
# print(a or b)
# print(ord("a"))#ordinal value(unicode value)
# print(ord("A"))
# print(chr(97))#character value(sky value)
# print(0b11)
# print(0o11)
# print(0x11)
# print(0x1f)
# #identity operator like is and is not
# print(a is b)
# print(a is not b)
# #membership operator like in and not in
# str1="welcome"
# str2="come"
# print(str1 in str1)
# print(str2 not in  str1)
# #floor operator part of arithmetic operator
# print(a//b)
# print(4//16)
# print(16//4)
# print(4//3)

# #comparison operator
# print(4==4)
# print(4==3)
# #asignment operator always use to asign the value in variable
# #print(a+=3)
# a=4
# a+=3#a=a+3
# a-=3#a=a-3
# a*=3#a=a*3
# a/=3#a=a/3
# a//=3#a=a//3
# a%=3#a=a%3
# a**=3#a=a**3
# #bitwise operator not use in float value
# #a&=3#a=a&3
# #a|=3#a=a|3
# #a^=3#a=a^3
# #a>>=3#a=a>>3
# #a<<=3#a=a<<3
# print(a)


# #list data type
# empty_list=[]
# #list can store multiple data type
# #list can store duplicate value
# #list can store multiple data type
# #list arrange in order
# #list is mutable(changeable))
# #list is dynamic
# #list is growable
# #list is heterogenous
# #list is index based
# #list is sequence data type
# #list is iterable
# #list is mutable
# #list is represented by square bracket
# #list is represented by comma separated value
# #list is represented by list()
# #list is represented by list comprehension
# #list is represented by list slicing


# my_list=[1,2,3,4,5,6,7,8,9,10]
# print(my_list)
# print(my_list[0])
# print(my_list[-1])
# #in slicing first index is inclusive and last index is exclusive
# print(my_list[0:5])
# print(my_list[0:10:2])
# print()
# #list comprehension means consise way to create list means create list in one line means shortcut to create list
# print([i for i in range(1,11)])
# print([i for i in range(1,11) if i%2==0])
# print([i for i in range(1,11) if i%2!=0])
# b=5
# print(i for i in range(3,33) if i**3==b**3)

# #list method
# print()
# a=4
# my_list_demo=[1,2,3,4,5,6,7,8,9,10]
# #adding in list
# #append() add single element in list
# #whereas add multiple element in append() we use extend() method but if you want to add multiple element in append() method then append() treat as single element
# my_list_demo.append(4)
# print(my_list_demo)
# #extend() add multiple element in list
# my_list_demo.extend([4,5,6,7,8,9,10])
# #insert() add element in list at specific index and shift the other element to right and if index is not given then it will add element at last and if index is out of range then it will add element at last and if index is negative then it will add element at last and if index is zero then it will add element at first 
# #list.insert(index,element))
# print(my_list_demo.insert(0,4))

# #removing from list
# #remove() remove element from list by value and if value is not found then it will give error and if value is duplicate then it will remove first occurrence of value
# my_list_demo=[1,2,3,4,5,6,7,8,9,10]
# my_list_demo.remove(4)
# print(my_list_demo)
# #pop() remove element from list at specific index and return the removed element and if index is not given then it will remove last element and if index is out of range then it will give error and if index is negative then it will remove last element and if index is zero then it will remove first element
# my_list_demo.pop(1)
# print(my_list_demo)
# #clear() remove all element from list
# my_list_demo.clear()
# print(my_list_demo)
# #count() count the occurrence of element in list
# my_list_demo=[1,2,3,4,5,6,7,8,9,10,4,4,4]
# print(my_list_demo.count(4))
# #delete() delete the list
# del my_list_demo

# #sort() sort the list in ascending order and if reverse=True then it will sort in descending order

# my_list_demo=[1,2,3,4,5,6,7,8,9,10,4,4,4]
# my_list_demo.sort()
# print(my_list_demo)
# my_list_demo.sort(reverse=True)
# print(my_list_demo)
# #reverse() reverse the list
# my_list_demo.reverse()
# print(my_list_demo)
# #copy() copy the list
# my_list_demo_copy=my_list_demo.copy()                                
# print(my_list_demo_copy)

# #nested list
# list1=[1,2,3]
# list2=[4,5,6]
# print([list1,list2])
# list1.append(list2)
# print(list1)
# list1.extend(list2)
# print(list1)
# print(list1[3][0])
# #list iteration
# list= [1,2,3,4,5,6,7,8,9,10]
# a=4
# for a in list:
#     print(a*2)

# while a<len(list):
#     print(list[a])
#     a+=1
# #concatenation of list
# list1=[1,2,3]
# list2=[4,5,6]
# print(list2+list1)
# #repetition of list
# print(list1*2)
# #copying of list
# list3=list1.copy()
# print(list3)
# print(list1)
# #list alising
# list4=list1
# print(list4)
# #iteration of list
# enumerate(list1)
# zip(list1,list2)
# print(zip(list1,list2))


# #number formatting
# a=5
# b=3
# list=[1,2,3,4,5,6,7,8,9,10]
# print("a=%d#b=%.2f"%(a,b))
# print(f"a={a}#b={b}")
# #filtering even number from list
# print([i for i in list if i%2==0])
# print()
# print(3>>3)

# print(3<<3)
# print(~3)
# print(i for i in range(4,8) if i**2==2)

# #for loop
# print("hello world")
# a = [i for i in input().split()]
# for i in a:
#     print(i)


# print("hello")
# def hello():
#     hello()
    

# hello()

# list=[3,5,6,5,6,7,8]
# list.sort()
# print(list)
# #nested loop

# for i in range(1,9):
#     for j in range(i):
#         print(j,end=" ")
#     print(i)


# a=input("list: ").split(",")
# print(a)




# #dictionary
# dict1={
#     "a":5,
#     "b":6,
#     "c":7,
#     "d":8
# }
# #making tuples using .items() method
# for i in dict1.items(): 
#     print(i)

# key=["x","y","z","a"]
# values=[34,5,6,34]
# z=dict(zip(key,values))
# #print(z)

# for i,j in z.items():
#    print(i,j)

# list1=[i for i in range(1,9)]
# list2=[i**3 for i in range(1,9)]


# print(list2)
# z=dict(zip(list1,list2))
# for i,j in z:
#     print(i,j)


# #dictionary comprehension
# result={i:i**3 for i in range(1,11)}
# print(result)

# #lambda function

# add=lambda x,y:x+y
# print(add(2,3))

# #anonymous function means immediate call
# print((lambda x,y:x*y)(4,5))


# l1=[4,3,7,6,8]
# l2=["j","y","o","t","i"]
# dict=dict(zip(l1,l2))
# sorted_dict=sorted(dict)
# print(sorted(dict))


# def myfunc(a,b):
#     sum=a+b
#     print(sum)
   

# myfunc(3,4)


# list={
#     "a":1,
#     "b":2,
#     "c":3,
#     "d":4,
#     "e":5
# }

# for i,j in list.items():
#     print(i,j)

# list1=[2,3,4,5,6,7,8]
# #map function
# def squares(x):
#     return x**2
# m=list(map(squares,list1))
# print(m)
# #filter function
 
# list2=list(filter(lambda x:x%2==0,list1))
# print(list2)
# #reduce function


# print(0b111)
# print(0x3f)
# print(0o44)


# add=lambda x,y:x+y
# print(add(3,4))

# list=[-i for i in range(-4,11)]
# print(list)
# print("hello world")
# print("hello jyotish")

# #method1
# list2=[3,-5,-3,5,9,-1,2]
# def absolutevalue(seq):
#     return [abs(i) for i in seq]

# a=absolutevalue(list2)
# print(a)
# #method2
# def absolute_input(input):
#     list1=[]
#     for i in input:
#         if i>0:
#             list1.append(i)
#         else:
#             list1.append(-i)
#     return list1

# print(absolute_input(list2))

# #abstract function to return the absolute value
# print(abs(-2))
# print(abs(4))
# print("save point-2")

# #print factorial
# n=int(input("enter a number:"))
# fact=1
# for i in range(1,n+1):
#     fact*=i
# print(fact)


##compostion of function
# def add(x):
#     return x+2
# def square(y):
#     return y*y
# result=square(add(3))
# print(result)

##compose function=>making chain of function
# x=int(input("enter a number:"))
# def square(x):
#     return x*x
# def add(x):
#     return x+2
# def half(x):
#     return x

# def compose(*functions):
#     def inner(arg):
#         result=arg
#         for f in functions:
#             result=f(result)
#         return result
#     return inner

# final=compose(square,add,half)
# print(final(x))
# final2=compose(half,add,square)
# print(final2(x))

##convert the element of list into integer type
# n=['3','5','7','9','11']
# #method1 using loop
# for i in range(len(n)):
#     n[i]=int(int(n[i]))
# print(n)
# #method2 using map function
# n=list(map(int,n))
# print(n)

# #class and object(instance)
##class is the blueprint of object(instance) 
##constructor is a special method which is used to initialize the object(instance) of class

##object is the instance of class
##class is the blueprint of object(instance)
##object define itself without his origin
##instance define itself with his origin 
##class is a user defined data type

##constructor is a special type of method which is used to define global variable of class so that it can used by all normal method(function) of class using self keyword self keyword is used to define the global variable of class so that it can be used by all normal method(function) of class
##constructor is defined by __init__() method
##normal function can behave like constructor function if we use self keyword to define global variable of class
##but when initialize the class in any object then you have to call normal function manually but constructor function is called automatically when we initialize the class in any object
##when we define any normal function in class then we have to call that function manually but when we define constructor function in class then we don't have to call that function manually because constructor function is called automatically when we initialize the class in any object
##example of constuctor and normal function in class
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
    
# myperson=Person("jyotish",20)
# print(myperson.age)

##as soon as initilize the class in any object the constructor is called automatically without calling it manually or without printing it but next example shows that normal function is not called automatically when we initialize the class in any object we have to call it manually
# class Person:
#     def __init__(self):
#         self.name="jyotish"
#         self.age=20
#         print(self.name,self.age)

# myperson=Person()

##you can't call the class variable directly inside the method because class variable is not belong to the object(instance) of class it belong to the class itself so to access the class variable inside the method of class you have to use either self keyword or class name
##example of class variable
##and example of accessing class variable inside the method of class using self keyword and class name
# class Person:
#     myname="hello"
#     def info(self):
#         self.name="jyotish"
#         self.age=20
#         print(self.name,self.age)
#         print(self.myname)
#         print(Person.myname)

    

# myperson=Person()
# myperson.info()

# #inside class we can define three types of variable
# #1.class variable
# #2.instance variable(object variable)
# #3.local variable

# #object of two types global object and local object
# #global object which is defined outside the class and can be accessed by all class and function
# #local object which is defined inside the class and can be accessed by that class only like self(recommended)
# #self is not keyword it is popular word to define local object inside the class instead of self you can use any word but it is recommended to use self because it is popular word to define local object inside the class
# #first parameter of method is always local object(self)
# #initialize the class in any variable is called global object or real object 

# #example of class variable, instance variable(object variable) and local variable
# #define a class StudentId with class variable schoolname, instance variable name, age, grade and method info to print the details of student and method updategrade to update the grade of student
# class StudentId:
#     schoolname="st. colombus public school"
#     def __init__(student,studentname,studentage,studentgrade):
#         student.name=studentname
#         student.age=studentage
#         student.grade=studentgrade
    
#     def info(student):
#         print(f"school name is: {student.schoolname}")
#         print(f"student name is: {student.name}")
#         print(f"student age is: {student.age}")
#         print(f"student grade is: {student.grade}")

#     def updategrade(student,newgrade):
#         student.grade=newgrade
#         print(f"student new grade is: {student.grade}")

# student1=StudentId("jyotish",20,"A++")
# student2=StudentId("rahul",21,"A+")
# student1.info()

# student1.updategrade("b++")

##reverse a string 
##method1 using slicing
# a="jyotish"
#print(a[::-1])
##method2 using loop
# rev=""
# for i in a:
#     rev=i+rev
# print(rev)

##method3 using reversed() function
# rev2=''.join(reversed(a))
# print(rev2)
##method4 using recursion
# def reverse_string(s):
#     if len(s)==0:
#         return s
#     else:
#         return s[-1]+reverse_string(s[:-1])
    
# print(reverse_string(a))

##print all element of tuple except the last element
# tup=(1,2,3,4,5,6,7,8,9,10)
# print(tup[:-1])
##print all element of tuple except the first element
# print(tup[1:])
##print all element of tuple except the first and last element
# print(tup[1:-1])

#---------------------------------------
##question on 0ops
#------------------------------------
#overloading in oops
##inheritance,polymorphism,overloading and modularity,abstraction,encapsulation,multiple inheritance,multilevel inheritance,method overriding,
#---------------------------------------
#1inheritance means property of parent also child have their property of parent and child have their own property also child can access the property of parent using inheritance or super() method

#2polymorphism means poly(many) morphism(forms) means many forms one name means same method name but different class
#polymorphism is of two types

#1compile time polymorphism(static polymorphism) means method overloading and operator overloading

#2run time polymorphism(dynamic polymorphism) means method overriding

#difference between polymophism and overriding  polymorphism is of two types compile time polymorphism and run time polymorphism whereas overriding is only run time polymorphism

#3overloading means same method same class but multiple parameters in multiple call

#4modularity means divide the large program into small program called module so that it can be easily debugged and maintained

#5abstraction means hide the implementation details and show only functionality to the user 

#6encapsulation means data inside the capsule layer and data can only be accessed by the method of class when we make data private using __ before the variable name because private data can only be accessed by the method of class(inside the class) and not outside the class and public data can be accessed by the method of class(inside the class) and outside the class also

# class Person:
#     def __init__(self,owner,money):
#         self.owner=owner
#         self.__money=money  #private variable
#     def deposit(self,amount):
#         self.__money+=amount
#         print(f"amount deposited: {amount}")
#         print(f"new balance: {self.__money}")
#     def withdraw(self,amount):
#         if amount>self.__money:
#             print("insufficient balance")
#         else:
#             self.__money-=amount
#             print(f"amount withdrawn: {amount}")
#             print(f"new balance: {self.__money}")
                
#     def display_balance(self):
#         print(f"balance of {self.owner}: {self.__money}")

# person1=Person('jyotish',1000)
# person2=Person('rahul',2000)
# person1.deposit(500)
# person2.deposit(1000)
# person2.withdraw
# person1.withdraw(200)
# person1.display_balance()
# person2.display_balance()
# print(person1.owner)

#print(person1.__money) #error because __money is private variable and can only be accessed by the method of class(inside the class) and not outside the class

#7multiple inheritance means child have have multiple parent class(same level value of both parent class)
#8multilevel inheritance means child have parent and grandparent class(different level value of both parent class)


#inheritance means property of parent also child have their property of parent and child have their own property also child can access the property of parent using super() method
#parent class==base class==super class
#child class==derived class==sub class

#calling constructor of parent class to use parent parent name variable in child class

#name variable is defined in parent class beacause making object of child class we have to pass name variable also so to avoid the error we have to call the constructor of parent class using super() method

#single inheritance using super() method and method overriding
# class Person:
#     def __init__(self,name):
#         self.name=name
#     def getname(self):
#         print(self.name)

# class Student(Person):
#     def __init__(self,name,marks):
#         super().__init__(name)
#         self.marks=marks
#         #overriding getname() method of parent class
#     def getname(self):
#         print(self.name,self.marks)


# student1=Student("jyotish",90)
# student1.getname()

#Multiple Inheritance is like having two parents (Mother and Father).
#Multilevel Inheritance is like having a parent and a grandparent.

#overloaing means same method same class but multiple parameters in multiple call

# class Mathoperation:
#     def add(self,a=0,b=0,c=0,d=0,e=0):
#         self.a=a
#         self.b=b
#         self.c=c
#         self.d=d
#         self.e=e
#         print(self.a+self.b+self.c+self.d+self.e)

# math=Mathoperation()
# math.add(2,3)
# math.add(2,3,4)
# math.add(2,3,4,5)
# math.add(2,3,4,5,6)

# #inheritance
# class Parent:
#     def parent_property(self,money,land,gold):
#         self.money=money
#         self.land=land
#         self.gold=gold

# class Child(Parent): #parent inherit
#     def child_property(self,bike,car):
#         self.bike=bike
#         self.car=car

# child1=Child()
# child1.child_property("honda","suzuki")
# child1.parent_property("1crore","2acre","5kg")
# print(child1.money)
# print(child1.bike)
# print(child1.land)
# print(child1.car)


#
