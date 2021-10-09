y0 = int(input("Enter your YO: "))

xf = int(input("Enter your Xf: "))
p0=y0
n = int(input("Enter your iteration number: "))
x = np.linspace(x0,xf,n)
def func( x,y):
    return (x + y)
y = np.zeros([n])
y[0] = y0
h= (xf-x0)/(n-1)
h2= 2*(xf-x0)/(n-1)
p=np.zeros([n])
p[0]=p0
for i in range(1, n):
     y[i] = h * func(x[i - 1], y0) + y0
     y0 = y[i]
     print(y)
     x[i]=x0
     x0 = x0 + h


for i in range(1, n):
     p[i] = h2 * func(x[i - 1], p0) + p0
     p0 = p[i]
     print(p)
     x[i]=x0
     x0 = x0 + h


y_true= -x-1+np.exp(x)

print("x_n\t\t    y_n\t\t    y-true\t\t   P_n")
print("-------------------")
for i in range(n):
	print(format(x[i],'6f'),"\t",format(y[i],'6f'),"\t",format(y_true[i],'6f'),"\t",format(x[i],'6f'))
#plt.plot(x,y,'b.-',x,y_true,'r-')
plt.plot(x, y ,'b.-', x, y_true , 'r-', x, p, 'g,-')
plt.grid(True)
plt.xlabel("Value of x")
plt.ylabel("Value of y")

plt.title("Approximation Solution with Euler's Method")
plt.show()
