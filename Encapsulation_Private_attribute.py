class Students:
    def __init__(self,name,number):
        self.name = name
        self.__number = number
    
    def get_number(self):
        return self.__number
    
    def set_number(self,value):
        if value > 0:
            self.__number = value
        else:
            return "Invalid number"
            
s_1 = Students("Malcolm", 20260895)
print("Student name: ", s_1.name)
print(s_1.get_number())
        