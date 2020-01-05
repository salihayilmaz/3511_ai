import sys,re
from ortools.sat.python import cp_model

model = cp_model.CpModel()

text = open("futoshiki_input.txt","r")
outputText = open("futoshiki_output.txt","w+")

input = text.readlines()

num_vals = 5
A1 = model.NewIntVar(1, num_vals - 1, 'A1')
B1 = model.NewIntVar(1, num_vals - 1, 'B1')
C1 = model.NewIntVar(1, num_vals - 1, 'C1')
D1 = model.NewIntVar(1, num_vals - 1, 'D1')

A2 = model.NewIntVar(1, num_vals - 1, 'A2')
B2 = model.NewIntVar(1, num_vals - 1, 'B2')
C2 = model.NewIntVar(1, num_vals - 1, 'C2')
D2 = model.NewIntVar(1, num_vals - 1, 'D2')

A3 = model.NewIntVar(1, num_vals - 1, 'A3')
B3 = model.NewIntVar(1, num_vals - 1, 'B3')
C3 = model.NewIntVar(1, num_vals - 1, 'C3')
D3 = model.NewIntVar(1, num_vals - 1, 'D3')

A4 = model.NewIntVar(1, num_vals - 1, 'A4')
B4 = model.NewIntVar(1, num_vals - 1, 'B4')
C4 = model.NewIntVar(1, num_vals - 1, 'C4')
D4 = model.NewIntVar(1, num_vals - 1, 'D4')

dictionary = {}

dictionary["A1"] = A1
dictionary["A2"] = A2
dictionary["A3"] = A3
dictionary["A4"] = A4

dictionary["B1"] = B1
dictionary["B2"] = B2
dictionary["B3"] = B3
dictionary["B4"] = B4

dictionary["C1"] = C1
dictionary["C2"] = C2
dictionary["C3"] = C3
dictionary["C4"] = C4

dictionary["D1"] = D1
dictionary["D2"] = D2
dictionary["D3"] = D3
dictionary["D4"] = D4

for line in input:
    list = line.split(",")
    value1 = str(list[0].replace(" ", "").replace("\n",""))
    value2 = str(list[1].replace(" ", "").replace("\n",""))
    if value2.isdigit():
        value2 = int(value2)
        dictionary[value1] = model.NewIntVar(value2, value2, value1)
        input.remove(line)        
    
for line in input:
    list = line.split(",")
    value1 = str(list[0].replace(" ", "").replace("\n",""))
    value2 = str(list[1].replace(" ", "").replace("\n",""))
    model.Add(dictionary[value1] > dictionary[value2])    

list1 = [dictionary["A1"], dictionary["A2"], dictionary["A3"], dictionary["A4"]]
list2 = [dictionary["B1"], dictionary["B2"], dictionary["B3"], dictionary["B4"]]
list3 = [dictionary["C1"], dictionary["C2"], dictionary["C3"], dictionary["C4"]]
list7 = [dictionary["D1"], dictionary["D2"], dictionary["D3"], dictionary["D4"]]
list4 = [dictionary["A1"], dictionary["B1"], dictionary["C1"], dictionary["D1"]]
list5 = [dictionary["A2"], dictionary["B2"], dictionary["C2"], dictionary["D2"]]
list6 = [dictionary["A3"], dictionary["B3"], dictionary["C3"], dictionary["D3"]]
list8 = [dictionary["A4"], dictionary["B4"], dictionary["C4"], dictionary["D4"]]

allLists = [list1, list2, list3, list4, list5, list6, list7, list8]

for list in allLists:
    model.AddAllDifferent(list)

solver = cp_model.CpSolver()
status = solver.Solve(model)

if status == cp_model.FEASIBLE:
        outputText.writelines( str(solver.Value(dictionary["A1"])) + "," + 
         str(solver.Value(dictionary["A2"])) + "," + 
          str(solver.Value(dictionary["A3"])) + "," +  
           str(solver.Value(dictionary["A4"])) + "\n")
        
        outputText.writelines( str(solver.Value(dictionary["B1"])) + "," + 
         str(solver.Value(dictionary["B2"])) + "," + 
          str(solver.Value(dictionary["B3"])) + "," +  
           str(solver.Value(dictionary["B4"])) + "\n")
           
        outputText.writelines( str(solver.Value(dictionary["C1"])) + "," + 
         str(solver.Value(dictionary["C2"])) + "," + 
          str(solver.Value(dictionary["C3"])) + "," +  
           str(solver.Value(dictionary["C4"])) + "\n")
           
        outputText.writelines( str(solver.Value(dictionary["D1"])) + "," + 
         str(solver.Value(dictionary["D2"])) + "," + 
          str(solver.Value(dictionary["D3"])) + "," +  
           str(solver.Value(dictionary["D4"])) + "\n")   

text.close()
outputText.close()
