from PIL import Image
import numpy as np
import random
import scipy


def nearest(cell, centroids):
    best = 100000000
    idx = 0
    for i,c in enumerate(centroids):
        d = np.linalg.norm(cell - c)
        if d < best:
            best = d
            idx = i
    return idx


def main():
    fname = "mandrill-small.tiff"
    k = 16
    iterations = 30
    
    # Read the image in a three-dimensional numpy array
    image = Image.open(fname)
    pix = np.asarray(image, dtype=np.int)
    n = pix.shape[0]
    
    # Array storing centroids, initialize with random cells
    centroids = np.zeros((k, 3))
    for s in range(k):
        centroids[s] = pix[random.randint(0, n)][random.randint(0, n)]
    
    # Iterate!
    for t in range(iterations):
        # scratch arrays for recomputing centroids
        scratch = np.zeros((k, 3)) # store sums
        counters = np.zeros((k)) # store number of points in cluster

        # Assign clusters, then recompute centroids
        for i in range(n):
            for j in range(n):
                idx = nearest(pix[i][j], centroids)
                scratch[idx] += pix[i][j]
                counters[idx] += 1
        for i in range(k):
            if counters[i] != 0:
                centroids[i] = scratch[i]/counters[i]

    # Run over large image
    image = Image.open("mandrill-large.tiff")
    big = np.asarray(image, dtype=np.int)
    # Create new pixel map
    res = np.zeros((512, 512, 3), dtype=np.uint8)
    for i in range(512):
        for j in range(512):
            idx = nearest(big[i][j], centroids)
            res[i][j] = centroids[idx]
            
    # To save the image corresponding to matrix A
    out_im = Image.fromarray(res, "RGB")
    out_im.save("output-mandrill.tiff")

if __name__ == "__main__":
    main()
