from functools import update_wrapper
class MyClassDec:

    def __init__(self,func):
        update_wrapper(self,func)
        self.func=func
    def __call__(self):
        print('amiiiiiiiiiiiiiiiiiiiiiiiiir')
        return self.func()

@MyClassDec
def my_func():
    '''amirhossein khare'''
    print('amirhossein')

my_func()