print("# Nomina del Empleado H #")
print("========================================")

nombre = input("| Digite el nombre y apellido del empleado  :  ")
cedula=int(input("| Digite su cedula: "))
salario = float(input("| Digite el salario mensual  :  "))
dias_laborados = int(input("| Digite los días laborados  :  "))
horas_extras_diurnas = int(input("| Digite la cantidad de horas extras diurnas  :   "))
horas_extras_nocturnas = int(input("| Digite la cantidad de horas extras nocturnas  :   "))
horas_extras_festivas = int(input("| Digite la cantidad de horas extras festivas  :   "))
horas_extras_festivas_diurnas= int(input("| Digite la cantidad de horas extras festivas diurnas  :   "))
horas_extras_festivas_nocturnas= int(input("| Digite la cantidad de horas extras festivas nocturnas :   "))
auxilio_transporte = 162000

print("========================================")

print("# Cálculo del valor de la hora ordinaria")
valor_hora = salario // 30 // 7

print("# Cálculo de horas extras")
total_extras_diurnas = horas_extras_diurnas * valor_hora * 0.25
total_extras_nocturnas = horas_extras_nocturnas * valor_hora * 0.75
total_extras_festivas = horas_extras_festivas * valor_hora * 100
total_extras_festivas_diurnas = horas_extras_festivas_diurnas * valor_hora * 2
total_extras_festivas_nocturnas = horas_extras_festivas_nocturnas * valor_hora * 2.5

print("# Suma de todas las horas extras")
total_extras = total_extras_diurnas + total_extras_nocturnas + total_extras_festivas+total_extras_festivas_diurnas+total_extras_festivas_nocturnas

print("# Cálculo de salario total")
salario_diario = salario // 30
total_salario = salario_diario * dias_laborados

print("# Cálculo de devengados")
tot_devengado = total_salario + total_extras + auxilio_transporte

print("# Cálculo de deducciones")
salud = salario * 4 // 100
pension = salario * 8 // 100
sindicato = salario * 2 // 100  
retencion = salario * 1.5 // 100  

tot_deducido = salud + pension + sindicato + retencion

print("# Cálculo de neto a pagar")
neto_apagar = tot_devengado - tot_deducido

print("# Impresión de resultados")
print("|================================|")
print("| Nombre :  ", nombre)
print("| Cedula : ",cedula)
print("| Salario :  " f"${salario :.0f}")
print("| Días Laborados :  ", dias_laborados)
print("| Auxilio de Transporte : " f"${auxilio_transporte :.0f}")
print("|================================|")
print("| Salud: " f"${salud :.0f}")
print("| Pensión: " f"${pension :.0f}")
print("| Sindicato: " f"${sindicato :.0f}")
print("| Retención en la fuente: " f"${retencion :.0f}")
print("|================================|")
print("| Total salario :  " f"${total_salario :.0f}")
print("| Horas Extras Diurnas :  " f"${total_extras_diurnas :.0f}")
print("| Horas Extras Nocturnas :  " f"${total_extras_nocturnas :.0f}")
print("| Horas Extras Festivas :  " f"${total_extras_festivas :.0f}")
print("| Total Horas Extras :  " f"${total_extras :.0f}")
print("| Valor Horas Ordinarias :  " f"${valor_hora :.0f}")
print("| Horas Extras Festivas diurnas :" f"${total_extras_festivas_diurnas :.0f}")
print("| Horas Extras Festivas nocturnas :" f"${total_extras_festivas_nocturnas :.0f}")
print("|================================|")
print("| Total Devengado:  " f"${tot_devengado :.0f}")
print("|================================|")
print("| Total Deducido:  " f"${tot_deducido :.0f}")
print("|================================|")
print("| Neto a Pagar  :  " f"${neto_apagar :.0f}")
print("|================================|")

input("presiona enter para salir...")

      
