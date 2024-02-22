class ListMetaclass(type):
    def __new__(cls,name,bases,attrs):
        attrs['add'] = lambda value:cls.append(value)
        return type.__new__(cls,name,bases,attrs)
    
class MyList(list,metaclass = ListMetaclass):
    pass


L = MyList
L.add(1)
print(L)