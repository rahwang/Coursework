from subprocess import call
import time
import os

#eigP = "/Users/rah/rah1-cs254-win-14/hw5/eigP"
eigP = "/home/rah1/rah1-cs254-win-14/hw5/eigP"

outputdir = "/home/rah1/rah1-cs254-win-14/hw5/"
#outputdir = "/Users/rah/rah1-cs254-win-14/hw5/"
output = "data1.csv"

outf = open(output, 'w')

print "Writing benchmark output to: [%s]" % output


def RUNeigP(path, k, epsilon, fname, n):
    cmd = []
    cmd.append(path)
    cmd.append(str(k))
    cmd.append(str(epsilon))
    cmd.append(str(fname))
    cmd.append(str(n))
    cmd.append(str(2))
    print "Benchmark: " + " ".join(cmd)+ "\t"
    call(cmd, stdout=outf)


def experiment1():
    fname = "test10.mat"
    eps = [10, 9, 8, 7, 6, 5]
    ns = [10, 100, 1000, 10000]

    for e in eps:
        for n in ns:
            RUNeigP(eigP, 1, e, fname, n)

    print "Exp 1 done."

experiment1()
#experiment2()
#experiment3()
