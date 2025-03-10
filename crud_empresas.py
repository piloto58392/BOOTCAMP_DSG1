import os
import tabulate
import time

lista_empresas = [
    {
        'Razon Social':'Empresa ABC',
        'Web':'abc.com',
        'RUC':'20606060'
    }
]
ANCHO = 50
opcion = 0
while(opcion < 5):
    os.system("clear")
    print("="*ANCHO)
    print(" " * 10 + "CRUD DE EMPRESAS")
    print("="*ANCHO)
    print("""
         [1] REGISTRAR EMPRESA
         [2] MOSTRAR EMPRESA
         [3] ACTUALIZAR EMPRESA
         [4] ELIMINAR EMPRESA
         [5] SALIR
          """)
    print("="*ANCHO)
    opcion = int(input("INGRESE OPCION : "))
    os.system("clear")
    if(opcion == 1):
        print("="*ANCHO)
        print(" " * 10 + "[1] REGISTRAR EMPRESA")
        print("="*ANCHO)
        empresa = input("EMPRESA : ")
        web = input("WEB : ")
        ruc = input("RUC : ")
        dic_nuevo_empresa = {
            'empresa':empresa,
            'web':web,
            'ruc':ruc
        }
        lista_empresas.append(dic_nuevo_empresa)
        print(" EMPRESA REGISTRADA CON EXITO")
    elif(opcion == 2):
        print("="*ANCHO)
        print(" " * 10 + "[2] MOSTRAR EMPRESAS")
        print("="*ANCHO)
        cabeceras = ["EMPRESA","WEB","RUC"]
        tabla = [empresa.values() for empresa in lista_empresas]
        print(tabulate.tabulate(tabla,headers=cabeceras,tablefmt="grid"))
        input("presione ENTER para continuar...")
    elif(opcion == 3):
        print("="*ANCHO)
        print(" " * 10 + "[3] ACTUALIZAR EMPRESA")
        print("="*ANCHO)
        valor_busqueda = input('INGRESE WEB DE LA EMPRESA A ACTUALIZAR :')
        posicion_busqueda = -1
        for posicion in range(len(lista_empresas)):
            dic_empresa = lista_empresas[posicion]
            if valor_busqueda in dic_empresa.values():
                posicion_busqueda = posicion
                break
        if posicion_busqueda == -1:
            print("NO SE ENCONTRO LA EMPRESA SOLICITADA")
        else:
            print(f' EMPRESA A ACTUALIZAR : {lista_empresas[posicion_busqueda].get("nombre")}')
            nuevo_empresa = input("EMPRESA : ")
            nuevo_web = input("WEB : ")
            nuevo_ruc = input("RUC : ")
            dic_actualizar_empresa = {
                'empresa':nuevo_empresa,
                'web':nuevo_web,
                'ruc':nuevo_ruc
            }
            lista_empresas[posicion_busqueda] = dic_actualizar_empresa
        print("EMPRESA ACTUALIZADO CON EXITO...")
    elif(opcion == 4):
        print("="*ANCHO)
        print(" " * 10 + "[4] ELIMINAR EMPRESA")
        print("="*ANCHO)
        valor_busqueda = input('INGRESE WEB DE LA EMPRESA A ELIMINAR :')
        posicion_busqueda = -1
        for posicion in range(len(lista_empresas)):
            dic_empresa = lista_empresas[posicion]
            if valor_busqueda in dic_empresa.values():
                posicion_busqueda = posicion
                break
        if posicion_busqueda == -1:
            print("NO SE ENCONTRO LA EMPRESA SOLICITADA")
        else:
            lista_empresas.pop(posicion_busqueda)
            print('EMPRESA ELIMINADA!!!')
    elif(opcion == 5):
        print("="*ANCHO)
        print(" " * 10 + "[5] SALIR")
        print("="*ANCHO)
    else:
        print("="*ANCHO)
        print(" " * 10 + "OPCIÓN INVALIDA!!!")
        print("="*ANCHO)
        
    time.sleep(1)