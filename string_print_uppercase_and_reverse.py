class MyClass:
    def Get_String(self):
        self.MyStr=input("Enter any String: ")
    def Print_String(self):
        s=self.MyStr
        print("String in Upper Case: " , s.upper())
        cnt=len(s)
        i=cnt-1
        RevStr=""
        while(i >= 0):
            RevStr=RevStr + s[i]
            i=i-1
        print("String in Reverse & Lower case:" , RevStr.lower())

Obj=MyClass()
Obj.Get_String()
Obj.Print_String()