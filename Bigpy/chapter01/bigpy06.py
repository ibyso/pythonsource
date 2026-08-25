# numpy : 고성능의 수치계산 지원(C언어로 구성)
import numpy as np

# 수치 계산용 배열 np.array
arr = np.array([1,2,3])
print(arr)
print(type(arr))

print('-'*10)
matrix = np.array([[1,2,3],[4,5,6]])
print(matrix)


print('-'*10)
a = np.array([[1,2],[3,4]])
b = np.array([[1,1],[1,1]])
c = a+b
print(c)



print('-'*10)
aa = np.array([[1,2],[3,4]])
k = 10
ak = k * aa
print(ak) 