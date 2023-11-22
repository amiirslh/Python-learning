from math import sqrt

class Point:

    def __init__(self,x=0,y=0)->None:
        self.x=x
        self.y=y

    def move(self,x,y):
        self.x=x
        self.y=y

    def reset(self):
        self.move(0,0)
    def dis(self,other):
        return sqrt((self.x-other.x)**2+(self.y-other.y)**2)
point:Point=None
def get_point():
    global point

    point=Point()
    return point




def main():
    if __name__ == '__main__':
        a = get_point()
        a.move(10, 11)
        print((a.x, a.y))


