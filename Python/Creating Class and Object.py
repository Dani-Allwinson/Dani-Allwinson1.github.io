class Robot:
    def __init__(self,name,color,weight):
        self.name = name
        self.color = color
        self.weight = weight


    def introduce_self(self):
        print("My Name is " + self.name)
        print("My Lovable Color is " + self.color)
        print("My Weigth is " + self.weight)


r1 = Robot("dani" , "white" , "20")
r2 = Robot("allwin" , "black" , "13")

r1.introduce_self()
r2.introduce_self()
