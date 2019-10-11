class Father:
    def run(self):
        print('fa run')

    @classmethod
    def test(cls):
        print('father test')

    @classmethod
    def as_view(cls,**kwargs):
        print('father as_view')
        o = super(Father, cls)
        print('o', id(o))
        print(o.test())


class Other:
    @classmethod
    def as_view(**kwargs):
        print('other, as view')

    @classmethod
    def test(cls):
        print('other test')


class Son(Father, Other):
    def so(self):
        print('son的so方法')

    @classmethod
    def test(cls):
        print('son test')


Son.as_view()
print('son id', id(Son))
print('father id', id(Father))
print('other id', id(Other))