import numpy as np 

def main():
	#vs = input("Vs = ")
	#mu = input("Mu = ")

	print("")
	print("Holes or electrons?")
	he = input(" [h / e] = ")
	T = float(input("Temp (K) = "))
	f = float(input("F (V/cm) = "))

	if he == "e":
		A = 5.66 * 1E5 #m
		P = 1.68
		B = 1.3 * 1E7 #m/s
		phi = 200    #K
	else:
		A = 1.65 * 1E5
		P = 2.4
		B = 1.2 * 1E7
		phi = 200
		

	#mu = A / T*p (A = 5.66E3, P = 1.68) e (1.65E5, 2.4) h
	#Vs = 1.2 e, 1.1 h *10^7

	mu = A / T**P *10000 #cm^2 / Vs
	Tan_H = np.tanh(phi / (2 * T))
	vs = B * Tan_H**0.5
	fc = vs / mu

	print("")
	print("Mu = ", mu)
	print("Vs = ", vs)
	print("Fc = ", fc)
	print("")

	bot = 1.0 + (f / fc)**2.0

	v = ( vs * (f / fc) ) / bot**0.5

	print("V = ", v, " cm/s")
	print("")










main()
