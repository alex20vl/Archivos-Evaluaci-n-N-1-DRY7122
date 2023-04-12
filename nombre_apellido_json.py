import json

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")

datos = {
    "nombre": nombre,
    "apellido": apellido
}

json_datos = json.dumps(datos, ensure_ascii=False, indent=2)

print("Datos en formato JSON:")
print(json_datos)
