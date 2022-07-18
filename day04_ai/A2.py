import numpy

s = [87, 88, 89, 87, 88, 86, 87]
x = numpy.std(s)
print(x)

s = [33, 112, 139, 29, 60, 78, 98]
x = numpy.std(s)
print(x)

x = numpy.var(s)
print(x)
y = numpy.sqrt(x)
print(y)