import numpy as np

a = np.array([1,2,3,4])
x = [True, True, False, True]
c1 = a[x] #[1,2,4] True인것만 뽑아서 배열을 생성
print(c1) 

#c2 = a>2 #[False False True True]
c2 = a%2==0 #[False True False True]
print(c2)
c3 = a[c2]
print(c3)