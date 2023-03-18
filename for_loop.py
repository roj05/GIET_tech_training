"""for i in range(1,101):
    print(i,end=' ')
print()
for i in range(1,101,2):
    print(i,end=' ')
for i in range(2,101,2):
    print(i,end=' ')"""



#100 to 1
"""for i in range(100,0,-1):
    print(i,end=' ')
for i in range(100,0,-2):
    print(i,end=' ')
for i in range(99,0,-2):
    print(i,end=' ')"""




#break_statement
"""for i in range(1,101):
    if i==50:
        break
    print(i,end=' ')

else:
    print("else statement")"""

#continue_statement
"""for i in range(1,101):
    if i==50:
        continue
    print(i,end=' ')

else:
    print("else statement")"""

#pass_statement:- null statement
"""for i in range(1,101):
    if i==50:
        pass
    print(i,end=' ')
    
else:
    print("else statement")"""

#functions
"""def function1():
    print("its a function1")
function1()
def function2(num1,num2):
    print("num1=",num1,"num2=",num2)
        #print()__str__
function2(10,20)"""


"""def function1():
    print("its a function1")
function1()
def function2(num1,num2):
    print("num1=",num1,"num2=",num2)
        #print()__str__
function2(10,20)
def function3(num1,num2):
    num3=num1+num2
    return num3
print("value returned", function3(100,200))"""


"""def function1():
    print("its a function1")
function1()
def function2(num1,num2):
    print("num1=",num1,"num2=",num2)
        #print()__str__
function2(10,20)
def function3(num1,num2):
    num3=num1+num2
    return num3
print("value returned", function3(10,20.2))
def function5(num1,num2):
    num3=float(num1)+num2
    return num3
print("value returned",function5('10',20.2))"""


#categories of function
#based on arguments
#1:Positional arguments
"""def function1(num1,num2,num3,num4):
    print("num1",num1,"num2",num2,"num3",num3,"num4",num4)
function1(10,20,30,40)
function1(100,200,300,400)"""


#2:keyword_argument
"""def function2(num1,num2,num3,num4):
    print("num1",num1,"num2",num2,"num3",num3,"num4",num4)
function2(num4=10,num1=20,num2=30,num3=40)
function2(num4=10,num1=10,num2=70,num3=100)"""


#3default_arguments
"""def function3(name,rollno,branch,collegname):
    print(name,rollno,branch,collegname)
function3("Khyati",397,"CSE","GIET")
function3("Ashu",398,"ECE","GIET")
function3("Bhavya",396,"CST","GIET")
function3("Ishika",395,"CSE","GIET")"""


#4: variable no of argument
"""def function4(*var):
    for i in var:
        print(i,end=' ')
function4(10,20)
print()
function4(10,20,30,40)
print()
function4(10,20,30,40,50,60)"""


def add(*var):
    sum1=0
    for i in var:
        sum1=sum1+i
    return(sum1)
print(add(10,20))
print(add(10,20,30,40))
print(add(10,20,30,40,50,60))























    

    
