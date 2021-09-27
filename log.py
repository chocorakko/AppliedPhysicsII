import matplotlib.pyplot as plt
import numpy as np
import math

x = np.linspace(-5,10,num=100)
plt.plot(x,np.log(x),label="log(x)",color="firebrick")
cmap = plt.get_cmap("Blues")

y = x-1
plt.plot(x,y,label="n=1",color="lightblue")

#rangeの数字を大きくすることによって精度を上げる
#ここではグラフの変化がみたいので、差分でループを止めるのではなく、range数字を指定してループ回数を決める
for i in range(2,25):
    #y = y +(((-1)**(i+1))*((x-1)**(i)))/i
    y = y +(((-1)**(i+1))*(x-1)**i)/i
    plt.plot(x,y,label="n="+str(i),color=cmap(i*25))


plt.xlim(-5,10)
plt.ylim(-2,5)

plt.title("log(x) Taylor Expansion")

plt.axhline(0, color="black")
plt.axvline(0, color="black")

plt.xlabel("x")
plt.ylabel("y")

plt.legend()
plt.show()