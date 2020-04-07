import numpy as np
import random
from tqdm import tqdm
import matplotlib.pyplot as plt
import matplotlib.style as style

rango = [0,100]

def simulacion_juego(numero_escogido):
''''Simular la escogencia para valores aleatorios a,b;
    estos valores no pueden ser iguales por comodidad''''
    
    a = 0
    b = 0
    
    while a == b:
        a = random.randint(rango[0], rango[1])
        b = random.randint(rango[0], rango[1])
    
    seleccion_etrategia = a if a >= numero_escogido else b
    seleccion_aleatoria = random.sample([a,b], 1)[0]
    estrategia_correcto = 1 if seleccion_estrategia == max([a,b]) else 0
    aleatorio_correcto = 1 if seleccion_aleatoria == max([a,b]) else 0
 
    return dict(zip(["Estrategia", "Aleatoria"], [estrategia_correcto, aleatoria_correcto]))
    
n_simulaciones = 25000

probabilidad_estrategia  = []
probabilidad_aleatorio = []

for numero in tqdm(range(rango[1] + 1)):
    resultado_estrategia = []
    resultado_aleatorio = []

    for _ in range(n_simulaciones):
        resultado_estrategia.append(simulacion_juego(numero)['Estrategia'])
        resultado_aleatorio.append(simulacion_juego(numero)['Aleatoria'])
    
    probabilidad_estrategia.append(sum(resultado_estrategia)/n_simulaciones)
    probabilidad_aleatorio.append(sum(resultado_aleatorio)/n_simulaciones)
    
    
# Gráfica de la simulación

plt.style.use("seaborn")
plt.figure(figsize = (13,10))
plt.plot(range(rango[1] + 1), probabilidad_estrategia, label = 'Usando estrategia')
plt.plot(range(rango[1] + 1), probabilidad_aleatorio, label = 'Al azar')
plt.title("Comparación de la razón de éxitos/fracasos")
plt.xlabel("Número escogido para usar la estrategia")
plt.ylabel("Razón de éxitos")
plt.legend()

