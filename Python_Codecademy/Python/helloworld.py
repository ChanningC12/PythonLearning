import csv
f = open('EmployeeData.csv')
csv_f=csv.reader(f)

print (csv_f)

my_list=[2,3,4,5,6]
my_set=set(my_list)
print (my_set)


small_set = set([2, 3, 4, 5, 6])
large_set = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
print (large_set.difference(small_set))
