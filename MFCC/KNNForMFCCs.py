#In this code KNN (K-Nearest Numbers) algorithm will be implemented from scratch using numpy.
import numpy as np 
import DCT

'''
The function has argument which is a 2d vector with row storing feature vector 
with 13 MFCCs in each col.
For example  
L/C     0   1   2   3   4       ......        13   
A/0    99 -105  15  28 0.81     ......      1.61928649                     
B/1    ..                 
C/2    ..                 
'''

#since we have 13 coefficients we need to compute the distance of dimenstion 13

def computeDistance(C,U,kN=4):
    total_Known_frames = len(C[:,0])
    dimesion_n_distance = np.zeros((total_Known_frames,2))
    
    for i in range (total_Known_frames):
        partial_distance = 0
        for k in range(len(U)):
            partial_distance += (C[i,k+1] - U[k]) ** 2 
        dimesion_n_distance[i,:] = [C[i,0],np.sqrt(partial_distance)]
    print(dimesion_n_distance)
    sorted_n_dimention_distance = dimesion_n_distance[dimesion_n_distance[:,1].argsort()]
    K_labels = sorted_n_dimention_distance[0:kN,0] #will return k shortest labels between the unknown and known labels
    return K_labels




#Now implementing majority voting on the k labels
def majorityLabelVoting(k_labels,Total_Labels = 3):
    counter = np.zeros(Total_Labels)
    
    for i in range(len(k_labels)):
        counter[int(k_labels[i])] += 1

    maxindexval = 0
    equal_counter = 0
    equal_labels = np.zeros(Total_Labels)
    maxval = counter[0]
    for i in range(1,Total_Labels):
        if (counter[i] > maxval):
            maxindexval = i 
            maxval = counter[i]
           
        elif (counter[i] == maxval):
            equal_labels[equal_counter] = i
            equal_counter +=1
            
            
    return maxindexval,equal_counter,equal_labels





#inputs, U - unknown data. C = known data structured as [label ,feature_variables]
#NOTE : provide the known frame value C in ascending order i.e 0,1,2....
#U = DCT.MFCCS.mean(axis=0)
U = [0,0,0]
  
C = np.array([[1,0,11,12],
              [2,0,4,13],
              [1,0,4,14],
              [8,0,35,15],
              [0,0,71,16],
              [1,0,5,17]
              ])
#parameters
k = 4
total_label = int(C[:,0].max() + 1)


dis = computeDistance(C,U,k)
print(dis)










