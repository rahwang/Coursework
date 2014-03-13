import csv
import sys
from pylab import *
from numpy import *
from scipy import *
from scipy import optimize
import matplotlib.pyplot as plt

plt.ylabel("# Iterations")
plt.xlabel("Epsilon (log form)")

eps = [-10, -9, -8, -7, -6, -5]
ns = [10, 100, 1000, 10000]

ls = [[],[],[],[],[]]

with open("data0.csv", 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter='\t', quotechar='|')
    for row in spamreader:
        if row[0] == "10":
            ls[0].append(float(row[2]))
        if row[0] == "100":
            ls[1].append(float(row[2]))
        if row[0] == "1000":
            ls[2].append(float(row[2]))
        if row[0] == "10000":
            ls[3].append(float(row[2]))

print eps
print ls[0]
print ls[1]
print ls[2]
print ls[3]


# Create plots with pre-defined labels.
# Alternatively, you can pass labels explicitly when calling `legend`.
#fig, ax = plt.subplots()

plt.plot(eps, ls[0], 'r', label='n = '+str(10))
plt.plot(eps, ls[1], 'g', label='n = '+str(100))
plt.plot(eps, ls[2], 'k', label='n = '+str(1000))
plt.plot(eps, ls[3], 'b', label='n = '+str(10000))

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

