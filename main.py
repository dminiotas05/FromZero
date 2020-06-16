import statistics
import numpy as np

def std_deviation(sarasas):

    std_nuokrypis = statistics.stdev(sarasas)

    return std_nuokrypis

def list_sum(sarasas):

    vidurkis = np.mean(sarasas)

    return vidurkis

sarasas = [] 
n = int(input("Enter number of elements : ")) 
  
for i in range(n): 
    skaicius = int(input()) 
    sarasas.append(skaicius) 

print(std_deviation(sarasas))
print(list_sum(sarasas))