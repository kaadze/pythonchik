import numpy as np
array1=[]
array2=[]
def createArray():
	
	#1 матрица
	print("Введите количество строк первой матрицы:")
	i1=int(input())
	print("Введите количество столбцов первой матрицы:")
	j1=int(input())
	print("Введите элемент матрицы:")
	e1=int(input())
	

	for i in range (i1):
		array1.append([])
		for j in range(j1):
			array1[i].append(e1)
			print("Введите элемент матрицы:")
			e1=int(input())
	
	print("Матрица:")
	for m1 in range(j1):
		print(array1[m1])

createArray()

def createArray2():
	
	#2 матрица
	print("Введите количество строк второй матрицы:")
	i2=int(input())
	print("Введите количество столбцов второй матрицы:")
	j2=int(input())
	print("Введите элемент матрицы:")
	e2=int(input())
	

	for i in range (i2):
		array2.append([])
		for j in range(j2):
			array2[i].append(e2)
			print("Введите элемент матрицы:")
			e2=int(input())
	
	print("Матрица:")
	for m2 in range(i2):
		print(array2[m2])

createArray2()

print ("Что сделать с матрицами?")
operacia=(input())

if operacia=="Умножение":
	print(np.array(array1)*np.array(array2))
elif operacia=="Сложение":
	print(np.array(array1)+np.array(array2))
elif operacia=="Вычитание":
	print(np.array(array1)-np.array(array2))
elif operacia=="Деление":
	print(np.array(array1)/np.array(array2))
else:
	print("Надо было ввести 'Умножение'/'Сложение'/'Вычитание'/'Деление'")