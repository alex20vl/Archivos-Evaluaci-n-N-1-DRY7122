from xml.etree import ElementTree as ET

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")

root = ET.Element("persona")
nombre_elemento = ET.SubElement(root, "nombre")
nombre_elemento.text = nombre
apellido_elemento = ET.SubElement(root, "apellido")
apellido_elemento.text = apellido

xml_datos = ET.tostring(root, encoding="unicode", method="xml")

print("Datos en formato XML:")
print(xml_datos)
