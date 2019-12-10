import networkx as nx
import numpy as np                  
import pandas as pd                                 
import argparse
import scipy
import os
import operator

def pairs_(pathway):                                
    all_pairs = []                                    
    for i in range(len(pathway)):                            
        if i == len(pathway)-1:                                   
            break                                             
        ps = []                                                              
        ps.append(pathway[i])                                                   
        ps.append(pathway[i+1])                                  
        all_pairs.append(ps)             
    return all_pairs                    

# Read the origional graph



if __name__ == "__main__":                                                  
    # parse command-line arguments                                          
    parser = argparse.ArgumentParser(description="Weighting the Graph")                                 
    parser.add_argument("--data_set", help="Graph Data - should be txt file only contains edges either directed or un directed", required=True)
    parser.add_argument("--pathways_sets", help="lists of pathways  - for training phase", required=True)
    
    args = parser.parse_args()                  

    current_path = os.getcwd()                         
    path = os.path.join(current_path, args.data_set)      
    
    
    int_genes_ = pd.read_csv(path, header=None, sep='\t')   # with or without sep='\t'
    int_genes_.columns = ["Gene_1","Gene_2"] 
    
    all_edges = []                                         
    for i in range(len(int_genes_)):                
        all_edges.append(list(int_genes_.iloc[i]))        

    #G = nx.Graph()                      
    #G.add_edges_from(all_edges)

    ## visulaize 

    G = nx.Graph()  
    for m in range(len(all_edges)):
        G.add_weighted_edges_from([(all_edges[m][0], all_edges[m][1],1)])

    for n, nbrs in G.adj.items():
        for nbr, eattr in nbrs.items():
            wt = eattr['weight']            
            if wt < 0.5: print(n, nbr, wt)
            
    print(" Number_of_nodes_origional_graph =" , len(G.nodes()) )
    print(" Number_of_edges_origional_graph = =" , len(G.edges()) ) 
    
    #===================================================================
    # Read the signaling pathways (gene) sets - for training purposes
    
    path2 = os.path.join(current_path, args.pathways_sets)      
    
    
    with open(path2) as f:         
        gene_sets = []                                                                                      
        for line in f:                                                   
            line = line.split()            
            gene_sets.append(line)                                         
    print("number of pathways:", len(gene_sets))  
   #===================================================================

    #Phase I:  Main Code, updating the weights of the edges of the origional graph
    # the output of this phase are two gz files (need to be processed before ) 

    t = np.ones(len(all_edges))                         
    all_edges_dp = pd.DataFrame(all_edges)                  
    all_edges_dp["wgeith"] = np.ones(len(all_edges)) 

    for m in range(0,len(gene_sets)):
    #for m in range():

        if m == 3000:
            break
        
        ppp = pairs_(gene_sets[m][2:])
    
        for z in ppp:
            ss= []
            z1 =z[0]
            z2 =z[1]  
            uu1 = all_edges_dp[ all_edges_dp[0] == str(z1)]                                                               
            uu2 = all_edges_dp[ all_edges_dp[1] == str(z1)]          
            ss = pd.concat([uu2,uu1], axis=0, ignore_index=True)                                        
            if len(ss[ss[1] == str(z2)]) == 0 and len(ss[ss[0] == str(z2)]) ==0:
                continue                                                                                                               
            else:  
                print(z1,z2)
                G[str(z2)][str(z1)]['weight'] = G[str(z2)][str(z1)]['weight'] + 1           
            
           
    nx.write_edgelist(G, "test.edgelist1.gz")

    for m in range(3000,len(gene_sets)):
    #for m in range():

        if m == 6000:
            break
        
        ppp = pairs_(gene_sets[m][2:])
    
        for z in ppp:
            ss= []
            z1 =z[0]
            z2 =z[1]  
            uu1 = all_edges_dp[ all_edges_dp[0] == str(z1)]                                                               
            uu2 = all_edges_dp[ all_edges_dp[1] == str(z1)]          
            ss = pd.concat([uu2,uu1], axis=0, ignore_index=True)                                        
            if len(ss[ss[1] == str(z2)]) == 0 and len(ss[ss[0] == str(z2)]) ==0:
                continue                                                                                                               
            else:  
                print(z1,z2)
                G[str(z2)][str(z1)]['weight'] = G[str(z2)][str(z1)]['weight'] + 1           
            
           
    nx.write_edgelist(G, "test.edgelist2.gz")
    
        
    
    
    
    
    
