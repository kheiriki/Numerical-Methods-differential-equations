import numpy as np
from matplotlib import pyplot as plt

x0 = int(input("Enter your X0: "))

y0 = int(input("Enter your YO: "))

xf = int(input("Enter your Xf: "))

n = int(input("Enter your iteration number: "))
x = np.linspace(x0,xf,n)
def func( x,y):
    return (x + y)
y = np.zeros([n])
y[0] = y0
h= (xf-x0)/(n-1)
for i in range(1, n):
     y[i] = (1/2)*h *( func(x[i - 1], y0)+func(x[i], y0+h*func(x[i-1],y0))) + y0
     y0 = y[i]
     print(y)
     x[i]=x0
     x0 = x0 + h


y_true= -x-1+np.exp(x)

print("x_n\t\t    y_n\t\t    y-true")
print("-------------------")
for i in range(n):
	print(format(x[i],'6f'),"\t",format(y[i],'6f'),"\t",format(y_true[i],'6f'))
#plt.plot(x,y,'b.-',x,y_true,'r-')
plt.plot(x, y ,'b.-', x, y_true , 'r-')
plt.grid(True)
plt.xlabel("Value of x")
plt.ylabel("Value of y")
plt.title("Approximation Solution with Modified Euler's Method")
plt.show()

