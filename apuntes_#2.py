# n1 = 10
# msg = "hola"

# print(n1,msg)
# print(str(n1)+msg)

#fstrings

# print(f"{n1} {msg}")
#hacer una funcion que reciba el nombre de una persona el año de nacimiento y el año actua
#retornando el mensaje "hola <nombre> tienes <edad> años"

# añoac = input("ingrese el año actual: ")

# añonac = input("ingrese el año de nacimiento: ")

# name = input("ingresa el nombre")

# if __name__=="__main__":
#     edad1 = ((int(añoac))-(int(añonac)))
#     print("hola",name,"tienes",edad1,"años")

# from pickletools import read_uint1


# def mensaje(name:str,a_nac:int,a_actual:int)->str:
#     edad = a_actual - a_nac
#     return f"hola {name}, tienes {edad} años"

# if __name__ =="__main__":
#     print(mensaje("alex",1980,2022))

# def calcular_edad(a_nac:int,a_actual:int)-> int:
#     return a_actual - a_nac

# def mensaje3(name:str,a_nac:int,a_actual:int)->str:
#     return f"hola {name}, tienes {calcular_edad(a_nac, a_actual)}"

# if __name__ =="__main__":
#     print(mensaje3("regina",2010,2022))


#Listas
# alumnos = ["hugo", "paco", "luis", "Lupita"]

# print(f"alumnos: {alumnos}")

# for i in range(4):
#     print(f"alumnos: {alumnos[i]}")

#indice la forma de entrar a una lista

#tuplas
# alumnos = ("hugo", "paco", "luis", "Lupita")

# print(f"alumnos: {alumnos}")

# for i in range(len(alumnos)):
#     print(f"alumnos {i+1}: {alumnos[i]}")


#sets
# alumnos = {"hugo", "paco", "luis", "Lupita"}
# print(f"alumnos: {alumnos}")

#diccionarios
# alumnos = {"nombre": "Hugo", "Materia1": 10, "Materia2": 5}
# print(f"alumnos: {alumnos}")
# print(f"Alumno: {alumnos['nombre']}")


#listas y sets
# numeros_list =[1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,84,2,3,4,]
# numeros_set ={1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,84,2,3,4,}
# print(numeros_list)
# print(numeros_set)


# h = ["nombre", "est_dat", "prog func", "ingles"]
# alumnos = ["hugo", "paco", "luis", "Lupita"]
# m_e_d = [9,8,7,9]
# m_p_f = [10.5,5.6,6.9,7]
# m_i = [5,8,7,8]

# ancho =15
# print(f"{h[0]:^{ancho}}{h[1]:^10}{h[2]:^10}{h[3]:^10}")
# for i in range (len(alumnos)):
#     print(f"{alumnos[i]:^10}{m_e_d[i]:^10}{m_p_f[i]:^10}{m_i[i]:^10}")


# def reporte(fmt:int):

#     print(f"{h[0]:^{fmt}}{h[1]:^{fmt}}{h[2]:^{fmt}}{h[3]:^{fmt}}")
#     for i in range (len(alumnos)):
#         print(f"{alumnos[i]:*<{fmt}}{m_e_d[i]:+^{fmt}}{m_p_f[i]:#>{fmt}}{m_i[i]:-^{fmt}}")


# if __name__=="__main__":
#     reporte(15


# numerobig = 12123456789123456787
# print(f"{numerobig:,d}")
# #fijar cantidad de decimal
# numeropi = 3.1592678547858
# #notacion cientifica
# print(f"{numeropi:.3f}")
# print(f"{numeropi:e}")
# print(f"{numeropi:.2e}")
# #porcentaje
# numeroporciento = 0.258478585
# print(f"{numeroporciento:%}")
# print(f"{numeroporciento:.2%}")


# #numeros binarios
# print(f"{25:x}")
# #unicodes
# print(f"{65:c}")
# #hexadecimal
# print(f"{255:x}")
# #octal
# print(f"{255:o}")


"""
Escriba una funcion que genere una tabla de multiplicar recibiendo como argumento 
la cantidad de numeros y la tabla a generar.
"""
def producto(a:int,b:int)->int: return a*b

def tablas (m:int,n:int,fmt:int):
    for i in range(1,m+1):
        tabla(n,i,fmt)
        print(f"{13:c}")

def tabla(n:int,t:int, fmt:int):
    for i in range(1,n+1):
        print(f"{t:^{fmt}}x{i:^{fmt}}={i*t:^{fmt}}")
        


if __name__=="__main__":
    tablas(15,15,6)
    # print(f"{13:c}")
    # tabla(10,7,5)









