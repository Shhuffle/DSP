#In this code KNN (K-Nearest Numbers) algorithm will be implemented from scratch using numpy.
import numpy as np 


'''
The function a 2d vector with row storing label with coordinates and col having the x and y cordinates
For example  w
L/C     0(x-axis)      1(y-axis)   
1       5                6 
0       7                9
1       8                10
'''
def distanceVector(C,U,k): #C - known coordinates, U - unkonwn data coordinates, k- number of distanes to take
    KNN = np.zeros(k)
    totaldata = len(C)
    distances = np.zeros((totaldata,2))
    distances = np.sqrt((C[:,1] - U[0])**2 + (C[:,2] - U[1])**2)
    distances = np.column_stack((C[:,0], distances))

    #Now sorting the obtained distances.
    sorted_distance = distances[distances[:,1].argsort()] #sorts on the basis of 2nd col, i.e distane values.
    K_labels = sorted_distance[0:k,0]
    
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





#inputs, U - unknown data. C = known data structured as [label ,x_coordinate,y_cordinate]
U = [2,78]
  
C = np.array([[1,0,11],
              [2,0,4],
              [1,0,4],
              [0,0,35],
              [0,0,71],
              [1,0,5]
              ])
#parameters
k = 3

total_label = int(C[:,0].max() + 1)



#KNN label prediction
k_distances = distanceVector(C,U,k)
label,equal_counter,equal_label = majorityLabelVoting(k_distances,total_label)
if (equal_counter):
    print(f"There are {equal_counter+1} equal labels",equal_label[0:equal_counter+1])
else:
    print("The predicted label is: ",label)










