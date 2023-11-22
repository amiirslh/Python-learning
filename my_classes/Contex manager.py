class C:

    def __enter__(self):
        print('enter')
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit')

c=C()
with c:
    print('amir')

print('-' * 40)

class A:
    def __init__(self,func):
        self.func=func
    def __call__(self):
        print('enter')
        self.func()
        print('exit')
        return self.func
@A
def function():
    print('amir')
function()


class FileManager:

    def __init__(self,filename,mode):
        self.filename=filename
        self.mode=mode
        self.file=None

    def __enter__(self):
        print('The file was opened')
        self.file =open(self.filename,self.mode)
        return self.file


    def __exit__(self, exc_type, exc_val, exc_tb):
        print('the file is closed')
        self.file.close()


with FileManager('amir','w') as f:
    f.write('I love you')