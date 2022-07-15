import matplotlib.pyplot as plt
import seaborn as sns
from numpy import random as r
#x = r.rand(10) #0~1실수 10개
x = r.normal(size=2000)
print(x)

#a = [0,1,2,3,4]
sns.distplot(x)
plt.show()