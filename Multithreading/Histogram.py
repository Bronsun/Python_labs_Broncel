
from multiprocessing.pool import Pool
import numpy as np
import matplotlib.pyplot as plt
import random 

def matrix(size):
    macierz = np.random.rand(size,size)
    x = np.linalg.det(macierz)
    return x



def testMultiThreading():
    p = Pool(processes=4)

    sizes = [2, 4, 6, 8, 10]

    result = p.map(matrix, sizes)
    p.close()
    p.join()
    
    plt.hist(result, bins=10)
    plt.show()

if __name__ == "__main__":
    
    testMultiThreading()