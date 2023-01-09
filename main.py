def divide(x, y):
    return x / y

def multiply(x, y):
    return x * y

def addition(x, y):
    return x + y

def subtract(x, y):
    return x - y

def exponents(x, y):
    return x**y

def square_root(x):
    import math
    square_root = (math.sqrt(x))
    return square_root


print("Choose Math function" )
application=["1.divide","2.multiply","3.addition","4.subtract","5.exponents","6.Square root"] 
for x in application:
  print(x)


while True:
    Choice=input("Enter choice (1/2/3/4/5/6/):")
    if Choice in ('1','2','3','4','5','6',):
      num1=float(input("Enter your first number"))
      num2=float(input("Enter your first number"))

      if Choice=='1':
        print(num1,"/",num2,"=",divide(num1,num2))

      elif Choice=='2':
        print(num1,"*",num2,"=",multiply(num1,num2))
      
      elif Choice=='3':
        print(num1,"+",num2,"=",addition(num1,num2))

      elif Choice=='4':
        print(num1,"-",num2,"=",subtract(num1,num2))

      elif Choice=='5':
        print(num1,"**",num2,"=",exponents(num1,num2))

      elif Choice=='6':
        print(num1,"sqrt","=",square_root(num1))


      satisfaction=input("do you want to do another calculation? (yes/no):")
      if satisfaction=="no":
        break

else:
  print("Invalid input")