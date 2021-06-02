'''class myclass:
    x=5
p1=myclass()      #Create Object
print(p1.x)
'''


class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def myfunc(self):
        print("hello my name is "+self.name)

p1=person("BAnsi",21)
p1.myfunc()