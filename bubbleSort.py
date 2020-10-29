def bubble_Sort(array): 
    n = len(array) 
    for i in range(n-1):   
        for j in range(0, n-i-1): 
            if array[j] > array[j+1] : 
                array[j], array[j+1] = array[j+1], array[j] 
                
                
array = [333, 3228, 1422, 221, 4222, 993434, 966,5664,86667] 
bubble_Sort(array) 
  
print ("Sorted arrayay using bubble sort:") 
for i in range(len(array)): 
    print ("%d" %array[i]),  
