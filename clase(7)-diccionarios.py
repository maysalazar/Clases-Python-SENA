'''son tio de coleccion donde los elementos tambien se guardan de manera desorndenada y la principal caracteristica de los diccionarios
 es que tienen dos elementos por posicion la CLAVE y el VALOR
 

 los diccionarios tambien aceptan cualquier tipo de dato 

 recordar que los diccionarios se crean con llaves {}

 ejemplo     continuamos modificando'''


# diccionario = {"azul":"blue","rojo":"red","verde":"green"}

# diccionario["amarillo"] = "yellow"    # agregar un nuevo elemento al diccionrio

# diccionario["azul"] = "BLUE"            #si quiero modificar el nombre o colocaro en mayuscula 

# del(diccionario["verde"])             #si quiero eliminar usamos la funcion (del) y colocamos la clave, al momento de ejecutar eliminara la clave y el valor 

# print(diccionario)


# print(diccionario["rojo"])    #si queremos saber como se dice rojo en ingles

# print(diccionario)            # muestra todos los elementos

'''los diccionarios tambien aceptan cualquier tipo de dato como por ejemplo enteros reales, y tambien otras colecciones, 
listas tuplas o inclusive otros diccionarios'''


# diccionario = {"mairon":[29,1.72],"jose":[34,1.83],"maria":[27,1.56]}

# print(diccionario ["mairon"])

# ¿Qué es un diccionario en Python?
# Un diccionario es una estructura de datos que almacena pares clave-valor.
# Permite acceder rápidamente a los valores mediante su clave.

# 1. Crear un diccionario
# diccionario = {"nombre": "Juan", "edad": 25, "ciudad": "Bogotá"}
# print("Diccionario:", diccionario)

# # 2. Acceder a un valor por su clave
# print("Nombre:", diccionario["nombre"])

# # 3. Modificar un valor
# diccionario["edad"] = 26
# print("Diccionario modificado:", diccionario)

# # 4. Agregar un nuevo par clave-valor
# diccionario["profesion"] = "Ingeniero"
# print("Diccionario con nueva clave:", diccionario)

# # 5. Eliminar un elemento con 'del'
# del diccionario["ciudad"]
# print("Diccionario después de eliminar 'ciudad':", diccionario)

# # 6. Obtener todas las claves de un diccionario
# claves = diccionario.keys()
# print("Claves del diccionario:", list(claves))

# # 7. Obtener todos los valores de un diccionario
# valores = diccionario.values()
# print("Valores del diccionario:", list(valores))

# # 8. Obtener todos los pares clave-valor
# elementos = diccionario.items()
# print("Elementos del diccionario:", list(elementos))

# # 9. Recorrer un diccionario con un bucle 'for'
# for clave, valor in diccionario.items():
#     print(f"{clave}: {valor}")

# # 10. Verificar si una clave existe en el diccionario
# print("¿La clave 'edad' está en el diccionario?", "edad" in diccionario)

# # 11. Usar el método 'get()' para obtener un valor
# print("Edad:", diccionario.get("edad", "No disponible"))
# print("Altura:", diccionario.get("altura", "No disponible"))

# # 12. Crear un diccionario con 'dict()'
# otro_diccionario = dict(nombre="Ana", edad=30, ciudad="Medellín")
# print("Otro diccionario:", otro_diccionario)

# # 13. Fusionar dos diccionarios con 'update()'
# diccionario.update({"altura": 1.75, "peso": 70})
# print("Diccionario actualizado:", diccionario)

# # 14. Eliminar todos los elementos de un diccionario
# diccionario.clear()
# print("Diccionario vacío:", diccionario)

# # 15. Crear un diccionario con valores predeterminados
# claves = ["nombre", "edad", "ciudad"]
# diccionario_predeterminado = dict.fromkeys(claves, "Desconocido")
# print("Diccionario con valores predeterminados:", diccionario_predeterminado)



