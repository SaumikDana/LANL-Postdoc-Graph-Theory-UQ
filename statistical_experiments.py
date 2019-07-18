#code to plot standard error
import numpy as np
import matplotlib.pyplot as plt
import sys
from matplotlib import rc
from scipy import stats

#font
rc('font',**{'family':'serif','serif':['New Century Schoolbook']})
rc('text', usetex=True)

def line_tuple(filename):
    return np.loadtxt(filename,unpack=True)

#parse each line from the datafile into a tuple of the form (xvals,yvals); store that tuple in a list.

number_realizations = int(sys.argv[1])
time_bin_number = int(sys.argv[2])
stderror_graph = np.empty((number_realizations,25))
means_graph = np.empty((number_realizations,25))
count = np.arange(1,number_realizations+1)
stderror_dfn = np.empty((number_realizations,25))
means_dfn = np.empty((number_realizations,25))

for i in range(1,number_realizations+1):
    graph_file_list = ['graph%s.txt' %s for s in range(1,i+1)]
    dfn_file_list = ['dfn%s.txt' %s for s in range(1,i+1)]

    #DFN ------------------------------------------------
    data = [line_tuple(fname) for fname in dfn_file_list] #first index of data is realization number-1; second index is 0 for times and 1 for pdf values
    
    #np.shape(data) is (#number of realizations, 2, number of time bins)
    #np.shape(data_reorganized) is (#number of realizations, number of time bins)
    data_reorganized = [np.interp(data[0][0],d[0],d[1]) for d in data]
    
    #Now do the averaging and standard deviation
    averages = [np.average(x) for x in zip(*data_reorganized)]
    stds = [np.std(x) for x in zip(*data_reorganized)]
#    maxes = [np.amax(x) for x in zip(*data_reorganized)]
#    mins = [np.amin(x) for x in zip(*data_reorganized)]

    for j in range(0,25):
        stderror_dfn[i-1,j] = (stds/np.sqrt(i))[j]
        means_dfn[i-1,j] = averages[j]
   
    #Graph ----------------------------------------------
    data = [line_tuple(fname) for fname in graph_file_list]
    
    data_reorganized = [np.interp(data[0][0],d[0],d[1]) for d in data]
    
    averages = [np.average(x) for x in zip(*data_reorganized)]
    stds = [np.std(x) for x in zip(*data_reorganized)]
#    maxes = [np.amax(x) for x in zip(*data_reorganized)]
#    mins = [np.amin(x) for x in zip(*data_reorganized)]

    for j in range(0,25):
        stderror_graph[i-1,j] = (stds/np.sqrt(i))[j]
        means_graph[i-1,j] = averages[j]
 
# Plot ---------------------------------------------
flag = False
if flag: #dfn
   plt.plot(count,stderror_dfn[:,time_bin_number-1], label = 'Standard Error')
   plt.gca().set_title("For time bin \# %s in DFN" %(time_bin_number), fontsize=14)
   plt.gca().set_xlabel("Number of realizations", fontsize=14)
   #plt.gca().set_yscale('log')
   plt.yticks(fontsize=14)
   plt.gca().legend(frameon=False, loc="best")
   plt.grid()
   plt.tight_layout()
   plt.show()
else:
   plt.plot(count,stderror_graph[:,time_bin_number-1], label = 'Standard Error')
   plt.gca().set_title("For time bin \# %s in Graph" %(time_bin_number), fontsize=14)
   plt.gca().set_xlabel("Number of realizations", fontsize=14)
   #plt.gca().set_yscale('log')
   plt.yticks(fontsize=14)
   plt.gca().legend(frameon=False, loc="best")
   plt.grid()
   plt.tight_layout()
   plt.show()

