import math
consumo_anual =float(input("ingrese el consumo anual de electricidad en kWh :"))
horas_sol = float(input("ingrese las horas promedio del sol por dia :"))
eficiencia = float(input("ingrese la eficiencia del panel solar en porcentaje (ej= 15 para 15% ) :")) / 100
area_panel =float(input("ingrese la superficie promedio de un panel solar en m2 :"))
radiacion =float(input("ingrese la radiacion solar promedio por metro cuadrado en kWh/m2/dia :"))
potencia_diaria= area_panel*radiacion* eficiencia
potencia_anual = potencia_diaria*365
num_paneles = consumo_anual/potencia_anual
area_total= num_paneles*area_panel
#mostrar resultados
print(f"Potencia diaria generada por un panel: {potencia_diaria} kWh")
print(f"Potencia anual generada por un panel: {potencia_anual} kWh")
print(f"Número de paneles necesarios: {num_paneles}")
print(f"Área total requerida para los paneles: {area_total} m²")


