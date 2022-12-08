print("Hello World")
v=6
v2=3.5
v3="Hello"
print(type(v))
print(type(v2))
print(type(v3))
#value=input("Enter value")
'''
print(value)
print(type(value))
value_=int(value)
print(type(value_))
'''
i=0
while i<=10:
    print(i)
    if i%2==0:
        print("even")
    elif i==7:
        print("some special number")
    else:
        print("not even")
    i = i + 1

for i in range(10):
    print(i)

for i in range(100,10,-4):
    print(i)
############# Function definition ############
def myFirstFunction():
    print("My First Function")

myFirstFunction()

def sum(v1,v2):
    return v1+v2

print(sum(v,10))
s_=sum(v,v2)
print(s_)
print(type(s_))

def power(a, b):
    temp = a
    for i in (1, b):
        temp = temp*a
    return temp

print(power(2, 3))



arr=[1,10,8,6,5,0,3.6]
for el in arr:
    print(el)

print(len(arr))
arr.append(3.3)
arr.pop(2)
arr.sort()
for el in arr:
    print(el)

def maxNo(l):
    num = 0
    for i in l:
        if(num < i):
            num = i
    return num
list1 = [1,2,3,4,5,6]
print("maximum number: ", maxNo(list1))
list2=[1,9,78]
list3=list1+list2
for element in list3:
    print(element)

print(3**5)