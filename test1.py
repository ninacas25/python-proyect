puntaje = 0

preguntas = [
    {
        'texto': '1.-¿Que es una variable en programacion?',
        'opciones': ['Una palabra clave', 'Una operación matemática', 'Un tipo de error', 'Un espacio en la memoria del ordenador donde se almacena un valor o referencia'],
        'respuesta': 'Un espacio en la memoria del ordenador donde se almacena un valor o referencia'
    },
    {
        'texto': '2.-¿Cual es un lenguaje mas "amigable" para aprender a programar?',
        'opciones': ['python', 'java', 'javascript', 'c#'],
        'respuesta': 'python'
    },
    {
        'texto': '3.-¿Que operador se utiliza para comparar la igualdad entre dos valores?',
        'opciones': ['=', '==', ':=', '=+'],
        'respuesta': '=='
    },
    {
        'texto': '4.-¿Cuál es el resultado de la siguiente operacion? 10 % 3',
        'opciones': ['3', '3.33', '3.1', '4.1'],
        'respuesta': '3.1'
    },
    {
        'texto': '5.-¿Que estructura permite ejecutar un bloque de código varias veces según una condicion?',
        'opciones': ['if/else', 'switch', 'do/while o for', 'def'],
        'respuesta': 'do/while o for'
    },
    {
        'texto': '6.-¿Cual es la principal función de un compilador?',
        'opciones': ['ejecutar programas', 'traducir codigo fuente a codigo maquina', 'optimizar imagenes', 'administrar bases de datos'],
        'respuesta': 'traducir codigo fuente a codigo maquina'
    },
    {
        'texto': '7.-¿Como se declara una variable llamada "edad" con valor 25 en JavaScript?',
        'opciones': ['int edad = 25', 'var 25 = edad', 'var edad = 25', 'edad -> 25'],
        'respuesta': 'var edad = 25'
    },
    {
        'texto': '8.-¿Que funcion se utiliza en Python para imprimir un mensaje en consola?',
        'opciones': ['console.log()', 'printf()', 'System.out.print()', 'print()'],
        'respuesta': 'print()'
    },
    {
        'texto': '9.-¿Cual es el valor booleano que representa "verdadero" en python?',
        'opciones': ['0', '1', 'true', 'false'],
        'respuesta': 'true'
    }
]

for pregunta in preguntas:
    print(pregunta["texto"])
    for i, opcion in enumerate(pregunta["opciones"]):
        print(f"{i + 1}. {opcion}")

    respuesta_usuario = int(input("Ingrese el número de su respuesta: "))

    if pregunta["opciones"][respuesta_usuario - 1] == pregunta["respuesta"]:
        puntaje += 1
        print("Correcto!\n")
    else:
        print("Incorrecto\n")

# Calcula el porcentaje de calificación
porcentaje_calificacion = (puntaje / len(preguntas)) * 100 

print(f"Tu puntaje es: {puntaje}/{len(preguntas)}")
print(f"Porcentaje de calificación: {porcentaje_calificacion}%")