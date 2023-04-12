import yaml

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")

datos = {
    "nombre": nombre,
    "apellido": apellido
}

yaml_datos = yaml.dump(datos, allow_unicode=True)

print("Datos en formato YAML:")
print(yaml_datos)
