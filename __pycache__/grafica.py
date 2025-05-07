import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[2,4,6,8,10]

plt.plot(x,y,label="Linea", color="blue")

plt.title("Mi primer grafico-Nelson Villalta - 06/05/2025-20:04")

plt.xlabel("Eje de las x")
plt.ylabel("Eje de las y")
plt.legend()

plt.show()