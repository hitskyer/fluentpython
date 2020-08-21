def deco(func):
    print('deco')
    def inner():
        print('running inner()')
    return inner
@deco
def target():
    print('running target()')
if __name__ == '__main__':
    print('main')
    target()
    print(target)