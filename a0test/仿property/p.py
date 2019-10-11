class Desc:
    def __get__(self, instance, owner):
        print('get')
        return instance.__dict__['name']

    def __set__(self, instance, value):
        print('set')
        print('instance', instance)
        print('value', value)
        instance.__dict__['name'] = value



class Cat:
    name = Desc()


tom = Cat()
print('tom', tom)
tom.name = '汤姆猫'
print(tom.__dict__)
print(tom.name)
