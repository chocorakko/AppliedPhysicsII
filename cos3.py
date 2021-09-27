
import matplotlib.pyplot as plt
import numpy as np
import math

x = np.linspace(-10,10,num=100)
plt.plot(x,np.cos(x),label="cos(x)",color="firebrick")

y = x**0 #メモ：1にしてしまうと、xとyの次元が合わなくなる
plt.plot(x,y,label="n=1",color="lightblue")

y = y - x**2 / 2
plt.plot(x,y,label="n=2",color="skyblue")

y = y + x**4 / math.factorial(4)
plt.plot(x,y,label="n=4",color="deepskyblue")

y = y - x**6 / math.factorial(6)
plt.plot(x,y,label="n=6",color="cornflowerblue")

y = y + x**8 / math.factorial(8)
plt.plot(x,y,label="n=8",color="royalblue")

y = y - x**10 / math.factorial(10)
plt.plot(x,y,label="n=10",color="midnightblue")

plt.xlim(-10,10)
plt.ylim(-10,10)

plt.title("cos(x) Maclaurin Expansion")

plt.axhline(0, color="black")
plt.axvline(0, color="black")

plt.xlabel("x")
plt.ylabel("y")

plt.legend()
plt.show()