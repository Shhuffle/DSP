#In this code KNN (K-Nearest Numbers) algorithm will be implemented on the featured mfccs values computed using DCT.py
#This program will compare the unknown featured mfccs with the known values and give the nearest known label. 
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

def computeDistance(C,U,kN=4,Threshold = 30):
    total_Known_frames = len(C[:,0])
    dimesion_n_distance = np.zeros((total_Known_frames,2),dtype=object)
    C_features = C[:, 1:].astype(float)  
    for i in range (total_Known_frames):
        partial_distance = 0
        for k in range(len(U)):
                  
            partial_distance += (C_features[i,k] - U[k]) ** 2 
        dimesion_n_distance[i,:] = [C[i,0],np.sqrt(partial_distance)]
    sorted_n_dimention_distance = dimesion_n_distance[dimesion_n_distance[:,1].argsort()]
    if sorted_n_dimention_distance[0,1] > Threshold:
        return "UNKNOWN"
    K_labels = sorted_n_dimention_distance[0:kN,0] #will return k shortest labels between the unknown and known labels
    K_labels = [str(label) for label in K_labels] #This will explicitly convert the elements to Python native string type form object
    #attribute which will make printing clean.
    return K_labels




#Now implementing majority voting on the k labels, to be used when multiple featured mfccs exists for same letter.
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
U = DCT.feature_vector #get the feature vector of my_recording.wav form the dct.py 
print(U)
'''
0 - A
1 - B
2 - E
3 - I
4 - O
5 - U

'''
C = np.array([
                ['a',110.52727724, -114.35473222, 20.37394894, 32.19629276, 5.0533949, 65.73177524, 1.13324768, -21.32912454, 6.36501137, -3.72874006, 5.91032346, 5.39705026, 6.01898879],
                ['b',78.73033833, -112.09893752, 31.8571981, 49.24017728, -3.44412544, 49.92068925, 4.20284084, -23.57793725, 8.87359253, 9.34343453, 7.42310555, 5.32938923, 1.98941612],
                ['e',60.30561104, -104.76710488, 21.8700172, 43.82628849, 1.23589619, 35.76642306, -6.3433096, -10.43049232, 19.46854428, 7.78004877, 2.27614107, -3.35421437, 2.99585966],
                ['i',128.66864724, -97.85098657, 14.86990785, 10.35837987, -18.93308472, 38.76781705, -14.18255467, -13.28664078, 14.40136285, -9.7082583, -2.19200674, 0.65061844, 6.1445766],
                ['o',113.52880575, -49.47377354, 63.44192718, 28.16339865, -10.79038955, 33.87289352, -36.72913229, -26.10591055, 17.66863745, -6.10231173, -3.6140773, 6.48185176, 17.91188184],
                ['u',100.62456049, -64.49713876, 33.64326447, 18.52672853, -24.46638633, 40.01955746, 4.50950458, -16.51784523, 1.50821074, -8.5341442, 7.59758049, 13.79179869, 3.05324052],
                ['kukur',89.51741758, -51.77533918, 42.95886541, 12.28330478, -27.42368507, 36.72793219, -4.11181619, -15.64226847, 9.55486595, -3.78837517, 7.5484735, 12.45134504, 3.84213374]


              ])
#parameters
k = 1

total_label = 6
dis = computeDistance(C,U,k)
print(dis)










