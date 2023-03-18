#1
"""def function(str1):
    l_count=0
    d_count=0
    for i in str1:
        if i.isalpha():
            l_count=l_count+1
        elif i.isdigit():
            d_count=d_count+1
        else:
            continue
    return[l_count,d_count]
print(function("Infosys 123"))"""

#2
"""def pair_of_no(num,n):
    count=0
    for x in num:
        index=num.index(x)+1
        for y in range(index,len(num)):
            if x+num[y]==n:
                count+=1
                break
    return count
num=[1,2,7,4,5,6,0,3]
n=6
print(pair_of_no(num,n))"""

#3
"""def function(str1):
    if len(str1)<2:
        return -1
    else:
        return str1[0:2]+str1[-2:]



print(function("w3resource"))
print(function("w3"))
print(function("A"))"""

#4
"""def function(str1):
    length=len(str1)

    
    if len(str1)>2:
        if str1[-3:]=='ing':
            str1+='ly'
        else:
            str1+='ing'
    return str1
print(function("sleep"))
print(function("amazing"))
print(function("is"))"""

#5
"""def double_check(number):
    num1=str(number*2)
    number=str(number)
    count=0
    for x in number:
        if x in num1:
            count+=1
        else:
            return false
    if count==len(number):
        return True    
print(double_check("4"))
print(double_check("125847"))"""

#6
"""def average(a):
    count=0
    avg=sum(a)//len(a)
    for i in a:
        if(i>avg):
            count+=1
    return(count*100//len(a))
print(average((12,18,25,24,5,2,20,20,21,18)))
def frequency(a):
    list1=[]
    count=0
    for i in range(0,26):
        list1.append(a.count(i))
    return list1
print(frequency((12,18,25,24,5,2,20,20,21,18)))
def marks(a):
    return sorted(a)
print(marks((12,18,25,24,5,2,20,20,21,18)))"""

#7
"""def trans(dict1,list1):
    list2=[]
    for i in list1:
        list2.append(dict1[i])
    return list2
dict1={"merry":"god","christmas":"jul","and":"och","happy":"gott","new":"nytt","year":"ar"}
list1=["merry","christmas"]
print(trans(dict1,list1))"""

#8
n1=int(input("Enter a value of n1"))
n2=int(input("Enter a value of n2"))
result=[]
for i in range(n1,n2+1):
    result.append(i)
print(result)
result=[i for i in range(n1,n2+1)]
print(result)
array=[i for i in range(n1,n2+1)]
print(array)
for i in range(len(array)):
    for j in range(i,len(array)):
        result.append(array[i:j+1])
print(result)
result=[array[i:j+1] for i in range(len(array))for j in range(i,len(array))]
print(result)
c=0
for i in result:
    if sum(i)%2!=0:
        c+=1
print(c)
    
    
        
            


    
    
    
