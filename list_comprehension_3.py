#List comprehension

#for loop version
"""result=[]
for i in range(11):
    result.append(i)
print(result)
#list_comprehension
print([i for i in range(11)])
#for loop versin-->odd elements
result=[]
for i in range(11):
    if i%2!=0:
        result.append(i)
print(result)
print([i for i in range(11)if i%2!=0])


result=[]
for i in range(11):
    if i%2!=0:
        result.append(i)
    else:
        result.append(i**2)
print(result)
print([i if i%2!=0 else i**2 for i in range(11)])"""

#2
#mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
#for loop-->square it-->odd
#even-->cube it
"""mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
result=[]
for i in mat:
    for j in i:
        if j%2!=0:
            result.append(j**2)
        else:
            result.append(j**3)
print(result)
list2=[j**2 if j%2!=0 else j**3 for i in mat for j in i]
print(list2)
print(j**2 if j%2!=0 else j**3 for i in mat for j in i)
print([[j**2 if j%2!=0 else j**3 for j in i] for i in mat])"""


#for each number in list_b,get the number and its position(index) in myList as return list of tuples
"""list1=[9,3,6,1,5,0,8,2,4,7]
list2=[6,4,6,1,2,2]
result=[]
for i in list2:
    result.append((i,list1.index(i)))
print(result)
print([(i,list1.index(i))for i in list2])
#dict_comprehension
print(dict([(i,list1.index(i))for i in list2]))"""

#3
#the goal is to tokenize the following 5 sentence into words, excluding the stopwords.
#input:sentence=["a new world record was set","in the holy city of ayodhya","on the eve of diwali tuesday","with over three of diya or earthen lamps"
#"lit up simultaneously on the banks of the river sarayu"]
"""sentences=["a new world record was set","in the holy city of ayodhya","on the eve of diwali tuesday","with over three of diya or earthen lamps",
          "lit up simultaneously on the banks of the river sarayu"]
stopword=['for','a','of','the','and','to','in','on','with','was']
result=[]
for sentence in sentences:
    row_data=[]
    for word in sentence.split():
        if word not in stopword:
            row_data.append(word)
    result.append(row_data)
print(result)"""

#4
#input a string of seperated numbers. The number 5 and 8 are present in list.assume that 8 always comes after 5.
#case1: num1=add all the numbers which do not lie between 5 and 8 in the input.
#case2: num2=number formed by concatenate all numbers from 5 to 8
'''array=list(map(int,input().split(",")))
number1=sum(array[:array.index(5)])+sum(array[array.index(8)+1:])
l=array[array.index(5):array.index(8)+1]
number2=""
for i in l:
    number2+=str(i)
print(int(number2)+number1)'''

#5
#string rotation
s=input().split(",")
stt=[]
numm=[]
for i in s:
    s1,n=i.split(":")
    stt.append(s1)
    numm.append(n)
def rotate(ss,n):
    n=str(n)
    s=0
    for i in n:
        s+=int(i)**2
    if s%2==0:
        return ss[-1]+ss[:-1]
    else:
        return ss[2:]+ss[:2]
for i in range(len(numm)):
    print(rotate(stt[i],numm[i]))
    
    
    
        
    































