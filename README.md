# Electrical Circuit Analysis

## Overview, key features

Given number of vertices, electromotive force and maximum resistance, algorithm: 

- generates random graph
- finds approximate direction of current flow (BFS)
- detects all simple cycles in undirected graph
- finds equations according to Kirchhoff laws 
- calculates current on every edge
- adds adjustments to find real direction of current flow
- generates and displays network graph 

## Example

Given 12 nodes and 15V electromotive force between nodes 0, 1:
![small graph](/images/example1.png)

50 nodes and 150V electromotive force between nodes 0, 1:

![medium graph](/images/example2.png)

More complex computations are also possible. 



## Technologies used

- Python 
- Calculations: Numpy
- Displaying graphs: Pyvis.network
- Development environment: Pycharm Professional

## Authors

- Kamil Rudny [GitHub](https://github.com/krudny)

Project was inspired by numerical methods course taught by Ph.D Wojciech Czech at CS, AGH UST. 

