import math
consumo_anual =float(input("ingrese el consumo anual de electricidad en kWh :"))
horas_sol = float(input("ingrese las horas promedio del sol por dia :"))
eficiencia =float(input("ingrese la eficiencia del panel solar en porcentaje (ej= 15 para 15% ) :"))
area_panel =float(input("ingrese la superficie promedio de un panel solar en m2 :"))
radiacion =float(input("ingrese la radiacion solar promedio por metro cuadrado en kWh/m2/dia :"))
potencia_diaria= area_panel*radiacion* eficiencia
potencia_anual = potencia_diaria*365
num_paneles = consumo_anual/potencia_anual
area_total= num_paneles*area_panel
#mostrar resultados
print ("potencia_diaria, 2), "kWh")
print ("Potencia anual generada por panel:", round(potencia_anual,2), "kWh")
print (numero de paneles necesarios:", num_paneles)
print (Área total requerida para los paneles:" round(area_total,2), "m2")


