import matplotlib.pyplot as plt
import numpy as np
import math

x = np.linspace(-10,10,num=100)
plt.plot(x,np.cos(x),label="cos(x)",color="firebrick")
cmap = plt.get_cmap("Blues")

y = x**0
plt.plot(x,y,label="n=0",color="lightblue")

#rangeの数字を大きくすることによって精度を上げる
#ここではグラフの変化がみたいので、差分でループを止めるのではなく、range数字を指定してループ回数を決める
for i in range(1,20):
    y = y +(((-1)**i)*(x**(2*i)))/math.factorial(2*i)
    plt.plot(x,y,label="n="+str(2*i),color=cmap(i*25))


plt.xlim(-10,10)
plt.ylim(-10,10)

plt.title("cos(x) Maclaurin Expansion")

plt.axhline(0, color="black")
plt.axvline(0, color="black")

plt.xlabel("x")
plt.ylabel("y")

plt.legend()
plt.show()