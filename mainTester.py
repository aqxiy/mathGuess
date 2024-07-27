import random

X_lb = 2
X_ub = 7

Y_lb = 1
Y_ub = 5

Z_lb = 0
Z_ub = 10

X_coeff = 3
Y_coeff = 7
Z_coeff = 5

random_X = random.randint(X_lb, X_ub)
random_Y = random.randint(Y_lb, Y_ub)
random_Z = random.randint(Z_lb, Z_ub)

randomValue = random_X * X_coeff + random_Y * Y_coeff + random_Z * Z_coeff



print('X_coeff == 3')
print('Y_coeff == 7')
print('Z_coeff == 5')

print('RNGv: ', randomValue)

randomSelector = random.randint(1,3)

if randomSelector == 1:
	print('X var == ', random_X)
elif randomSelector == 2:
	print('Y var == ', random_Y)
elif randomSelector == 3:
	print('Z var == ', random_Z)

Xg, Yg, Zg = input('enter 3 vars:').split()

Xg = int(Xg)
Yg = int(Yg)
Zg = int(Zg)

print(Xg, Yg, Zg)

print('INT ==', Xg * X_coeff + Yg * Y_coeff + Zg * Z_coeff)

foundAnswer = 0

if Xg == random_X and Yg == random_Y and Zg == random_Z:
	foundAnswer = 1

while (not foundAnswer):
	print("Try again...")
	print('RNGv: ', randomValue)
	if randomSelector == 1:
		print('X var == ', random_X)
	elif randomSelector == 2:
		print('Y var == ', random_Y)
	elif randomSelector == 3:
		print('Z var == ', random_Z)
	Xg, Yg, Zg = input('enter 3 vars:').split()

	Xg = int(Xg)
	Yg = int(Yg)
	Zg = int(Zg)

	print(Xg, Yg, Zg)
	print('INT ==', Xg * X_coeff + Yg * Y_coeff + Zg * Z_coeff)

	if Xg == random_X and Yg == random_Y and Zg == random_Z:
		foundAnswer = 1

print("endloop")
