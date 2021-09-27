import matplotlib.pyplot as plt
import numpy as np
import math

x = np.linspace(-10,10,num=100)
plt.plot(x,np.exp(x),label="exp(x)",color="firebrick")

y = x**0
plt.plot(x,y,label="n=0",color="lightblue")

y = y + x
plt.plot(x,y,label="n=1",color="skyblue")

y = y + x**2 / math.factorial(2)
plt.plot(x,y,label="n=2",color="deepskyblue")

y = y + x**3 / math.factorial(3)
plt.plot(x,y,label="n=3",color="cornflowerblue")

y = y + x**4 / math.factorial(4)
plt.plot(x,y,label="n=4",color="royalblue")

y = y + x**5 / math.factorial(5)
plt.plot(x,y,label="n=5",color="blue")

y = y + x**6 / math.factorial(6)
plt.plot(x,y,label="n=6",color="midnightblue")

plt.xlim(-10,10)
plt.ylim(-1,3)

plt.title("exp(x) Maclaurin Expansion")

plt.axhline(0, color="black")
plt.axvline(0, color="black")

plt.xlabel("x")
plt.ylabel("y")

plt.legend()
plt.show()