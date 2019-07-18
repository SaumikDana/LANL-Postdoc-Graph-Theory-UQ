import numpy as np
import sys
import math

#saumik
def truncated_array(numbers):
    temp = []
    for x in numbers:
        if x != 0:
           temp.append(x)
    return temp

def create_log_bins(nBins, a_low, a_high):
    #return numbers evenly spaced on the log scale
    return np.logspace(math.log10(a_low), math.log10(a_high), nBins +1)

def bin_and_create_pdf(t_exit, nBins, flag, graph_flag):
    if graph_flag: #graph
       a_low = 41.0
       a_high = 4.456e+18
    else: #dfn
       a_low = 4.0
       a_high = 3856891173.0
    x = create_log_bins(nBins, a_low, a_high) # bin_edges is the same as x
    pdf, bin_edges = np.histogram(t_exit, bins=x, density=flag)
#    bx = bin_edges[:-1] + np.diff(bin_edges)
    bx  = (bin_edges[:-1] + bin_edges[1:])/2 # bin_edges[:-1] knocks off the last element in the array
    if flag: #pdf
       cdf = np.cumsum(pdf * np.diff(bin_edges))
    else: #number of particles
       cdf = np.cumsum(pdf)
    return bx, pdf, cdf

for realization_number in range(1,101):
    traj_file1 = '../simple_reservoir_new' + str(realization_number) + '/graph_partime.dat'
    traj_file2 = '../simple_reservoir_new' + str(realization_number) + '/traj/partime'
    
    t1 = np.loadtxt(traj_file1, usecols=0)
    t2 = np.loadtxt(traj_file2, usecols=2)
    t1 = truncated_array(t1) #saumik
    
    flag=False #flag for histogram function: True for PDF, False for actual distribution of number of particles
    nbins=25
    
    bx1, pdf1, cdf1 = bin_and_create_pdf(t1, nbins, flag, True) #graph
    bx2, pdf2, cdf2 = bin_and_create_pdf(t2, nbins, flag, False) #dfn
    
    np.savetxt('graph%s.txt' %realization_number, zip(bx1, cdf1), fmt="%10.7e %10.7e")
    np.savetxt('dfn%s.txt' %realization_number, zip(bx2, cdf2), fmt="%10.7e %10.7e")
