

# A Supervised Learning Approach For Predicting Signaling Pathways in Protein Protein Interaction Networks

## This project is to weight a protein protein interaction network and to identify and predict new signaling pathways  


# Abstract
In molecular biology, cellular mechanisms are produced by group of interacting proteins. Huge amount
of these groups are still not discovered. In this study, we present a novel learning-based framework for
the problem of identifying and predicting new signaling pathways in human protein-protein interaction
networks. Our approach consists two phases, in rst phase, we weight the edges between the interacting
proteins according to existing biological knowledge and previously discovered pathways. In the second
phase, we searched the PPI graph for signaling pathways that have the minimum weights. Using this
strategy, we discovered pathways that are identied with similar biological processes and functions. Fur-
ther, we used it for reconstructing known signaling pathways. We concluded that this weighting approach
is ecient and can be used for reconstructing unknown signaling pathways and identifying functionally
enriched paths, and assign putative roles to uncharacterised proteins.




Four new files: 

[[1]] Pre-processing 1:  Clean, pre-process origional data            
      Inputs: PPI file, dowloaded from IntAct website 
      Outputs: Clean graph data (edges)  interacting_gene_pairs.txt
      
     (This is a jupyter notebook file called: 'pre_processing_1.ipynb')


## Implementing the method ##

[[2]] Phase I:  Main Code, updating the weights of the edges of the origional graph
      The output of this phase are two gz files (called test.edgelist1.gz)
      those files should be converted to csvfiles
      (need to be processed before going to phase II)  
      
      Inputs:  
             1) the origional PPI graph  "interacting_gene_pairs.txt"
             2) the gene sete (pathways, training data), msigdb.v6.2.symbols.txt         
      Outputs:  two gz files (test.edgelist1.gz , and test.edgelist2.gz)    

      Command line: 
      python phase_1.py --data_set interacting_gene_pairs.txt --pathways_sets msigdb.v6.2.symbols.txt 


[[3]]  Pre-processing 2: 
       
       Inputs: "edges.csv" and "edges_2.csv"   (two csv files from phase 1)
       outputs: weighted_edges.txt   
       Command line: 
           python  pre_processing_2.py --edges_1 edges.csv --edges_2 edges_2.csv 



[[4]] Phase II: Search for new signaling pathways
     
     - Inputs:  weighted_edges.txt 
     - Outputs: Figures of pathways
     - Command line:
       python phase_2.py --weighted_edges weighted_edges.txt   

