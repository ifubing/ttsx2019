class Father:
    def __init__(self):
        self.name = 'father'
    def run(self):
        print('father de run')
        # o = super()
        o = super(Father, self)
        o.teach()

    def one(self):
        print('father de one')

class Mother:
    def one(self):
        print('mother de one')


class Teacher:
    def __init__(self):
        self.name = 'teacher'
    def teach(self):
        print('老师的实例方法，teach方法', self.name)
        print('teach self id',id(self), self)


class Son(Father,Mother,Teacher):
    def __init__(self):
        self.name = 'son'


s = Son()
print('s obj id', id(s), s)
s.run()



