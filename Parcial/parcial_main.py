# Importo el archivo py previo con los punto 1 y 2 del ejercicio.
import AcostaLucas_Parcial

###############################################################################################################################

# 3) Función mejor_promedio(): Calcula el promedio de cada alumno y
# determina cuál tiene el mejor promedio. Retorna el índice del alumno y
# el valor del promedio.

###############################################################################################################################

def mejor_promedio(programacionI):
    # instancio las variables del mejor alumno y promedio de c/u
    mejor_alumno = -1
    mejor_promedio = -1

    # itero la matriz por alumno (var fila), saco la cuenta del promedio y 
    # guardo el mejor alumno y su nota y posterior retorno las dos variables 
    for i, fila in enumerate(programacionI):
        suma = 0
        for nota in fila:
            suma += nota
        promedio = suma / len(fila)
        if promedio > mejor_promedio:
            mejor_promedio = promedio
            mejor_alumno = i

    return mejor_alumno, mejor_promedio

###############################################################################################################################

# 4) Función buscar_nota(): Recibe la matriz y una nota buscada, y
# retorna una lista con todas las posiciones (fila, columna) donde aparece
# esa nota exacta.

###############################################################################################################################

# defino la funcion que busca la nota, tomando los parametros matriz(programacionI) y 
# la nota que busca el usuario
def buscar_nota(programacionI, nota_buscada):
    # instancio el array que voy a utilizar en el retorno
    posiciones = []

    # itero el array programacionI, para obtener la fila y la columna de la matriz
    # luego lo agrego en la matriz instanciada previamente y lo retorno
    for i in range(len(programacionI)):
        for j in range(len(programacionI[i])):
            if programacionI[i][j] == nota_buscada:
                posiciones.append((i, j))
    return posiciones

# uso del main del archivo actual - parcial_main.py, importando las funciones dentro 
# del archivo previo - AcostaLucas_Parcial.py => cargar_matriz_notas y porcentaje_aprobados
def main():
    try:
        n = int(input("Ingrese la cantidad de alumnos: "))
        m = int(input("Ingrese la cantidad de exámenes: "))
        notas = AcostaLucas_Parcial.cargar_matriz_notas(n, m)

        if notas:
            print("\nNotas de la clase Programación I:")
            for i, fila in enumerate(notas):
                print(f"Alumno {i+1}: {fila}")

            print("\nPorcentaje de aprobación de exámenes por alumno:")
            AcostaLucas_Parcial.porcentaje_aprobados(notas)

            # llamo a la funcion y le paso el parametro de notas (es un array)
            idAlumno, promedio = mejor_promedio(notas)
            print(f"\nEl alumno con mejor promedio, es {idAlumno + 1} con un promedio de {promedio:.2f}")

            # le pregunto al usuario si desea buscar 
            # una nota especifica
            respuesta = input("\n¿Desea buscar una nota en la clase Programación I? (y/n): ").strip().lower()

            # en caso de "y", le pide por consola el numero de la nota a buscar
            # en caso de "n" / otro comando, finaliza el programa e imprime el mensaje
            if respuesta == "y":
                while True:
                    try:
                        nota_buscada = int(input("Ingresá la nota que estas buscando (1-10): "))

                        # validaciones para que si o si sea una nota entre 1 y 10
                        if 1 <= nota_buscada <= 10:
                            break
                        else:
                            print("La nota debe estar entre 1 y 10.")
                    except ValueError:
                        print("Entrada inválida. Ingrese un número entero entre 1 y 10.")

                # llamado a la funcion que contempla el retorno de la matriz 
                posiciones = buscar_nota(notas, nota_buscada)
                if posiciones:
                    print(f"\nLa nota {nota_buscada} se encontró en la clase:")
                    for pos in posiciones:
                        print(f"Alumno {pos[0] + 1}, exámen: {pos[1] + 1}")
                else:
                    print(f"\nLa nota {nota_buscada} no se encontró en la clase.")
            else:
                print("\nBúsqueda de nota omitida.")

    except ValueError:
        print("Debe ingresar números enteros válidos.")

# validacion extra que impide que se utilice el main desde otro archivo.
if __name__ == "__main__":
    main()
