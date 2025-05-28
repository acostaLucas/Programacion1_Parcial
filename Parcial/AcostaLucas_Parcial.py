###############################################################################################################################

# 1)    Función cargar_matriz_notas(): Recibe dos enteros n y m y permite cargar n x m 
#       notas válidas entre 1 y 10 inclusive. La validación debe hacerse dentro de esta función. 

###############################################################################################################################


# declaro la funcion pedida en la cual se ingrese como variable "n" los alumnos y 
# como variable "m" la cantidad de notas 
def cargar_matriz_notas(n, m):
    if n != m:
        # informa al usuario de la problematica al ingresar los datos 
        print("Error: La clas de Programación I debe tener igual cantidad de alumnos y exámenes.")
        
        # retorna la matriz vacía ya que trata de un error
        return []

    # Defino la matriz a utilizar.
    programacionI = []

    # Itero las listas de alumnos y examenes
    for alumno in range(n):

        # declaro un array vacío para utilizarlo de almacen para cada alumno
        fila = []

        #itero los examenes ingresados y aplico las validaciones
        for examen in range(m):
            while True:
                try:
                    # defino el input y me aseguro de que ingrese un numero entero.
                    nota = int(input(f"Ingrese la nota del alumno n° {alumno+1}, nota del examen: {examen+1} (1-10): "))

                    # validacion pedida en el examen: nota entre el 1 y el 10.
                    if 1 <= nota <= 10:

                        # agrego la nota a cada alumno
                        fila.append(nota)
                        break
                    else:

                        # en caso de que la nota no sea entre 1 y 10
                        print("La nota debe estar entre 1 y 10.")

                except ValueError:

                    # catch para caso inválido, el usuario no ingresa un numero entero.
                    print("Entrada inválida. Debe ingresar un número entero.")

        # por ultimo se agrega a la matriz de la clase la fila, es decir cada alumno con sus notas 
        programacionI.append(fila)

    # retorna la matriz con sus valores
    return programacionI

###############################################################################################################################

# 2)    Función porcentaje_aprobados(): Calcula el porcentaje de exámenes aprobados (nota ≥ 6) por cada alumno 
#       y muestra un resumen individual. Usar contadores y acumuladores.

###############################################################################################################################

def porcentaje_aprobados(programacionI):

    #itero la lista programacion I 
    for i, fila in enumerate(programacionI):

        # para el total de examenes saco la cantidad de filas (alumnos) que posee el array 
        total_examenes = len(fila)

        # instancio en 0 los aprobados
        aprobados = 0

        # recorro las filas de alumnos y aplico la validacion de mayor o igual a 6 para los aprobados
        for nota in fila:
            if nota >= 6:
                aprobados += 1

        # saco la cuenta del porcentaje y lo imprimo en pantalla.
        porcentaje = (aprobados / total_examenes) * 100
        print(f"Alumno n° {i+1}: {aprobados} exámen/es aprobado/s de {total_examenes}, ({porcentaje:.2f}%)")

# Bloque principal
def main():
    
    # Defino un try - catch para el facil rastreo de errores.
    try:
        # pide por consola el numero de alumnos y la cantidad de examenes en total.
        n = int(input("Ingrese la cantidad de alumnos: "))
        m = int(input("Ingrese la cantidad de exámenes: "))

        # llamado a la funcion de cargar la matriz de notas
        notas = cargar_matriz_notas(n, m)

        # en caso de notas retornar valores, los muestra en pantalla iterando las filas, cada alumno
        if notas:

            # muestro en pantalla los datos obtenidos.
            print("Notas para la clase de Programacion I:")

            # itero la lista enumerada de notas e imprimo en pantalla el dato del alumno, sus notas
            for alumno, fila in enumerate(notas):
                print(f"Alumno: {alumno+1}: {fila}")

            print("\nResumen de aprobados por alumno:")
            porcentaje_aprobados(notas)

    except ValueError:

        # catch en caso de producirse un error en el valor del input.
        print("Debe ingresar números enteros válidos para los alumnos y exámenes.")

# Ejecuto el programa - python .\Parcial\AcostaLucas_Parcial.py
if __name__ == "__main__":
    main()