import csv
import sys
from pylab import *
from numpy import *
from scipy import *
from scipy import optimize
import matplotlib.pyplot as plt

plt.ylabel("Gamma (log2)")
plt.xlabel("Accuracy (by cross validation)")

c = range(-5, 15, 2)
g = [15, 13, 11, 9, 7, 5, 3, 1, -1, -3]

ls = [[],[],[],[],[],[],[],[],[],[]]

with open("1000cv.data", 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        if row[0] == "-5":
            print row[0]
            print float(row[2])
            ls[0].append(float(row[2]))
        if row[0] == "-3":
            ls[1].append(float(row[2]))
        if row[0] == "-1":
            ls[2].append(float(row[2]))
        if row[0] == "1":
            ls[3].append(float(row[2]))
        if row[0] == "3":
            ls[4].append(float(row[2]))
        if row[0] == "5":
            ls[5].append(float(row[2]))
        if row[0] == "7":
            ls[6].append(float(row[2]))
        if row[0] == "9":
            ls[7].append(float(row[2]))
        if row[0] == "11":
            ls[8].append(float(row[2]))
        if row[0] == "13":
            ls[9].append(float(row[2]))

print ls[0]
print g

# Create plots with pre-defined labels.
# Alternatively, you can pass labels explicitly when calling `legend`.
#fig, ax = plt.subplots()

plt.plot(g, ls[0], 'r', label='log2(c) = '+str(-5))
plt.plot(g, ls[1], 'g', label='log2(c) = '+str(-3))
plt.plot(g, ls[2], 'k', label='log2(c) = '+str(-1))
plt.plot(g, ls[3], 'b', label='log2(c) = '+str(1))
plt.plot(g, ls[4], 'b', label='log2(c) = '+str(3))
plt.plot(g, ls[5], 'b', label='log2(c) = '+str(5))
plt.plot(g, ls[6], 'b', label='log2(c) = '+str(7))
plt.plot(g, ls[7], 'b', label='log2(c) = '+str(9))
plt.plot(g, ls[8], 'b', label='log2(c) = '+str(11))
plt.plot(g, ls[9], 'b', label='log2(c) = '+str(13))

#for l, c, mu in zip(ls, cs, mus):
#    plt.plot(ts, l, c, label='mu = '+str(mu))

# Now add the legend with some customizations.
legend = plt.legend(loc='best', shadow=True)

# The frame is matplotlib.patches.Rectangle instance surrounding the legend.
frame  = legend.get_frame()
frame.set_facecolor('0.90')

#plt.xscale('log', basey=2)
#plt.yscale('log')

# Set the fontsize
for label in legend.get_texts():
    label.set_fontsize('small')

for label in legend.get_lines():
    label.set_linewidth(1.5)  # the legend line width

#plt.title("Linear Online Errors")
plt.title("Iterations v Epsilon value for eigP.c")

plt.show()

savefig("p2.png")

