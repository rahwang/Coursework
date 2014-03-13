from subprocess import call
import time
import os

mp = "/Users/rah/rah1-cs254-win-14/hw3/message"

outputdir = "/Users/rah/rah1-cs254-win-14/hw3/"
output = "data.csv"

outf = open(output, 'w')

print "Writing benchmark output to: [%s]" % output


def RUNmp(path, fname, N, theta, mu):
    cmd = []
    cmd.append(path)
    cmd.append(str(fname))
    cmd.append(str(N))
    cmd.append(str(theta))
    cmd.append(str(mu))
    print "Benchmark: " + " ".join(cmd)+ "\t"
    call(cmd, stdout=outf)


def experiment1():
    fname = "square.data"
    N = 100
    thetas = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
    mus = [0.0, 0.1, 0.2, 0.3, 0.4]

    for t in thetas:
        for m in mus:
            RUNmp(mp, fname, N, t, m)

    print "Exp 1 done."


def experiment2():
    fname = "disk.data"
    N = 100
    thetas = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
    mus = [0.0, 0.1, 0.2, 0.3, 0.4]

    for t in thetas:
        for m in mus:
            RUNmp(mp, fname, N, t, m)

    print "Exp 2 done."


def experiment3():
    fname = "trees-bw.data"
    N = 350
    thetas = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
    mus = [0.0, 0.1, 0.2, 0.3, 0.4]

    for t in thetas:
        for m in mus:
            RUNmp(mp, fname, N, t, m)
    print "Exp 3 done."

experiment1()
experiment2()
#experiment3()
