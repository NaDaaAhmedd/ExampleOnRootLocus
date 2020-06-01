import matplotlib.pyplot as plt
import numpy as np
import math
import cmath
import sympy as sym
import warnings
warnings.filterwarnings("ignore",category=UserWarning)

fig = plt.figure()
fig.suptitle('Root Locus')
plt.axes().spines['left'].set_position(('data',0))
plt.axes().spines['bottom'].set_position(('data',0))
plt.axes().spines['right'].set_position(('data',0))
plt.axes().spines['top'].set_position(('data',0))
plt.xlim(-70,10)


#Drawing poles
x = [0,-25,-50,-50]
y = [0,0,10,-10]
plt.scatter(x, y, label= "poles", color= "red", marker= "X", s=100)

#Centroid and angles of the asymptotes
cen = (0-25-50-50)/4 
angle1 = ((2*0+1)/4)*180
angle2 = ((2*1+1)/4)*180
x = np.linspace(-50,50,1000)
asym1 = (math.tan(math.radians(angle1)))*x
asym2 = (math.tan(math.radians(angle2)))*x
plt.plot(x+cen, asym1, color='green', linestyle='dashed', linewidth = 2)
plt.plot(x+cen, asym2, color='green', linestyle='dashed', linewidth = 2)

#Break away points
s = sym.symbols('s')
func = -s*(s+25)*(s+complex(50,10))*(s+complex(50,-10))
diff_f = func.diff(s)
n = sym.Poly(diff_f,s)
breakawaypts = np.roots(n.all_coeffs())
plt.scatter(-20, 0, color= "b", marker= ">", s=70)
plt.scatter(-5, 0, color= "b", marker= "<", s=70)
plt.plot([0,-25], [0,0], color= "b", linewidth = 4)

#Intersection with imaginary axis
k = sym.symbols('k')
sub = (4580*65000-125*k)/4580
sol1 = sym.solve(sub)
aux = 4580*s**2+sol1[0]
n = sym.Poly(aux,s)
intsec = np.roots(n.all_coeffs())

#Angle of departure 
DepartureAngle = 180 - (180-math.degrees(math.atan(10/50)) + 90 + (180-math.degrees(math.atan(10/25)))) + 360
x = np.linspace(-2.5,0,10)
line1 = (math.tan(math.radians(DepartureAngle)))*x
plt.plot(x-50, line1+10, color='k', linestyle='dashed', linewidth = 2)
plt.plot([-50,-45],[-10,-10], color='k', linestyle='dashed', linewidth = 2)
line2 = (math.tan(math.radians(-DepartureAngle)))*x
plt.plot([-50,-45],[10,10], color='k', linestyle='dashed', linewidth = 2)
plt.plot(x-50, line2-10, color='k', linestyle='dashed', linewidth = 2)
plt.text(-49, 13, str(round(DepartureAngle,1)) + '°', fontsize=12,weight='bold')
plt.text(-49, -16, str(round(DepartureAngle,1)) + '°', fontsize=12,weight='bold')

#Changing k values, plotting root locus
for k in np.linspace(0,10000000,500):
  a = sym.Poly(func-k, s)
  sol = np.roots(a.all_coeffs())
  for x in range(len(sol)):
      plt.scatter([sol[x].real], [sol[x].imag], color= "blue",  
            marker= "o", s=10)
      
#Plotting the intersection with imaginary axis 
plt.scatter([0,0], [intsec[0].imag,intsec[1].imag], color= 'm', marker= "*", s=100)
plt.scatter(breakawaypts[2], 0, color= 'm', marker= "*", s=150)
plt.show()
