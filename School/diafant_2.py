
import math
for x in range(1,12):
    y=(150-13*x)/9
    if y==math.trunc(y):
        print(x,y)