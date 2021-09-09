class road:
    def __init__(self):
        self.lenght=0
        self.width=0
class TCar:
    def __init__(self,road0,p0,v0):
        self.road=road0
        self.p=p0
        self.v=v0
        self.X=0
    def move(self):
        self.X+=self.v
        if self.X>self.road.lenght:
            self.x=0

N=3
cars=[]
for i in range(N):
    cars.append(TCar(road, i+1 , 2*(i+1)))
print("100")
for i in range(3):
    print(cars[i].X)
