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

print(dir(student1))


class Animal(object):
    def run(self):
        print('%s is runing' % self.name)


class Dog(Animal):
   def __init__(self,name = 'dog'):
       self.name = name

dog = Dog()
dog.run()