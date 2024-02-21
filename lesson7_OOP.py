class Student(object):
    def __init__(self,name,score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name,self.__score))

    def get_name(self):
        return self.__name
    
    def set_name(self,name):
        self.__name = name

    def get_score(self):
        return self.__score    
    
    def set_score(self,score):
        self.__score = score


class Student1(object):
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender

    def get_gender(self):
       return self.__gender

    def set_gender(self,gender):
       self.__gender = gender 

student1 = Student1('simba','male')




class Animal(object):
    def run(self):
        print('%s is runing' % self.name)


class Dog(Animal):
   def __init__(self,name = 'dog'):
       self.name = name

dog = Dog()
dog.run()


def set_age(self,age):
    self.age = age
from types import MethodType
s = Student('simba',90)
s.age = 18
print(s.age)
s.set_age =MethodType(set_age,s)
s.set_age(20)
print(s.age)

class Screen(object):
    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self,value):
        self.__width = value

    @property
    def height(self):
        self.__height    

    @height.setter
    def height(self,value):
        self.__height = value

    @property
    def resolution(self):
        return self.__width * self.__height
