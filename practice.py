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


