grade=[100,100,90,40,80,100,85,70,90,65,90,85,50.5]
print ("Grades:",grade)

#print grades
def print_grades(grades):
    for i in grades:
        print (i)
print (print_grades(grade))

#Sum
def grades_sum(grades):
    total=0
    for i in grades:
        total += i
    return total
print (grades_sum(grade))

#Average
def grades_avg(grades):
    average=grades_sum(grades)/float(len(grades))
    return average
print (grades_avg(grade))

#variance
def grades_variance(scores):
    average=grades_average(scores)
    variance=0
    for score in scores:
        variance += ((average-score)**2)
    return variance/float((len(scores))
print (grades_variance(grade))
