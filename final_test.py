"""
We want to read in a file
Capture the number of grades
The average grade
Percentage of grades above the average grade
Exit the file
Display the correct answers to the user
"""
"""
main
file = Final.txt
percentaboveaverage(file)

percentageaboveaverage(file)
infile
gradelist[read per line]
infile.close
length = len(gradelist)
sumofgrades = sum(gradelist)
avg = sumofgrades / length
print(number of grades)
print(average)
count = 0
if item in gradelist > average
add 1 to count
percentaboveavg = count / length
print percentaboveavg
"""
def main():
    file = "Final.txt"
    calculate_percent_above_average(file)

def calculate_percent_above_average(file):
    infile = open(file, 'r')
    GradeList = [int(line.rstrip()) for line in infile]
    infile.close()
    TotalGrades = len(GradeList)
    SumOfGrades = sum(GradeList)
    AverageOfGrades = SumOfGrades / TotalGrades
    print("The number of grades is: ", TotalGrades)
    print("The average grade was: ", AverageOfGrades)
    NumberOfGradesAboveAverage = 0
    for item in GradeList:
        if item > AverageOfGrades:
            NumberOfGradesAboveAverage += 1
    PercentageAboveAverage = NumberOfGradesAboveAverage / TotalGrades
    print("Percentage of grades above average was: ", end = " ")
    print("{0:.2%}".format(PercentageAboveAverage))


main()