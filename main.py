import statistics
import numpy as np

def std_deviation(sarasas):

    std_nuokrypis = statistics.stdev(sarasas)

    return std_nuokrypis

def mean(sarasas):

    vidurkis = np.mean(sarasas)

    return vidurkis

def list_sum(sarasas):

    suma = sum(sarasas)

    return suma


sarasas = [] 
n = int(input("Enter number of elements : ")) 
  
for i in range(n): 
    skaicius = int(input()) 
    sarasas.append(skaicius) 

print("Std deviation:", std_deviation(sarasas))
print("Mean:", mean(sarasas))
print("Sum:", sum(sarasas))