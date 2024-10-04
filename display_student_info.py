class Student:
 def GetStudent(self):
    self.RollNo=int(input("\nEnter Student Roll No:"))
    self.Name=input("Enter Student Name:")
    self.Age=int(input("Enter Student Age:"))
    self.Gender=input("Enter Student Gender:")
 def PutStudent(self):
    print("Student Roll No:",self.RollNo)
    print("Student Name:",self.Name)
    print("Student Age:",self.Age)
    print("Student Gender:",self.Gender)

class Test(Student):
 def GetMarks(self):
    self.MarkMar=int(input("Enter Marks of Marathi Subject"))
    self.MarkHin=int(input("Enter Marks of Hindi Subject"))
    self.MarkEng=int(input("Enter Marks of Eglish Subject"))
 def PutMarks(self):
    print("Marathi Marks:", self.MarkMar)
    print("Hindi Marks:", self.MarkHin)
    print("English Marks:", self.MarkEng)
    print("Total Marks:",self.MarkMar+self.MarkHin+self.MarkEng)

n=int(input("Enter How may students"))
lst=[]
for i in range(0,n):
    obj=input("Enter Object Name:")
    lst.append(obj)
    print(lst)
for j in range(0,n):
    lst[j]=Test()
    lst[j].GetStudent()
    lst[j].GetMarks()
print("\nDisplay Details of Student",j+1)
lst[j].PutStudent()
lst[j].PutMarks()