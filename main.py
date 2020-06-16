import statistics

def std_deviation():

    sarasas = [] 
    n = int(input("Enter number of elements : ")) 
  
    for i in range(n): 
        skaicius = int(input()) 
        sarasas.append(skaicius) 
      
    std_nuokrypis = statistics.stdev(sarasas)

    return std_nuokrypis

print(std_deviation())