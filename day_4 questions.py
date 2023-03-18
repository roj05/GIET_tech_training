#write a python funtion, nearest palindrome() which accepts a number and returns the nearest palindrome greater than the given number.
'''import sys
def near_palindrome(n):
    for i in range(n+1,sys.maxsize):
        if str(i)==str(i)[:: -1]:
            return i
            
print(near_palindrome(99))
print(near_palindrome(1221))'''

#2
'''def max_visited_specialist(patient_medical_specialist_list,medical_specialist):
    max_visit=0
    P=patient_medical_specialist_list.count('P')
    E=patient_medical_specialist_list.count('E')
    O=patient_medical_specialist_list.count('O')
    if P>E and P>0:
        speciality=medical_speciality['P']
    elif E>0:
        speciality=medical_speciality['E']
    else:
        speciality=medical_speciality['O']
    return specialisty
patient_medical_specialist_list=[301,'P',302,'P',305,'P',401,'E',656,'E']
medical_specialist={'P':'Pediatrics','O':'Orthopedics','E':'ENT'}
speciality=(patient_medical_specialist_list,medical_specialist)
print(speciality)'''

#3
'''str1="I like Python"
str2="Java is a popular language"
def match(list1,list2):
    list3=[]
    for i in list1:
        for j in list2:
            if(i==j and i!=' ' and j!=' '):
                list3.append(j)
                break
        else:
            for i in list3:
                print(i,end='')
print(match(list1,list2))'''

#########
'''class Shoe:
    def __init__(self,price,material):
        self.price=price
        self.material=material
        def __str__(self):
            return "Shoe with price:"+str(self.price)+"and material:"+self.material
s1=Shoe(1000, "Canvas")
print(s1)'''

########
'''class Mobile:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
        self.total_price=None
    def purchase(self):
        if self.brand=="Apple":
            discount=10
        else:
            discount=5
        self.total_price=self.price-self.price*(discount/100)
        print("Total price of",self.brand, "Mobile is",self.total_price)
mob1=Mobile("Apple",200000)
mob2=Mobile("Samsung",100000)
mob1.purchase()
mob2.purchase()'''

########
class Customer:
    def __init__(self, cust_id, name, age, wallet_balance):
        self.cust_id=cust_id
        self.name=name
        self.age=age
        self.__wallet_balance=wallet_balance
    def set_balance(self,amount):
        if amount < 5000 and amount > 0:
            self.wallet_balance += amount
    def show_balance(self):
        print("The balance is", self.wallet_balance)
    def get_wallet_balance(self):
        return self.__wallet_balance
c1=Customer(100,"Gopal",24,1000)
print(c1.get_wallet_balance())
c1.set_balance(5000)
#print()'''

######
class dam:
    def __init__(self,name,length):
        self.name=name
        self.__length=length
    def get__length(self):
        
        
        


























