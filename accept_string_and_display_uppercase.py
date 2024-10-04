class MyClass:
    def Get_String(self):
        self.MyStr=input("Enter any String: ")
    def Print_String(self):
        print("String in Upper Case: " ,self.MyStr.upper())
# main body
Obj=MyClass()
Obj.Get_String()
Obj.Print_String()