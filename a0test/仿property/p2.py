class Deco:
    def __init__(self, func):
        self.func = func
        print('deco', func)


    def __get__(self, instance, owner):
        print(instance)
        print(owner)
        print(self.func)
        res = self.func(instance)
        return res

class Cat:
    @Deco  #place = Deco(place)
    def place(self):
        return '武汉'

t = Cat()
res = t.place
print(res)