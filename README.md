## Directory Structure

```
LANL-Postdoc-Graph-Theory-UQ/
│
├── README.md - The repository's readme file with an overview and instructions.
├── dfn2graph.py - Converts DFN data into a graph representation.
├── graph_flow.py - Script related to calculating or visualizing flow within a graph.
├── graph_partime.dat - Data file, possibly containing partitioning time or other graph-related metrics.
├── graph_transport.py - Script for simulating or analyzing transport phenomena in graphs.
├── plot_all.py - A script to plot various graph-related data or results.
├── plot_max_min_confidence_interval.py - For plotting maximum and minimum confidence intervals for graph metrics.
├── save_cdf.py - Script to save the Cumulative Distribution Function of a dataset or result.
├── save_pdf.py - Script to save the Probability Density Function of a dataset or result.
└── statistical_experiments.py - Contains routines for statistical experiments or analysis on graphs.
```

## Python Scripts Overview

### [dfn2graph.py](https://github.com/SaumikDana/LANL-Postdoc-Graph-Theory-UQ/blob/master/dfn2graph.py)
- **Purpose**: Creates and manipulates graphs based on Discrete Fracture Networks (DFN).
- **Key Functions**:
  - Graph creation: `create_graph`, `create_fracture_graph`, `create_intersection_graph`, `create_bipartite_graph`
  - Path finding: `k_shortest_paths`, `greedy_edge_disjoint`
  - Graph modification and utility: `add_perm`, `add_area`, `add_weight`
  - Visualization/output: `plot_graph`, `dump_json_graph`

### [graph_flow.py](https://github.com/SaumikDana/LANL-Postdoc-Graph-Theory-UQ/blob/master/graph_flow.py)
- **Purpose**: Solves flow problems on graphs.
- **Key Functions**:
  - Constructs the Laplacian matrix: `get_laplacian_sparse_mat`
  - Prepares a graph with attributes: `prepare_graph_with_attributes`
  - Solves for vertex pressures and flow attributes: `solve_flow_on_graph`
  - Orchestrates the graph flow portion of the workflow: `run_graph_flow`

### [graph_transport.py](https://github.com/SaumikDana/LANL-Postdoc-Graph-Theory-UQ/blob/master/graph_transport.py)
- **Purpose**: Simulates particle transport on graphs.
- **Key Functions**:
  - Creates a list of downstream neighbors: `create_neighbour_list`
  - Generates starting probabilities: `create_probability_list`
  - Defines a particle's attributes and tracking methods: `Particle` class
  - Runs particle tracking on the graph: `run_graph_transport`

### [plot_all.py](https://github.com/SaumikDana/LANL-Postdoc-Graph-Theory-UQ/blob/master/plot_all.py)
- **Purpose**: Plots breakthrough curves across all realizations for both DFN and graphs.
- **Key Functions**:
  - Creates log bins, bins data, creates PDFs and CDFs
  - Generates plots with log scales

### [plot_max_min_confidence_interval.py](https://github.com/SaumikDana/LANL-Postdoc-Graph-Theory-UQ/blob/master/plot_max_min_confidence_interval.py)
- **Purpose**: Plots the mean with confidence interval bands and also with maximum and minimum bands.
- **Key Functions**:
  - Parses data, calculates averages, standard deviations, maximums, and minimums
  - Generates plots with confidence intervals

### [save_cdf.py](https://github.com/SaumikDana/LANL-Postdoc-Graph-Theory-UQ/blob/master/save_cdf.py)
- **Purpose**: Calculates and saves the cumulative distribution function (CDF) values across realizations for both DFN and graph models.
- **Key Functions**:
  - Creates log bins, bins data, calculates and saves CDFs

### [save_pdf.py](https://github.com/SaumikDana/LANL-Postdoc-Graph-Theory-UQ/blob/master/save_pdf.py)
- **Purpose**: Calculates and saves the probability density function (PDF) values across realizations for both DFN and graph models.
- **Key Functions**:
  - Similar to `save_cdf.py`, but for PDFs

### [statistical_experiments.py](https://github.com/SaumikDana/LANL-Postdoc-Graph-Theory-UQ/blob/master/statistical_experiments.py)
- **Purpose**: Plots the standard error across different realizations.
- **Key Functions**:
  - Parses data, calculates averages, standard deviations, and standard errors
  - Generates plots

## Output

![montage_graph](https://github.com/SaumikDana/LANL-Postdoc-Graph-Theory-UQ/assets/9474631/d3f48642-1721-4c32-b434-29d6e3a1a962)

![montage_graph_results](https://github.com/SaumikDana/LANL-Postdoc-Graph-Theory-UQ/assets/9474631/6dc78177-872b-4512-b4be-5beae921d4dd)
