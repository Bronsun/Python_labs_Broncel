'''
from multiprocessing.pool import Pool
import numpy as np
import matplotlib.pyplot as plt
import random 

def matrix(size):
    macierz = np.random.rand(size,size)
    return np.linalg.det(macierz) 



def testMultiThreading():
    p = Pool(processes=2)

    sizes = [2, 4, 6, 8, 10, 12, 14]

    result = p.map(matrix, sizes)
    p.close()
    p.join()

    plt.hist(result, bins=16)
    plt.show()



if __name__ == "__main__":
    print("XD")
'''

import multiprocessing
import matplotlib.pyplot as plt
import numpy as np

def main():
    pool = multiprocessing.Pool()
    num_figs = 20
    input = zip(np.random.randint(10,1000,num_figs), 
                range(num_figs))
    pool.map(plot, input)

def plot(args):
    num, i = args
    fig = plt.figure()
    data = np.random.randn(num).cumsum()
    plt.plot(data)
    plt.title('Plot of a %i-element brownian noise sequence' % num)
    fig.savefig('temp_fig_%02i.png' % i)

main()