class attendence:
    def __init__(self,name,mark,subject):
        self.name = name
        self.mark = mark
        self.subject = subject
    def introduce_self(self):
        print("my name is " + self.name)
        print("my marks is " + self.mark)
        print("my subject is " + self.subject)
r1 = attendence("dani" , "76" , "maths" )
r2 = attendence("abi" , "2" , "physics" )
class rollno:
    def __init__(self,rollno):
        self.rollno = rollno
    def introduce_self(self):
        print("my rollno is " + self.rollno)
        print("my rollno is " + self.rollno)
rn1 = rollno("19bee076")
rn2 = rollno("19bee000")

rn1.attendence_owned = r1
rn2.attendence_owned = r2 

rn1.attendence_owned.introduce_self()
rn2.attendence_owned.introduce_self()


