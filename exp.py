import matplotlib.pyplot as plt
import numpy as np
import math

x = np.linspace(-10,10,num=100)
plt.plot(x,np.exp(x),label="exp(x)",color="firebrick")
cmap = plt.get_cmap("Blues")

y = x**0
plt.plot(x,y,label="n=0",color="lightblue")

#rangeの数字を大きくすることによって精度を上げる
#ここではグラフの変化がみたいので、差分でループを止めるのではなく、range数字を指定してループ回数を決める
for i in range(1,30):
    y = y +(x**i)/math.factorial(i)
    plt.plot(x,y,label="n="+str(i),color=cmap(i*25))

plt.xlim(-10,10)
plt.ylim(-1,3)

plt.title("exp(x) Maclaurin Expansion")

plt.axhline(0, color="black")
plt.axvline(0, color="black")

plt.xlabel("x")
plt.ylabel("y")

plt.legend()
plt.show()