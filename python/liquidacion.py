print("# Liquidacion del Empleado H #")
print("========================================")

nombre = input("| Digite el nombre y apellido del empleado  :  ")
cedula=int(input("|Digite su cedula: "))
salario = float(input("| Digite el salario mensual  :  "))
dias_laborados = int(input("| Digite los días laborados  :  "))
cesantias=("| Digite las cesatias  :  ")
intereses_cesantias=("| Digite los intereses  de las cesantias :  ")
primas_servicios=("| Digite las primas de servicios  :  ")
vacaciones=("| Digite los días de vacaciones  :  ")

print("========================================")

cesantias = salario * dias_laborados / 360
intereses_cesantias = cesantias * dias_laborados * 0.12 / 360
primas_servicios = salario * dias_laborados / 360
vacaciones = salario * dias_laborados / 720

tot_devengado = cesantias + intereses_cesantias + primas_servicios + vacaciones
neto_apagar = tot_devengado

print("=======================================")
print("- Nombre : nombre ")
print("- Cedula : ",cedula)
print("- Salario : " f"${salario:.0f}"salario)
print("- Días Laborados :  ", dias_laborados)
print("========================================")

print("cesantias :" f"${cesantias:.0f}")
print("Intereses_cesantias :" f"${intereses_cesantias :.0f}")
print("Primas_servicios :" f"${primas_servicios :.0f}")
print("Vacaciones :" f"${vacaciones :.0f}")
print("===============================================================")
print("Neto_Apagar :" f"${neto_apagar :.0f}")
print("===============================================================")
input("Presiona enter para salir...")

