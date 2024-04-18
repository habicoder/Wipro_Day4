class Car:  

    def __init__(self,mname, yr):  
        self.modelname = mname  
        self.year = yr  
 
 
    def display(self):  
        print(self.modelname,self.year)  
c1 = Car("Suzuki", 2018)  
c1.display()  
 
 
c2=Car("Mercedes-Benz",2020)
c2.display()