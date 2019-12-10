import networkx as nx                                      
import numpy as np                  
import pandas as pd                                 
import matplotlib.pyplot as plt
import argparse
import scipy
import os, sys
import operator


if __name__ == "__main__":                                                  
    # parse command-line arguments                                          
    parser = argparse.ArgumentParser(description="Weighting the Graph")                                 
    parser.add_argument("--weighted_edges", help="Graph Data - weighted graph", required=True)

    
    args = parser.parse_args()                               
                                                      
    current_path = os.getcwd()                             
    path__ = os.path.join(current_path, args.weighted_edges)      
                
    weighted_edges = pd.read_csv(path__, sep='\t') 
    weighted_edges.columns =["node1","node2", "w"]                   
    w = list(weighted_edges["w"])  
                                
    for m in range(len(w)):            
        w[m] = 1/w[m] 
    
    node1 = weighted_edges["node1"]
    node2 = weighted_edges["node2"]
    w_ = pd.DataFrame(w)


    edges_= pd.concat([ node1 , node2 ,w_], axis=1, ignore_index = True )                                                        
    edges_.columns =["node1","node2", "w"]                                                                  
     
    all_edges = []                                            
    for i in range(len(edges_)):                   
        all_edges.append(list(edges_.iloc[i]))
   
    import networkx as nx                             

    G = nx.Graph()
    for m in range(len(all_edges)):
        G.add_weighted_edges_from([(all_edges[m][0], all_edges[m][1],all_edges[m][2])])
        
        
    path =[] 
    weight = []
    names =[]

    for i in range(10,40):
        source = all_edges[i][0]
        target = all_edges[i+1301][1]
    
        try:
            path.append(list(nx.single_source_dijkstra(G,str(source),str(target))[1]))
        except:
            print("there is no path")
            continue
        names.append([str(source),str(target)])
        weight.append( nx.single_source_dijkstra(G,str(source),str(target))[0])
        
        
    path_ = current_path +  "/figures" 
    
    if not os.path.exists(path_):
        os.makedirs(path_)
    
        
    for z in range(10):
        G2 = nx.Graph()

        for m in range(len(path[z])):
            if m == len(path[z])-1:
                break 
            G2.add_weighted_edges_from([( path[z][m] , path[z][m+1],1) ])
            #plt.subplot(121)
            fig = plt.figure() 
            nx.draw(G2, with_labels=True, font_weight='bold')
        
            plt.savefig( path_ + "/" + str(m) +"png" )
             
        
        
        
    
    
        
        
        
        
        
        
        
