def deco(func):
    def inner():
        print(111)
        func()
        print(2222)
    return inner

@deco  # one=deco(one)
def one():
    print('页面跳转到用户中心')

@deco
def two():
    print('func two')

@deco
def three():
    print('func three')


# one()
print(deco(one))
# 装饰器（功能函数）   ----> 被装饰后的 功能函数
one()