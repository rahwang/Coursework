# linear perceptron
import numpy as np
import sys


def norm(a):
    return a/np.linalg.norm(a)


def train(data, labels, runs, do_print):

    out = open("linear_online_output.txt", "w")
    n = data.shape[0]
    w = np.zeros(784)
    errs = 0

    for run in range(runs):
        for i in range(n):
            x = norm(data[i])
            # get dot product
            dotp = np.dot(x, w)
            # get true value
            true = labels[i]
    
            # Make prediction
            if dotp >= 0:
                prediction = 1
            else: 
                prediction = -1
                
            # Update w
            scalar = (true - prediction)/2
            w += (scalar * x)
            errs += scalar**2
        
            # Write prediction to file
            out.write(str(prediction)+"\n")

        if do_print == 1:
            print "Run #"+str(run+1)+" "+str(errs)
            #print "Accuracy rate = "+str(100*(n-errs)/n)+"%\n"
        
        errs = 0

    return w


def main():
    batch = int(sys.argv[1])

    print "Running linear perceptron.\n"

    # import training set
    data = np.genfromtxt("train2k.databw.35")
    labels = np.genfromtxt("train2k.label.35")

    # import evaluation set
    test = np.genfromtxt("test200.databw.35")
    n = test.shape[0]

    # Open output file
    out = open("linear_batch_output.txt", "w")

    #THREE = 1
    #FIVE = -1
    
    # Run online protocol
    if batch == 0:
        w = train(data, labels, 1, 1)
    else:
        w = train(data, labels, 20, 1)

        # Now run over evaluation set
        for i in range(n):
            x = norm(test[i])
            # get dot product
            dotp = np.dot(x, w)
            # get norm of x
            x = norm(x)
    
            # Make prediction
            if dotp >= 0:
                prediction = 1
            else: 
                prediction = -1
                
            # Write prediction to file
            out.write(str(prediction)+"\n")

    # train(data, labels, 1, 1)
    print "\n...Done!"
    
if __name__ == '__main__':
    main()



    
        
