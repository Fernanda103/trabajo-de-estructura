from cargo import Cargo
from departamento import Departamento
from empleado import Empleado
from menu import Helper

import os

def buscarcargo(cod):
  car = 0
  for pos in range (0,len(Cargo.cargos)):
    cargo1 = Cargo.cargos[pos]
    if cargo1["cargo"] == cod:
      car = cargo1["cargo"]
      break
  return car

def buscardept(dep):
  depts = 0
  for pos in range (0,len(Departamento.departamentos)):
    deptos = Departamento.departamentos[pos]
    if deptos["nombre"] == dep:
      depts = deptos["nombre"]
      break
  return depts

helper = Helper()
lista = ["1) Cargo ","2) Departamento ","3) Empleados ","4) Salir"]
opcion = ""

while opcion !="4":
  os.system("cls")
  opcion =helper.menu(lista, "Menú Ficha Personal")
  os.system("cls")
  if opcion == "1":
    opcion1=""
    while opcion1 !=3:
      os.system("cls")
      print("*"*15,"MANTENIMIENTO DE CARGOS","*"*15)
      opcion1 = helper.menu(["1) Ingreso","2) Consulta", "3) Salir"], "Sub-menú Cargo")
      os.system("cls")
      if opcion1 == "1":
        print("*"*15,"INGRESO DE CARGOS","*"*15)
        nombre = input("Nombre del Cargo: ")
        val = len(nombre)
        while not val >2 and val <=20:
          nombre = input("Nombre del Cargo: ")
          val = len(nombre)
        crgo = Cargo(nombre)
        cargo = crgo.registro()
        Cargo.cargos.append(cargo)
        input("\n"
          "Datos ingresados exitosamente, Presiona una tecla para continuar:)")
      elif opcion1 == "2":
        print("*"*15,"LISTADO DE CARGOS","*"*15)
        print("Codigo"," "*5,"Descripcion"," ")
        for crgo in Cargo.cargos:
          codigo = crgo ["codigo"]
          desc= crgo ["cargo"]
          codig = buscarcargo(desc)
          print(" "*2,codigo," "*8,codig)
        print("*"*59)
        input("\n"
         "Presione una tecla para continuar...")
      elif opcion1 == "3":
        input("Saliendo..." 
        "\n" "Presione una tecla para continuar...")
        break

  elif opcion =="2":
    os.system("cls")
    opcion1 = ""
    while opcion1 !=3:
      os.system("cls")
      print("*"*15,"MANTENIMIENTO DE DEPARTAMENTOS","*"*15)
      opcion1 = helper.menu(["1) Ingreso","2) Consulta", "3) Salir"], "Sub-menú Departamento")
      os.system("cls")
      if opcion1 == "1":
        print("*"*15,"INGRESO DE DEPARTAMENTOS","*"*15)
        nombre = input("Nombre del Departamento: ")
        val = len(nombre)
        while not val >5 and val <=20:
          nombre = input("Nombre del Departamento: ")
          val = len(nombre)
        dpto = Departamento(nombre)
        depar = dpto.registro()
        Departamento.departamentos.append(depar)
        input("\n"
          "Datos ingresados exitosamente, Presiona una tecla para continuar:)")
      elif opcion1 == "2":
        print("*"*15,"LISTADO DE DEPARTAMENTOS","*"*15)
        print("Departamento"," "*5,"Nombre"," ")
        for dpto in Departamento.departamentos:
          depta = dpto ["departamento"]
          d_nom= dpto ["nombre"]
          nom_d = buscardept(d_nom)
          print(" "*4,depta," "*8,nom_d)
        print("*"*66)
        input(
        "\n" "Presione una tecla para continuar...")
      elif opcion1 == "3":
        input("Saliendo..." 
        "\n" "Presione una tecla para continuar...")
        break
        
  elif opcion == "3":
    os.system("cls")
    opcion1 = ""
    while opcion1 !=3:
      os.system("cls")
      print("*"*15,"MANTENIMIENTO DE EMPLEADOS","*"*15)
      opcion1 = helper.menu(["1) Ingreso","2) Consulta", "3) Salir"], "Sub-menú Empleados")
      os.system("cls")
      if opcion1 == "1":
        print("*"*15,"INGRESO DE EMPLEADOS","*"*15)
        nombre= input("Nombre del Empleado: ")
        val = len(nombre)
        while not val >= 3 and val <=20:
          nombre = input("Nombre del Empleado: ")
          val = len(nombre)
        cedu= input("Cédula del Empleado: ")
        val = len(cedu)
        while val != 10:
          cedu = input("Cédula del Empleado: ")
          val = len(cedu)
        cod_Cargo= input("Cargo del Empleado: ")
        car = buscarcargo(cod_Cargo)
        while car != cod_Cargo:
          cod_Cargo= input("Cargo del Empleado: ")
          car = buscarcargo(cod_Cargo)
        cod_Departamento= input("Departamento del Empleado: ")
        depto = buscardept(cod_Departamento)
        while depto != cod_Departamento:
          cod_Departamento= input("Departamento del Empleado: ")
          depto = buscardept(cod_Departamento)
        sueldo= float(input("Sueldo del Empleado: "))  
        while sueldo %1 == 0:
          sueldo= float(input("Sueldo del Empleado: "))  
        empl = Empleado(nombre,cedu,cod_Cargo,cod_Departamento,sueldo)
        empleado = empl.registro()
        Empleado.Empleados.append(empleado)
        input("\n"
        "Datos ingresados satisfactoriamente, presione una tecla para continuar...")
      elif opcion1 == "2":
        print("*"*25,"LISTADO DE ENPLEADOS","*"*25)
        print("Codigo"," "*6,"Nombre"," "*6,"Cedula"," "*6,"Cargo"," "*6,"Departamento"," "*6,"Sueldo")
        for empl in Empleado.Empleados:
          codigo = empl["codigo"]
          des_no=empl["nombre"]
          ced =empl["cedula"] 
          cgo =empl["cargo"]
          bus_cg = buscarcargo(cgo)
          detm = empl["departamento"]
          bus_dp = buscardept(detm)
          suel=empl["sueldo"]
          print(" "*2,codigo," "*8,des_no," "*(10-len(des_no)),ced," "*(14-len(ced)),bus_cg," "*(11-len(bus_cg)), bus_dp," "*(18-len(bus_dp)), suel)
        print("*"*92)
        input("\n"
          "Presione una tecla para continuar...")
      elif opcion1 == "3":
        input("Saliendo..." 
        "\n" "Presione una tecla para continuar...")
        break
  elif opcion == "4":
    print("¡Gracias por Preferirnos!")
    print("¡Tenga un Buen Dia!")          