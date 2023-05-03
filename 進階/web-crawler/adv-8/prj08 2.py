import matplotlib.pyplot as plt

listX = [1, 2, 3, 4, 5, 6]
listY = [20, 30, 37, 21, 33, 40]

fig, ax = plt.subplots()
ax.plot(listX, listY)
ax.set_xlabel('X label')
ax.set_ylabel('Y label')
ax.set_title('My title')

plt.show()