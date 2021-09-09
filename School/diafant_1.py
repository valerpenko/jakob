#10*h-2t=180           h<=21
import math
for h in range(1,22):
    t=(10*h-180)/2
    if t>=0 and t==math.trunc(t):
        print(h,t)