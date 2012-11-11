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



def cronometer(callback):
   def callback_timer(*arguments):
      
       inicio = time.time()
       # Lanzamos funcion a ejecutar.
       ret = callback(*arguments)
       # Tiempo de fin de ejecucion.
       fin = time.time()
       # Tiempo de ejecucion.
       tiempo_total = fin - inicio
       # Devolvemos el tiempo de ejecucion.
        tiempo_total += "(s) to compute"
       return tiempo_total
   # Devolvemos la funcion que se ejecuta.

   return callback_timer


if len(sys.argv) < 2:
    print "Please input amount decimal digits"
else:

    if isinstance(int(sys.argv[1]),(long,int)):

        print "Computing "+sys.argv[1]+" decimal digits of pi\n"
        print cronometer(pi)(int(sys.argv[1]))
    else:
        print "Please input amount decimal digits"
