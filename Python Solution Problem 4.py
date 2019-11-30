#machine problem 4 - trajectory of projectile motion 
import math as math
from matplotlib import pyplot as plt

def trajectory(yi, vi, angle, ax, ay):
    if ay == 0:
        print('ERROR! There is no free fall with zero vertical acceleration')
        return
    
    #find initial velocity in x and y
    vix = vi * math.cos(angle * (math.pi/180))
    viy = vi * math.sin(angle * (math.pi/180))
    
    #store x and y values
    xvalue = []
    yvalue = []
    
    #initiate values
    dt = 0.01
    t = 0
    x = 0
    y = yi
    xvalue.append(x)
    yvalue.append(y)
    
    #looping statement
    while(True):
        t = t + dt
        
        x = vix*t + (0.5) * ax * (t ** 2)
        y = yi + (viy*t + (0.5) * ay * (t ** 2)) 
        
        xvalue.append(x)
        yvalue.append(y)
        
        if y <= 0:
            break
     
    #plotting
    plt.plot(xvalue, yvalue, 'g', linewidth=3)
    plt.grid()
    plt.xlabel('X-AXIS')
    plt.ylabel('Y-AXIS')
    plt.title('MACH PROB 4 - TRAJECTORY OF A PROJECTILE MOTION')
    plt.show()
    
    