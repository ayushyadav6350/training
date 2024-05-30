# exception ending
#x=41
#if x>10:
#    print("above ten")
#    pass
#    if x>20:
#      print("above 20")
num1=int(input("enter the number:"))
num2=int(input("enter the number"))
try:
    print("program is running")
    result = num1/num2
    print("program is executed")
    print("the result of division is",result)

except Exception as e:
    print("as get an error")
    print(e)

else:
    print("no exception found")

finally:
    print("hello world")