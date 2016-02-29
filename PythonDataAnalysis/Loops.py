# For Loop
a = ["a","b","c","d","e"]
for i in a:
    print i

for i in range(10):
    print i**2

b=range(5)    
for i in range(len(a)):
    b[i] += 3
print b
    
c = [1,4,9,16,25]
for i in range(len(c)):
    print c[i]-c[i-1]

# While Loop
work_needed = 5
work_completed = 0
while work_completed < work_needed:
    work_completed += 1
    print "Work Completed:", work_completed

aa = []
i = 0
while i<10:
    aa.append(i)
    i += 1
print aa

data = '''header,stuff,1,2
0,1,2,3
0,1,2,3
9,1,2,3
9,1,2,3
'''

print data.split("\n")

header=True
for row in data.split("\n"):
    if header:
        header=False
        print "I am a header, skipping"
        continue
    print row