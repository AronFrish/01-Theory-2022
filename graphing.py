import matplotlib.pyplot as plt

#adding data
x = []
y = []
f = open("data_dump.txt", "r")
for line in f.readlines() :
    line = line[:-1]
    num = int(line[:line.index(":") - 1])
    x.append(num)
    zeroes = int(line[line.index(":") + 2:line.index(",")])
    ones = int(line[line.index(",") + 2:])
    y.append(round(ones/zeroes, 5))
#adding data

#graphing data
plt.plot(x, y)
plt.xlabel('Number')
plt.ylabel('Ratio of 1s to 0s')
plt.title('Ratio of 1s to 0s as Numbers Increase')
plt.show()
#graphing data