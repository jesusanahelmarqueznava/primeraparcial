#import sumar as s
#import restar as r
#import multiplicar as m
#import dividir as d
#import cuadrado as c

#aqui lo que se hace es importar las operaciones que requerimos de varios archivos.



#if __name__ == "__main__":
 #  print(s.sumar(5,6))
  # print(r.restar(6,10))
   #print(m.multiplicar(6,10))
   #print(d.dividir(6,10))
   #print(c.cuadrado(6))

#aqui se muestra el resultado de lo importado de otros archivos.

import ops.operacione as op

# se esta importando las operaciones que requerimos de otro archivo.

if __name__ == "__main__":
    print(op.restar(2,3))
    print(op.sumar(2,3))
    print(op.multiplicar(2,3))
    print(op.dividir(2))

#aqui se muestra el resultado de lo importado de otro archivo.
  