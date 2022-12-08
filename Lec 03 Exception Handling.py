from ExceptiocClasses import NegativeValueError,XYZError
def a():
    print("One")
    in_=None
    flag=False
    while flag==False:
        try:
            in_=input("Enter Number")
            in_=int(in_)
            flag=True
        except ValueError as e:
            print(str(e))
            print("Invalid input please re-enter")

    print("done")
    return in_

def b():
    print('Hello')
    v=a()
    v2=a()
    if v < 0 or v2<0:
        #raise NegativeValueError("Negative values not allowed")
        error=NegativeValueError("Negative values not allowed")
        raise error
    div=v/v2

    print(div)
    print("bye")

try:
    b()
    print("b is done")
except ZeroDivisionError as e:
    print("You are trying to divide be zero its not allowed")
except ValueError as e:
    print(str(e))
except NegativeValueError as e:
    print("You entered values voilating are business rules")
    print(str(e))

except Exception as e:
    print(str(e))
finally:
    print("Always")

print("All done")








def a():
    flag=False
    while(flag==False):
        try:
            inp=input("Enter a value: ")
            inp=int(inp)
            return inp
            flag=True
        except ValueError as e:
            print("Invalid Input.")
            print(str(e))
v=a()
if v!= None:
    print(v)





 def TakeVal():
    inp=input("Enter a value: ")
    inp=int(inp)
    if inp<0:
        error = ValueError("You entered negative value")
        raise error
    return inp

try:
    inp=TakeVal()
    print(inp)
except ValueError as e:
    print(str(e))



def DivisionVal():
    try:
        inp=input("Enter a value: ")
        inp=int(inp)
        inp2 = input("Enter another value: ")
        inp2 = int(inp2)
    except ValueError as e:
        print(str(e))
        return
    try:
        result=inp/inp2
        return result
    except ZeroDivisionError as e:
        print(str(e))

inp=DivisionVal()
while inp==None:
    print("")
    inp = DivisionVal()
print(inp)