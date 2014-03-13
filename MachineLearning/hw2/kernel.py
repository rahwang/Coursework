# linear perceptron
import numpy as np
import math
import sys


def norm(a):
    return a/np.linalg.norm(a)


def k(a, b, sigma):
    x = -1*(np.linalg.norm(a-b)**2)/(2.*sigma**2)
    return math.exp(x)


def pred(data, n, cs, vec, sigma):
    sum = 0
    for i in range(n):
        x = data[i]
        val = k(x, vec, sigma)
        #val = np.dot(x, vec)
        sum += cs[i]*val

    if sum >= 0:
        return 1
    return -1


def precomputed_pred(precomp, n, cs, t):
    sum = 0
    for i in range(n):
        val = precomp[i % n][t % n]
        #val = np.dot(x, vec)
        sum += cs[i]*val

    if sum >= 0:
        return 1
    return -1


def precompute(data, n, sigma):
    new = np.empty([n, n])
    for i in range(n):
        for j in range(i, n):
            v = k(data[i], data[j], sigma)
            new[i][j] = new[j][i] = v
    return new
    

def train(data, labels, runs, sigma):
    out = open("kernel_online_output.txt", "w")

    n = data.shape[0]

    # create c array
    cs = np.zeros(n)
    errs = 0

    # normalize
    for vec in data:
        vec = norm(vec)

    # Precompute matrix
    precomp = precompute(data, n, sigma)
    
    for j in range(runs):
        for i in range(n):
            # make prediction
            #prediction = pred(data, cs, data[i], n, sigma)
            prediction = precomputed_pred(precomp, n, cs, i)
            
            # get true value 
            true = labels[i]
        
            # Update cs
            scalar = (true - prediction)/2
            cs[i] += scalar
            errs += scalar**2

        print "Run #"+str(j+1)+" errors = "+str(errs)
        print "Accuracy rate = "+str(100*(n-errs)/n)+"%\n"
        errs = 0

    return cs


def cross_validate(data, labels, sigma):
    d1 = data[:1600]
    d2 = data[1600:]
    l1 = labels[:1600]
    l2 = labels[1600:]

    cs80 = train(d1, l1, 3, sigma)
    cs20 = train(d2, l2, 3, sigma)

    errs = 0
    for i in range(400):
        x = d2[i]
        prediction = pred(d1, 1600, cs80, x, sigma)
        
        true = l2[i]
        scalar = (true - prediction)/2
        errs += scalar**2

    print "after 20%",str(errs)

    return errs


def main():
    run_type = int(sys.argv[1])
    sigma = float(sys.argv[2])

    print "Running kernel perceptron.\n"

    # import training set
    data = np.genfromtxt("train2k.databw.35")
    n = data.shape[0]
    labels = np.genfromtxt("train2k.label.35")

    # import evaluation set
    test = np.genfromtxt("test200.databw.35")
    testn = test.shape[0]

    # Open output file
    out = open("kernel_batch_output.txt", "w")

    #THREE = 1
    #FIVE = -1
    
    # Run online protocol
    if run_type == 0:
        train(data, labels, 1, sigma)

    # Run batch protocol
    elif run_type == 1:
        cs = train(data, labels, 5, sigma)
        for i in range(testn):
            x = norm(test[i])
            prediction = pred(data, n, cs, x, sigma)

            # Write prediction to file
            out.write(str(prediction)+"\n")
    else:
        print cross_validate(data, labels, sigma);

    # train(data, labels, 1, 1)
    print "\n...Done!"
    
if __name__ == '__main__':
    main()



    
        
