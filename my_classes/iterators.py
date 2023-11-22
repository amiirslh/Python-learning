class PowTwo:
    def __init__(self,max_pow):
        self.n=0
        self.max_pow=max_pow

    def __iter__(self):
        """دو تا راه نوشتم براش : یدونش اینه یدونه اش تابع پایننی که کامنت شده"""
        z=0
        for i in range(self.n,self.max_pow+1):
            z=i**2
            i+=1
            yield z
    def __iter__(self):
        """کخ خب صد درصد این بهتره و پویا تره"""
        return self


    def __next__(self):
        if self.n <= self.max_pow:
            result = self.n**2
            self.n +=1
            return result
        else:
            raise StopIteration
a=PowTwo(5)
print(next(a))
print(next(a))
print('-'*10)
for i in a:
    print(i)