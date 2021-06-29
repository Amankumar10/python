def add(a,b):
    sum =a+b
    return sum

def sub(a,b):
    sub=a-b
    return sub

def mul(a,b):    
    mul=a*b
    return mul

def div(a,b):
    div=a/b
    return div

#Take input from the user
a =int(input("enter the first number  "))
b= int(input("enter the secound number"))
c= input("press + for add or - for sub or * for mul or \ for div")
if c=="+":
    print(add(a,b))
elif c=="-":
    print(sub(a,b))    
elif c=="*":
    print(mul(a,b))    
elif c=="/":    
    print(div(a,b))
else:
    print("invailde input")
