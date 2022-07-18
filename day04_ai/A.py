import numpy 

#(1) Standard Deviation
s = [87,88,89,87,88,86,87]
x = numpy.std(s)
print(x) #0.9035079029052513

s = [33,112,139,29,60,78,98]
x = numpy.std(s)
print(x) #37.84

#(2) Variance
x = numpy.var(s)
print(x) #1432.24
y = numpy.sqrt(x)
print(y) #37.84