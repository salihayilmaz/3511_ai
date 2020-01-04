from ortools.sat.python import cp_model

model = cp_model.CpModel()
solver = cp_model.CpSolver()

def Kakuro(borders, outputFile):

    # 3x3
    
    firstRow1 = model.NewIntVar(0, 9, "firstRow1")
    secondRow1 = model.NewIntVar(0, 9, "secondRow1")
    thirdRow1 = model.NewIntVar(0, 9, "thirdRow1")

    firstPart_rows = [firstRow1, secondRow1, thirdRow1]
    model.AddAllDifferent(firstPart_rows)

    
    firstRow2 = model.NewIntVar(0, 9, "firstRow2")
    secondRow2 = model.NewIntVar(0, 9, "secondRow2")
    thirdRow2 = model.NewIntVar(0, 9, "thirdRow2")

    secondPart_rows = [firstRow2, secondRow2, thirdRow2]
    model.AddAllDifferent(secondPart_rows)
    
    firstRow3 = model.NewIntVar(0, 9, "firstRow3")
    secondRow3 = model.NewIntVar(0, 9, "secondRow3")
    thirdRow3 = model.NewIntVar(0, 9, "thirdRow3")

    thirdPart_rows = [firstRow2, secondRow2, thirdRow2]
    model.AddAllDifferent(thirdPart_rows)

    first_column = [firstRow1, firstRow2, firstRow3]
    second_column = [secondRow1, secondRow2, secondRow3]
    third_column = [thirdRow1, thirdRow2, thirdRow3]
    
    model.AddAllDifferent(first_column)
    model.AddAllDifferent(second_column)
    model.AddAllDifferent(third_column)

    model.Add(firstRow1 + secondRow1 + thirdRow1 == borders[3])
    model.Add(firstRow2 + secondRow2 + thirdRow2 == borders[4])
    model.Add(firstRow3 + secondRow3 + thirdRow3 == borders[5])
    model.Add(firstRow1 + firstRow2 + firstRow3 == borders[0])
    model.Add(secondRow1 + secondRow2 + secondRow3 == borders[1])
    model.Add(thirdRow1 + thirdRow2 + thirdRow3 == borders[2])

    
    status = solver.Solve(model)

    if status == cp_model.FEASIBLE:
        outputFile.writelines(str(borders[3]) + ", " + str(solver.Value(firstRow1)) + ", " + str(solver.Value(secondRow1)) + ", " + str(solver.Value(thirdRow1)) + "\n")

        outputFile.writelines(str(borders[4]) + ", " + str(solver.Value(firstRow2)) + ", " + str(solver.Value(secondRow2)) + ", " + str(solver.Value(thirdRow2)) + "\n")

        outputFile.writelines(str(borders[5]) + ", " + str(solver.Value(firstRow3)) + ", " + str(solver.Value(secondRow3)) + ", " + str(solver.Value(thirdRow3)))

inputFile = open("kakuro_input.txt", "r")
line = inputFile.readline()
lineInt = []

outputFile = open("kakuro_output.txt", "w")
outputFile.writelines("x, " + line)

while line:
    line = line.strip().split(",")
    for i in line:
        lineInt.append(int(i))
    line = inputFile.readline()

Kakuro(lineInt, outputFile)
