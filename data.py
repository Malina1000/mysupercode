import matplotlib.pyplot as plt

#       numberd   voltage (mV)
data = [[255,     3253],
        [127,     1683],
        [64,      876],
        [32,      460],
        [5,       120.3],
        [0,       56.1]]

x = [   0,     5,  32,  64,  127,  255]
y = [56.1, 120.3, 460, 876, 1683, 3253]

plt.scatter(x, y)
plt.xlabel('number')
plt.ylabel('voltage, mV')
plt.grid('--')
plt.show()