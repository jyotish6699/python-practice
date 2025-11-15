# # a=4.3
# # b=4
# # print("a=%d#b=%.2f" % (a, b))

# # print(0b11)
# # print(0o11)
# # print(0x11)
# # print(0x1f)
# # print(ord("a"))
# # print(chr(97))
# # print(ord("A"))
# # sky value or unicode value
# # A=65 to Z=90
# # a=97 to z=122
# # a=4.5
# # b=4
# # print("a=%d"%a,"b=%.2f"%b)
# # print("a=%d#b=%.2f" % (a, b))
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
# print(list4)\
# #iteration of list
# enumerate(list1)
# zip(list1,list2)
# print(zip(list1,list2))










# #number formatting
# # a=5
# # b=3
# # list=[1,2,3,4,5,6,7,8,9,10]
# # print("a=%d#b=%.2f"%(a,b))
# # print(f"a={a}#b={b}")
# # #filtering even number from list
# # print([i for i in list if i%2==0])
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
# nested loop

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

#list1=[2,3,4,5,6,7,8]
# #map function
# def squares(x):
#     return x**2
# m=list(map(squares,list1))
# print(m)

#filter function
 
# list2=list(filter(lambda x:x%2==0,list1))
# print(list2)

#reduce function


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
print("save point-2")

