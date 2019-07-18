#code to plot breakthrough curves across all realizations for both dfn and graph
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import sys
import math

rc('font',**{'family':'sans-serif','sans-serif':['Times']})
rc('text', usetex=True)

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
    # take the a_low to a_high range and divide it into nBins slots
    x = create_log_bins(nBins, a_low, a_high)
    # bin_edges is the same as x
    pdf, bin_edges = np.histogram(t_exit, bins=x, density=flag)

    if flag: #pdf
       pdf_temp = []
       bx = []
       bx_temp1 = bin_edges[:-1]
       for j in range(0,np.size(pdf)):
           pdf_temp.append(pdf[j] * (bin_edges[j+1]-bin_edges[j]))
           bx.append(bx_temp1[j] + bin_edges[j+1]-bin_edges[j])
       cdf = np.cumsum(pdf_temp)
    else: #number of particles
       bx = bin_edges[:-1] + np.diff(bin_edges)
       cdf = np.cumsum(pdf)
    return bx, pdf, cdf

fig, ax = plt.subplots(nrows=1, ncols=2, squeeze=True)    
plt.subplots_adjust(wspace=0.25)
nbins = int(sys.argv[1])

for i in range(1,101):
    traj_file1 = '../simple_reservoir_new' + str(i) +  '/graph_partime.dat'
    traj_file2 = '../simple_reservoir_new' + str(i) + '/traj/partime'
    t1 = np.loadtxt(traj_file1, usecols=0)
    t2 = np.loadtxt(traj_file2, usecols=2)
    
    t1 = truncated_array(t1) #saumik
    
    flag=True #flag for histogram function: True for PDF
    
    bx1, pdf1, cdf1 = bin_and_create_pdf(t1, nbins, flag, True) #graph
    bx2, pdf2, cdf2 = bin_and_create_pdf(t2, nbins, flag, False) #dfn

    np.savetxt('graph%s.txt' %i, zip(bx1, pdf1), fmt="%10.7e %10.7e")
    np.savetxt('dfn%s.txt' %i, zip(bx2, pdf2), fmt="%10.7e %10.7e")
   
    if flag:
       markergraph="-k"
       markerdfn="-r"
       label="Production rate"
       labelcum="Cumulative production rate"
    else:
       markergraph="-ko"
       markerdfn="-ro"
       label="Number of exiting particles"
       labelcum="Cumulative number of exiting particles"
    
    if i == 1:
    	ax[0].plot(bx1, pdf1, markergraph, markersize=4, label="Graph")
    	ax[1].plot(bx1, cdf1, markergraph, markersize=4, label="Graph") 
    
    	ax[0].plot(bx2, pdf2, markerdfn, markersize=4, label="DFN")
    	ax[1].plot(bx2, cdf2, markerdfn, markersize=4, label="DFN")
    else:
    	ax[0].plot(bx1, pdf1, markergraph, markersize=4)
    	ax[1].plot(bx1, cdf1, markergraph, markersize=4)
    
    	ax[0].plot(bx2, pdf2, markerdfn, markersize=4)
    	ax[1].plot(bx2, cdf2, markerdfn, markersize=4)

ax[0].set_xscale('log') #saumik
ax[0].set_yscale('log') #saumik

ax[1].set_xscale('log') #saumik
ax[1].set_yscale('log') #saumik

ax[0].legend(frameon=False, loc="best")
ax[1].legend(frameon=False, loc="best")
ax[0].set_ylabel(label, fontsize=14)
ax[1].set_ylabel(labelcum, fontsize=14)
ax[0].set_xlabel("Exit time (s)", fontsize=14)
ax[1].set_xlabel("Exit time (s)", fontsize=14)

plt.tight_layout()
fig.savefig('combined_btc.pdf', bbox_inches="tight", transparent=True)
plt.show()
