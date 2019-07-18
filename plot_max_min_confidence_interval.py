#code to plot mean with confidence interval band 
#code to plot mean with max and min band
import numpy as np
import matplotlib.pyplot as plt
import sys
from matplotlib import rc
from scipy import stats

#font
rc('font',**{'family':'serif','serif':['Times']})
rc('text', usetex=True)

def line_tuple(filename):
    return np.loadtxt(filename,unpack=True)

#parse each line from the datafile into a tuple of the form (xvals,yvals); store that tuple in a list.

number_realizations = int(sys.argv[1])
graph_file_list = ['graph%s.txt' %s for s in range(1,number_realizations+1)]
dfn_file_list = ['dfn%s.txt' %s for s in range(1,number_realizations+1)]

#DFN ------------------------------------------------
data = [line_tuple(fname) for fname in dfn_file_list] #first index of data is realization number-1; second index is 0 for times and 1 for pdf values

#np.shape(data) is (#number of realizations, 2, number of time bins)
#np.shape(data_reorganized) is (#number of realizations, number of time bins)
data_reorganized = [np.interp(data[0][0],d[0],d[1]) for d in data]
 
#Now do the averaging and standard deviation
averages = [np.average(x) for x in zip(*data_reorganized)]
stds = [np.std(x) for x in zip(*data_reorganized)]
maxes = [np.amax(x) for x in zip(*data_reorganized)]
mins = [np.amin(x) for x in zip(*data_reorganized)]

#put the average value and standard deviation along with it's x point into a file.
with open('avg_stdfile_dfn.txt','w') as fout:
    for x,avg,std,maximum,minimum in zip(data[0][0],averages,stds,maxes,mins):
        fout.write('{0} {1} {2} {3} {4}\n'.format(x,avg,std,maximum,minimum))

#Graph ----------------------------------------------
data = [line_tuple(fname) for fname in graph_file_list]

#np.shape(data) is (#number of realizations, 2, number of time bins)
#np.shape(data_reorganized) is (#number of realizations, number of time bins)
data_reorganized = [np.interp(data[0][0],d[0],d[1]) for d in data]
 
#Now do the averaging.
averages = [np.average(x) for x in zip(*data_reorganized)]
stds = [np.std(x) for x in zip(*data_reorganized)]
maxes = [np.amax(x) for x in zip(*data_reorganized)]
mins = [np.amin(x) for x in zip(*data_reorganized)]

#put the average value and standard deviation along with it's x point into a file.
with open('avg_stdfile_graph.txt','w') as fout:
    for x,avg,std,maximum,minimum in zip(data[0][0],averages,stds,maxes,mins):
        fout.write('{0} {1} {2} {3} {4}\n'.format(x,avg,std,maximum,minimum))

#DFN ------------------------------------------------
X_dfn, Y_dfn = [], []
Y_lower_dfn, Y_upper_dfn = [], []
Y_dfn_min, Y_dfn_max = [], []
t_scale = 365.0*24.0*3600.0
for line in open('avg_stdfile_dfn.txt', 'r'):
  values = [float(s) for s in line.split()]
  X_dfn.append(values[0]/t_scale)
  Y_dfn.append(values[1])
  Y_dfn_max.append(values[3])
  Y_dfn_min.append(values[4])
  #95 percent confidence interval
  Y_lower_dfn.append(values[1]-1.96*values[2])
  Y_upper_dfn.append(values[1]+1.96*values[2])

#Graph ----------------------------------------------
X_graph, Y_graph = [], []
Y_lower_graph, Y_upper_graph = [], []
Y_graph_min, Y_graph_max = [], []
for line in open('avg_stdfile_graph.txt', 'r'):
  values = [float(s) for s in line.split()]
  X_graph.append(values[0]/t_scale)
  Y_graph.append(values[1])
  Y_graph_max.append(values[3])
  Y_graph_min.append(values[4])
  #95 percent confidence interval
  Y_lower_graph.append(values[1]-1.96*values[2])
  Y_upper_graph.append(values[1]+1.96*values[2])

# ---------------------------------------------------
plt.plot(X_dfn, Y_dfn, 'r-', label="DFN")
plt.plot(X_graph, Y_graph, 'b-', label="Graph")
plt.gca().legend(frameon=False, loc="best")

# dfn
#plt.plot(X_dfn, Y_lower_dfn, 'r--', linewidth=1)
#plt.plot(X_dfn, Y_upper_dfn, 'r--', linewidth=1)
#plt.fill_between(X_dfn, Y_dfn, Y_upper_dfn, color='lightcoral', alpha=0.5)
#plt.fill_between(X_dfn, Y_dfn, Y_lower_dfn, color='lightcoral', alpha=0.5)

plt.plot(X_dfn, Y_dfn_min, 'r--', linewidth=1)
plt.plot(X_dfn, Y_dfn_max, 'r--', linewidth=1)
plt.fill_between(X_dfn, Y_dfn, Y_dfn_min, color='lightcoral', alpha=0.5)
plt.fill_between(X_dfn, Y_dfn, Y_dfn_max, color='lightcoral', alpha=0.5)

# graph
#plt.plot(X_graph, Y_lower_graph, 'b--', linewidth=1)
#plt.plot(X_graph, Y_upper_graph, 'b--', linewidth=1)
#plt.fill_between(X_graph, Y_graph, Y_lower_graph, color='lightblue', alpha=0.5)
#plt.fill_between(X_graph, Y_graph, Y_upper_graph, color='lightblue', alpha=0.5)

plt.plot(X_graph, Y_graph_min, 'b--', linewidth=1)
plt.plot(X_graph, Y_graph_max, 'b--', linewidth=1)
plt.fill_between(X_graph, Y_graph, Y_graph_min, color='lightblue', alpha=0.5)
plt.fill_between(X_graph, Y_graph, Y_graph_max, color='lightblue', alpha=0.5)

plt.gca().set_xscale('log')
plt.gca().set_yscale('log')
plt.gca().set_title("Mean over %s realizations" %number_realizations, fontsize=14)
plt.gca().set_ylabel("Cumulative normalized production", fontsize=14)
plt.gca().set_xlabel("Exit time (Yr)", fontsize=14)
plt.tight_layout()
plt.savefig('mean_over_%s_realizations.pdf' %number_realizations, bbox_inches="tight", transparent=True)
plt.show()
