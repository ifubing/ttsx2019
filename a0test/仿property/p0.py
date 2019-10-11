class Deco:
    def __init__(self, x):
        self.x = x


class Cat:
    @Deco
    def place(self):
        return '武汉'


t = Cat()
res = t.place

print(res)
