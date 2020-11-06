'''#dictionary
#dictionary is used to store and implement a data in a key value pair in python
#dictionary is the data type in python which can simulate the real life data arragement wher some specific value exist for some particular keys


Employee = {"Name":"Kushal","Age":23,"Salary":200000.00}
print(type(Employee))
print(Employee)

#Accessing the value of dictionary
print("Name of the employee is :",Employee["Name"])
print("Age of the employee is :",Employee["Age"])
print("Salary of the employee is :",Employee["Salary"])


#updating
Employee["company"] = "Google"
print("Company of the employee is :",Employee["company"])

'''
#create a dictionary of 25 words with their meaning
words = {"A":"1","B":"2","C":"3","D":"4","E":"5","F":"6","G":"7","H":"8","I":"9","J":"10","K":"11","L":"12","M":"13","N":"14","O":"15","P":"16","Q":"17","R":"18","S":"19","T":"20","U":"21","V":"22","W":"23","X":"24","Y":"25"}
l =[]
i=1
flag = 0
while(i != 0):
    s = input("enter key to be searched")
    for x,y in words.items():
       if x == s:           
             print(y)
             l.append(x)
             flag = 1
    if (flag == 0):
      print("Element not FOund!")
      break
    #else:
      #print("not found")
      
    i=int(input("for more search  press 1 and  0 for exit"))
print(l)
    
#fuction
#funtion is a self block of code which is used to organise the functional code
#fuction can be called as section of a program that is written ones and can be used and can be executed whenever required in the program
#types of function

