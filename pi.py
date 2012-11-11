# Using Machin formula
# http://en.literateprograms.org/images/math/7/9/e/79e33327955cad64ea3613b02e7c8e2d.png
# Time function by 
# http://elviajedelnavegante.blogspot.com.es/2010/06/calcular-tiempos-de-ejecucion-en-python.html
import sys, time

def arccot(x, unity):
    sum = xpower = unity // x
    n = 3
    sign = -1
    while 1:
        xpower = xpower // (x*x)
        term = xpower // n
        if not term:
            break
        sum += sign * term
        sign = -sign
        n += 2
    return sum
def pi(digits):
    unity = 10**(digits + 10)
    pi = 4 * (4*arccot(5, unity) - arccot(239, unity))    
    print pi // 10**10



def cronometro(funcion):
   def funcion_a_ejecutar(*argumentos):
      
       inicio = time.time()
       # Lanzamos funcion a ejecutar.
       ret = funcion(*argumentos)
       # Tiempo de fin de ejecucion.
       fin = time.time()
       # Tiempo de ejecucion.
       tiempo_total = fin - inicio
       # Devolvemos el tiempo de ejecucion.
       return tiempo_total
   # Devolvemos la funcion que se ejecuta.

   return funcion_a_ejecutar


if len(sys.argv) < 2:
    print "Please input amount decimal digits"
else:

    if isinstance(int(sys.argv[1]),(long,int)):

        print "Searchig "+sys.argv[1]+" decimal digits of pi\n"
        print cronometro(pi)(int(sys.argv[1]))
    else:
        print "Please input amount decimal digits"
