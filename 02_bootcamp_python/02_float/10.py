#Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
import math
n1 = float(input("Digite o raio do circulo para cálculo da área: "))
pi = math.pi
area = pi * n1 ** 2
print(f"{area:.2f}")