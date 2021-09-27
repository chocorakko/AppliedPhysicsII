
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10,10,num=100)
plt.plot(x,np.sin(x),label="sin(x)",color="firebrick")

y = x
plt.plot(x,y,label="n=1",color="lightblue")

y = y - x**3 / 6 
plt.plot(x,y,label="n=3",color="skyblue")

y = y + x**5 / 120
plt.plot(x,y,label="n=5",color="deepskyblue")

y = y - x**7 / 5040
plt.plot(x,y,label="n=7",color="cornflowerblue")

y = y + x**9 / 362880
plt.plot(x,y,label="n=9",color="royalblue")

y = y - x**11 / 39916800
plt.plot(x,y,label="n=11",color="midnightblue")

plt.xlim(-10,10)
plt.ylim(-10,10)

plt.title("sin(x) Maclaurin Expansion")

plt.axhline(0, color="black")
plt.axvline(0, color="black")

plt.xlabel("x")
plt.ylabel("y")

plt.legend()
plt.show()