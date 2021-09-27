import matplotlib.pyplot as plt
import numpy as np
import math

x = np.linspace(-5,10,num=100)
plt.plot(x,np.log(x),label="log(x)",color="firebrick")
cmap = plt.get_cmap("Blues")

y = x-1
plt.plot(x,y,label="n=1",color=cmap(25))

#y = y +(((-1)**(i+1))*(x-1)**i)/i

y = y - (x-1)**2 / 2
plt.plot(x,y,label="n=2",color=cmap(25*2))

y = y + (x-1)**3 / 3
plt.plot(x,y,label="n=3",color=cmap(25*3))

y = y - (x-1)**4 / 4
plt.plot(x,y,label="n=4",color=cmap(25*4))

y = y + (x-1)**5 / 5
plt.plot(x,y,label="n=4",color=cmap(25*5))

y = y - (x-1)**6 / 6
plt.plot(x,y,label="n=6",color=cmap(25*6))

y = y + (x-1)**7 / 7
plt.plot(x,y,label="n=7",color=cmap(25*7))

y = y - (x-1)**8 / 8
plt.plot(x,y,label="n=7",color=cmap(25*8))

y = y + (x-1)**9 / 9
plt.plot(x,y,label="n=7",color=cmap(25*9))

y = y - (x-1)**10 / 10
plt.plot(x,y,label="n=7",color=cmap(25*10))

plt.xlim(-5,10)
plt.ylim(-2,5)

plt.title("log(x) Maclaurin Expansion")

plt.axhline(0, color="black")
plt.axvline(0, color="black")

plt.xlabel("x")
plt.ylabel("y")

plt.legend()
plt.show()