#===================================================================
# preprocessing - merging the weights - 

import numpy as np
import pandas as pd
import networkx as nx
import argparse
import scipy
import os
import operator

if __name__ == "__main__":                                                  
    # parse command-line arguments                                          
    parser = argparse.ArgumentParser(description="Weighting the Graph")                                 
    parser.add_argument("--edges_1", help="Graph Data - graph with updates weights of edges1", required=True)
    parser.add_argument("--edges_2", help="Graph Data - graph with updates weights of edges2", required=True)

    args = parser.parse_args()                  

    current_path = os.getcwd()                         
    path1 = os.path.join(current_path,args.edges_1)     
    path2 = os.path.join(current_path,args.edges_2)     

    #edges = np.loadtxt('/home/maburid/network_science_project/Project_/edges.csv',dtype=str)

    edges = pd.read_csv(path1)
    w = list(edges["Column4"])

    for m in range(len(list(edges["Column4"]))):
        w[m] = int(w[m][0])
  

    edges_2 = pd.read_csv(path2)
    w2 = list(edges_2["Column4"])                   

    for m in range(len(list(edges_2["Column4"]))):   
        w2[m] = int(w2[m][0])                      
    
                          
    for m in range(len(w)): 
        w[m] = w[m] + w2[m] -1 
    

    node1 = edges["Column1"]
    node2 = edges["Column2"]
    w_ = pd.DataFrame(w)

    edges_= pd.concat([ node1 , node2 ,w_], axis=1, ignore_index = True )                                 
    edges_.columns =["node1","node2", "w"]

    weighted_edges = edges_[edges_["w"] > 1 ] 
    print("Number of edges in the weighted graph:", len(weighted_edges))
    weighted_edges.to_csv("weighted_edges.txt", sep="\t", header=None,index=False)    

