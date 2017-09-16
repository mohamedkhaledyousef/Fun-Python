class Parent():
    def __init__(self,last_name,eye_color):
        print("Parent Constructor Called")
        self.last_name = last_name
        self.eye_color = eye_color

#Object
#mohamed_khaled = Parent("Khaled","Blue")

#print(mohamed_khaled.last_name)
#Output
#Parent Constructor Called
#Khaled


#inheritance ... class Child
class Child(Parent):     #means class Child will inherit or reuse every thing in class Parent
    def __init__(self,last_name,eye_color,number_of_toys):
        print("Child Constructor Called")
        Parent.__init__(self,last_name,eye_color)   #to inherit from parent class,we will reuse class parent's init method 
        self.number_of_toys = number_of_toys        #to initialize the last object variable



#create objects of class Child
mohamed_khaled = Child("Khaled","blue",5)
print(mohamed_khaled.last_name)
print(mohamed_khaled.number_of_toys)

#Output
#Child Constructor Called
#Parent Constructor Called
#Khaled
#5
