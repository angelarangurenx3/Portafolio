from datetime import datetime, timedelta

nombre = input("Nombre: ")
print (nombre)
fecha_de_ingreso = input("Fecha de Ingreso(DD-MM-AAAA): ")
fecha_de_egreso = input("Fecha de Egreso(DD-MM-AAAA): ")

dt1 = datetime.strptime(fecha_de_ingreso, '%d-%m-%Y')
dt2 = datetime.strptime(fecha_de_egreso, '%d-%m-%Y')

diferencia = dt2 - dt1

años_de_servicio = diferencia.days/365

print(f"\nAños de Servicio: {abs(años_de_servicio)} ")

salario_mensual = int(input("Salario Mensual: $"))
print (salario_mensual)
salario_diario = salario_mensual/20     #20 dias habiles

prestaciones1 = 30*años_de_servicio*salario_diario
print("Prestaciones Sociales: $", prestaciones1)

prestaciones2 = 5*salario_mensual

liquidacion = salario_mensual + prestaciones2

if años_de_servicio > 1:
    antiguedad = salario_mensual+5*salario_diario
    print ("Antiguedad: $", antiguedad)

elif años_de_servicio < 0.25:
    prestaciones1 = prestaciones2
    liquidacion
    print("Prestaciones: $", prestaciones1)
    print("Liquidacion: $", liquidacion)

dias_de_mora = int(input("Dias de Mora: "))

intereses = salario_diario*dias_de_mora
print("Intereses: $", intereses)

vacaciones = salario_mensual + 15*(salario_diario + años_de_servicio)
print("Vacaciones: $", vacaciones)

adelantos = int(input("Adelantos: $"))

anticipos = int(input("Anticipos: $"))

bono = int(input("Bono: $"))

vacaciones_no_disfrutadas = int(input("Dias de Vacaciones no Disfrutadas: "))

remuneracion_vacaciones_no_disfrutadas = salario_diario*vacaciones_no_disfrutadas

total_a_liquidar = prestaciones1 + prestaciones2 + antiguedad + liquidacion + dias_de_mora + intereses + remuneracion_vacaciones_no_disfrutadas
print("Total a Liquidar= $", total_a_liquidar)